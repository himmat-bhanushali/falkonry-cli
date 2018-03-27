from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas
import unittest
import re
import subprocess
import json
import datetime

global created_datastream
host = "https://localhost:8080"
token = "t6vl8dty74ngy9r4vy29r6pkth4b4npj"
falkonry = Falkonry(host,token)

path_datastream_add_entity_meta_request = "samples/EntityMetaRequest.json"
path_datastream_add_historical_data = "samples/Input.json"
def file_write(file_name, data):
    with open("test_check/" + str(file_name) + '.txt', 'w') as file:
        file.write(str(data))


class TestDatastream(unittest.TestCase):

    def setUp(self):
        # self.FALKONRY_HOST_URL = "https://localhost:8080"
        # self.FALKONRY_TOKEN = "t6vl8dty74ngy9r4vy29r6pkth4b4npj"
        # self.host = "https://localhost:8080"
        # self.token = "t6vl8dty74ngy9r4vy29r6pkth4b4npj"
        ########################################################################################################################
        # Initialising Dummy datastream for the tests
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health')

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        signal.set_signalIdentifier("signal")
        signal.set_valueIdentifier("value")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        field.set_entityIdentifier('car')
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        ########################################################################################################################

        self.created_datastreams = []
        global created_datastream
        created_datastream = self.created_datastreams #Created a reference
        test_datastream = falkonry.create_datastream(datastream)

        if test_datastream:
            self.test_datastream = test_datastream
            self.created_datastreams.append(test_datastream.get_id())
        self.login_data = """falkonry>> login --host={host} --token={token}\nlogged in to falkonry\n"""\
                .format(host = host, token = token)
        self.default_datastream_data = """falkonry>> datastream_default_set --id {id}
Default datastream set : {id}
""".format(
            id=str(test_datastream.get_id())
        )

    def test_do_login(self):
        """Creates a txt file to for transcript based testing"""
        data = self.login_data
        file_write('test_do_login',data)

    def test_do_logout(self):
        data = self.login_data + """falkonry>> logout\nlogged out from falkonry"""
        file_write('test_do_logout',data)

    def test_do_login_details(self):
        host = falkonry.host
        host = re.sub(r"/",r"\/",host)
        token = falkonry.token
        data = \
"""falkonry>> login_details\nHost : {host}\nToken : /.*/{token}/.*/
""".format(
    host=host,
    token=token
)
        file_write('test_do_login_details',self.login_data+data)

    def test_do_datastream_get_list(self):
        datastreams = falkonry.get_datastreams()
        if datastreams:
            data = \
"""falkonry>> datastream_get_list
Listing Datastreams...
==================================================================================================================
 Datastream Name                               Id                   Created By           Live Status         
==================================================================================================================
/.*/ {name}/.*/ {id}/.*/ {created_by} /.*/{live_status}/.*/
""".format(
    name = str(self.test_datastream.get_name()),
    id = str(self.test_datastream.get_id()),
    created_by = str(self.test_datastream.get_created_by()),
    live_status = str(self.test_datastream.get_live())

)
        else: #todo: Add case when no datastream is present
            data = ''

        file_write("test_do_datastream_get_list", self.login_data + data)
        p = subprocess.Popen('./test.sh')
        (output, error) = p.communicate()
        print("output", output)


    def test_do_datastream_get_by_id(self):
        datastream = self.test_datastream.to_json()
        datastream = json.loads(datastream)
        data = r"""falkonry>> datastream_get_by_id --id {id}
Fetching Datastreams
==================================================================================================================
Id : {id}
Name : {name}
Created By : {created_by}
Create Time : {created_time}
Update Time : {update_time}
Events # : /.*/
Events Start Time : /.*/
Events End Time : /.*/
Time Format : {time_format}
Time Zone : {time_zone}
Live Monitoring: {live}
Signals: /.*/
==================================================================================================================
""".format(
            id = datastream['id'],
            name = datastream['name'],
            created_by = datastream['createdBy'],
            created_time = (str(datetime.datetime.fromtimestamp(datastream['createTime']/1000.0))),
            update_time = (str(datetime.datetime.fromtimestamp(datastream['updateTime']/1000.0))),
            # event = str(datastream['stats']['events']),
            time_format = datastream['field']['time']['format'],
            time_zone = datastream['field']['time']['zone'],#todo:Back slash for space
            live = datastream['live'],
            # signals = '/.*/'
        )
        file_write("test_do_datastream_get_by_id", self.login_data + data)


    def test_do_datastream_default_set(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_default_set --id {id}
Default datastream set : {id}
""".format(
            id=str(datastream.get_id())
        )
        file_write("test_do_datastream_default_set", self.login_data + data)



    def test_do_datastream_default_get(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_default_set --id {id}
Default datastream set : {id}
falkonry>> datastream_default_get
Default datastream set : {id} Name : {name}
""".format(
            id = str(datastream.get_id()),
            name = str(datastream.get_name())
        )
        file_write("test_do_datastream_default_get", self.login_data + data)

    def test_do_datastream_add_entity_meta(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_default_set --id {id}
Default datastream set : {id}
falkonry>> datastream_add_entity_meta --path {path}
Entity Meta successfully added to datastream: {id}
""".format(
            id = str(datastream.get_id()),
            path = path_datastream_add_entity_meta_request
        )
        file_write("test_do_datastream_add_entity_meta", self.login_data + data)

    def test_do_datastream_get_entity_meta(self):
        datastream = self.test_datastream
        entity_meta = falkonry.get_entity_meta(datastream.get_id())
        for entity in entity_meta:
            entity_label = entity.get_label()
            entity_id = entity.get_sourceId()
        #todo: Can loop through and append all the labels
        data = """falkonry>> datastream_default_set --id {id}
Default datastream set : {id}
falkonry>> datastream_get_entity_meta
/.*/Entity Meta of datastream: {id}/.*/
/.*/Entity Label : {entity_label}. Entity Id : {entity_id}/.*/
""".format(
            id = str(datastream.get_id()),
            entity_label = str(entity_label) if entity_label else '/.*/',
            entity_id = str(entity_id) if entity_id else '/.*/'
        )
        file_write("test_do_datastream_get_entity_meta", self.login_data + data)

    def tes_do_datastream_delete(self):
        #todo:Complete for delete
        pass

    def test_do_datastream_get_live_status(self):
        datastream = self.test_datastream
        data="""falkonry>> datastream_get_live_status
Default datastream set : {id} Name : {name}
Fetching Live monitoring status for datastream : {id}
Live Monitoring : {live_status}
""".format(
            id=str(datastream.get_id()),
            name=str(datastream.get_name()),
            live_status = datastream.get_live()
        )
        file_write("test_do_datastream_get_live_status", self.login_data + self.default_datastream_data + data)

    def test_do_datastream_start_live(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_start_live
Default datastream set : {id} Name : {name}
Turning on Live monitoring for datastream : {id}
/(Datastream is {live_status} for live monitoring|Active model is not assigned in any assessment)/
""".format(
            id=str(datastream.get_id()),
            name=str(datastream.get_name()),
            live_status = datastream.get_live()
        )
        file_write("test_do_datastream_start_live", self.login_data + self.default_datastream_data + data)


    def test_do_datastream_stop_live(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_stop_live
Default datastream set : {id} Name : {name}
Turning off Live monitoring for datastream : {id}
/(Datastream is {live_status} for live monitoring|Active model is not assigned in any assessment)/
""".format(
            id=str(datastream.get_id()),
            name=str(datastream.get_name()),
            live_status=datastream.get_live()
        )
        file_write("test_do_datastream_stop_live", self.login_data + self.default_datastream_data + data)


    def test_do_datastream_add_historical_data(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_add_historical_data --path {path} --timeIdentifier "time" --entityIdentifier "car" --timeFormat "iso_8601" --timeZone "GMT" --signalIdentifier "signal" --valueIdentifier "value"
Default datastream set : {id} Name : {name}
/.*/__$id/.*/
""".format(
            path = path_datastream_add_historical_data,
            name = str(datastream.get_name()),
            id = str(datastream.get_id())
        )
        #only __$id is matched coz there is no predefined pattern in which the rest of the response can be checked against
        file_write("test_do_datastream_add_historical_data", self.login_data + self.default_datastream_data + data)

    def test_do_datastream_add_live_data(self):
        datastream = self.test_datastream
        data = """falkonry>> datastream_add_live_data --path {path} --timeIdentifier "time" --entityIdentifier "car" --timeFormat "iso_8601" --timeZone "GMT" --signalIdentifier "signal" --valueIdentifier "value"
Default datastream set : {id} Name : {name}\n/(/.*/__$id/.*/|Datastream is not live, streaming data cannot be accepted.)/
""".format(
            path = path_datastream_add_historical_data,
            name = str(datastream.get_name()),
            id = str(datastream.get_id())
        )
        #only __$id is matched coz there is no predefined pattern in which the rest of the response can be checked against
        file_write("check", self.login_data + self.default_datastream_data + data)


    # @staticmethod#todo:look for optimization
    # def tearDownClass():
    #     for datastream in created_datastream:
    #         try:
    #             falkonry.delete_datastream(datastream)
    #         except:
    #             pass
    #     print('Called')