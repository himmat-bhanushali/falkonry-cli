from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas
import unittest
import json
import datetime
import os


global created_datastream
host = os.environ['FALKONRY_HOST_URL']
token = os.environ['FALKONRY_TOKEN']
falkonry = Falkonry(host,token)
falkonry_path = os.path.dirname(os.path.abspath(__file__))

path_assessment_add_facts = "{path}/resources/AddFacts.json".format(path=falkonry_path)
path_datastream_add_historical_data = "tests/resources/Input.json"
def file_write(file_name, data):
    with open("{path}/tests/test_transcripts/".format(path=falkonry_path) + str(file_name) + '.txt', 'w') as file:
        file.write(str(data))


class TestAssessment(unittest.TestCase):

    def setUp(self):
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
        global created_datastreams
        created_datastreams = self.created_datastreams #Created a reference
        test_datastream = falkonry.create_datastream(datastream)
########################################################################################################################

        assessment_req = Schemas.AssessmentRequest()
        assessment_req.set_name("Assessement_name")
        assessment_req.set_datastream(test_datastream.get_id())
        assessment_req.set_rate('PTOS')
########################################################################################################################

        self.created_assessments = []
        global created_assessments
        created_assessments = self.created_assessments #Created a reference
        test_assessment = falkonry.create_assessment(assessment_req)

        if test_datastream:
            self.test_datastream = test_datastream
            self.created_datastreams.append(test_datastream.get_id())
        if test_assessment:
            self.test_assessment = test_assessment
            self.created_assessments.append(test_assessment.get_id())

        self.login_data = """falkonry>> login --host={host} --token={token}\nlogged in to falkonry\n"""\
                .format(host = host, token = token)
        self.default_datastream_data = """falkonry>> datastream_default_set --id {id}\nDefault datastream set : {id}\n"""\
                .format(
            id=str(test_datastream.get_id())
        )
        self.default_assessment_data ="""falkonry>> assessment_default_set --id {assessment_id}
Default datastream set : {datastream_id} Name : {datastream_name}
/(Default assessment set : {assessment_id}|Assessment id : {assessment_id} does not belong to default datastream)/
""".format(
            assessment_id = str(test_assessment.get_id()),
            datastream_id = str(test_datastream.get_id()),
            datastream_name = str(test_datastream.get_name())
        )


    def test_do_assessment_get_list(self):
        datastreams = falkonry.get_datastreams()
        assessments = falkonry.get_assessments()
        assessmentList = []
        for assessment in assessments:
            if assessment.get_datastream() == self.test_datastream.get_id():
                assessmentList.append(assessment)
        if len(assessmentList) > 0:
            data = \
"""falkonry>> assessment_get_list 
Default datastream set : {datastream_id} Name : {datastream_name}
Fetching assessment list of datastream : {datastream_id}...
==================================================================================================================
 Assessment Name                               Id                   Created By           Live Status         
==================================================================================================================
/.*/{assessment_name}/.*/{assessment_id}/.*/{created_by}/.*/{assessment_live_status}/.*/
""".format(
    datastream_name = str(self.test_datastream.get_name()),
    datastream_id = str(self.test_datastream.get_id()),
    assessment_name = str(assessmentList[-1].get_name()),
    assessment_id = str(assessmentList[-1].get_id()),
    created_by = str(assessmentList[-1].get_created_by()),
    assessment_live_status = str(assessmentList[-1].get_live())

)
        else:
            data=\
"""falkonry>> assessment_get_list 
Default datastream set : {datastream_id} Name : {datastream_name}
Fetching assessment list of datastream : {datastream_id}...
/.*/No assessment found/.*/
""".format(
    datastream_name=str(self.test_datastream.get_name()),
    datastream_id=str(self.test_datastream.get_id()),
)

        file_write("test_do_assessment_get_list", self.login_data + self.default_datastream_data + data)
        # p = subprocess.Popen('./test.sh')
        # (output, error) = p.communicate()
        # print("output", output)

#
    def test_do_assessment_get_by_id(self):
        assessment = self.test_assessment.to_json()
        assessment = json.loads(assessment)
        datastream = self.test_datastream
        data = r"""falkonry>> assessment_get_by_id --id {assessment_id}
==================================================================================================================
Id : {assessment_id}
Name : {assessment_name}
Created By : {assessment_created_by}
Create Time : {assessment_created_time}
Update Time : {assessment_update_time}
Datastream : {datastream_id}
Live : {assessment_live}
Rate : {assessment_rate}
/(Condition List|Apriori Condition List)/ : /.*/
==================================================================================================================
""".format(
            assessment_id = assessment['id'],
            assessment_name = assessment['name'],
            assessment_created_by = assessment['createdBy'],
            assessment_created_time = (str(datetime.datetime.fromtimestamp(assessment['createTime']/1000.0))),
            assessment_update_time = (str(datetime.datetime.fromtimestamp(assessment['updateTime']/1000.0))),
            datastream_id = assessment['datastream'],
            assessment_live = assessment['live'],
            assessment_rate = assessment['rate']
        )
        file_write("test_do_assessment_get_by_id", self.login_data + data)

    def test_do_assessment_create(self):
        datastream = self.test_datastream
        with open("{path}/resources/AssessmentRequest.json".format(path=falkonry_path),'w') as f:
            f.write("{"+\
                    """
  "name":"New Test Assessment",
  "datastream": "{id}",
  "rate": "PT0S"
""".format(id=str(datastream.get_id()))+\
                    "}")

        data = \
"""falkonry>> assessment_create --path {path}/resources/AssessmentRequest.json
Default datastream set : {datastream_id} Name : {datastream_name}
Assessment successfully created : /.*/
""".format(
        path = falkonry_path,
        datastream_name = datastream.get_name(),
        datastream_id = datastream.get_id()
    )
        file_write('test_do_assessment_create',self.login_data + self.default_datastream_data + data)

    def test_do_assessment_delete(self):
        assessment_req = Schemas.AssessmentRequest()
        assessment_req.set_name("TestAssessmentDelete")
        assessment_req.set_datastream(self.test_datastream.get_id())
        assessment_req.set_rate('PTOS')
        assessment = falkonry.create_assessment(assessment_req)

        data = \
"""falkonry>> assessment_delete --id {id}
Assessment deleted successfully: {id}
""".format(id=assessment.get_id())
        file_write('test_do_assessment_delete', self.login_data + data)


    def test_do_assessment_default_set(self):
        assessment = self.test_assessment
        datastream = self.test_datastream
        data = """falkonry>> assessment_default_set --id {assessment_id}
Default datastream set : {datastream_id} Name : {datastream_name}
/(Default assessment set : {assessment_id}|Assessment id : {assessment_id} does not belong to default datastream)|No such Datastream available/
""".format(
            assessment_id = str(assessment.get_id()),
            datastream_id = str(datastream.get_id()),
            datastream_name = str(datastream.get_name())
        )
        file_write("test_do_assessment_default_set", self.login_data +self.default_datastream_data + data)


    def test_do_assessment_default_get(self):
        assessment = self.test_assessment
        datastream = self.test_datastream
        data = """falkonry>> assessment_default_get
Default assessment set : {assessment_id} Name : {assessment_name}
""".format(
            assessment_id = str(assessment.get_id()),
            assessment_name = str(assessment.get_name()),
            datastream_id = str(datastream.get_id()),
            datastream_name = str(datastream.get_name())
        )
        file_write("test_do_assessment_default_get", self.login_data + self.default_datastream_data +self.default_assessment_data + data)


    def test_do_assessment_add_facts(self):
        assessment = self.test_assessment
        datastream = self.test_datastream
        data = r"""falkonry>> assessment_add_facts --path "tests/resources/AddFacts.json" --startTimeIdentifier "time" --endTimeIdentifier "end" --timeFormat "iso_8601" --timeZone "GMT" --valueIdentifier "Health" --entityIdentifier "car"
Default assessment set : {id} Name : {name}
/.*/
""".format(
            path = path_assessment_add_facts,
            name = str(assessment.get_name()),
            id = str(assessment.get_id())
        )
        #only __$id is matched coz there is no predefined pattern in which the rest of the response can be checked against
        file_write("test_do_assessment_add_facts", self.login_data + self.default_datastream_data +self.default_assessment_data + data)


    def test_do_assessment_get_historical_output(self):
        assessment = self.test_assessment
        datastream = self.test_datastream
        data = r"""falkonry>> assessment_get_historical_output --startTime "2017-07-19T14:04:06+05:30" --format "text/csv"
Default assessment set : {id} Name : {name}
/(/.*/__id/.*/
Falkonry is generating your output. Please try following command in some time.
assessment_get_historical_output --trackerId=/.*/|No models found for Assessment : {id})|/.*//
""".format(
            name = str(assessment.get_name()),
            id = str(assessment.get_id())
        )
        #only __$id is matched coz there is no predefined pattern in which the rest of the response can be checked against
        file_write("test_do_assessment_get_historical_output", self.login_data + self.default_datastream_data +self.default_assessment_data + data)


    def test_do_assessment_output_listen(self):
        assessment = self.test_assessment
        datastream = self.test_datastream
        data = r"""falkonry>> assessment_output_listen --format "application/json"
Default assessment set : {id} Name : {name}
/(Assessment is not in production|Fetching live assessments : )//.*/
""".format(
            name = str(assessment.get_name()),
            id = str(assessment.get_id())
        )
        file_write("test_do_assessment_output_listen", self.login_data + self.default_datastream_data +self.default_assessment_data + data)

    def test_do_assessment_get_facts_with_path(self):
        datastream = falkonry.get_datastream(os.environ.get("FALKONRY_DATASTREAM_SLIDING_ID")) if os.environ.get("FALKONRY_DATASTREAM_SLIDING_ID") else self.test_datastream
        assessment = falkonry.get_assessment(os.environ.get("FALKONRY_ASSESSMENT_SLIDING_ID")) if os.environ.get("FALKONRY_ASSESSMENT_SLIDING_ID") else self.test_assessment
        facts_data = falkonry.get_facts(assessment.get_id(),{})
        default_datastream_data = """falkonry>> datastream_default_set --id {id}\nDefault datastream set : {id}\n""" \
            .format(
            id=str(datastream.get_id())
        )
        default_assessment_data = \
"""falkonry>> assessment_default_set --id {assessment_id}
Default datastream set : {datastream_id} Name : {datastream_name}
/(Default assessment set : {assessment_id}|Assessment id : {assessment_id} does not belong to default datastream)/
""".format(
            assessment_id=str(assessment.get_id()),
            datastream_id=str(datastream.get_id()),
            datastream_name=str(datastream.get_name())
        )

        data = \
"""falkonry>> assessment_get_facts --path {path}/test_transcripts/TestAssessmentDataRemove
Default assessment set : {assessment_id} Name : {assessment_name}
Facts data is written to the file : /.*/TestAssessmentDataRemove/.*/""".format(
            path = falkonry_path,
            data = str(facts_data.text),
            assessment_id = str(assessment.get_id()),
            assessment_name = str(assessment.get_name())
        )
        file_write("test_do_assessment_get_facts_with_path", self.login_data + default_datastream_data + default_assessment_data + data)


    def test_do_assessment_get_facts_without_path(self):
        datastream = falkonry.get_datastream(os.environ.get("FALKONRY_DATASTREAM_SLIDING_ID")) if os.environ.get("FALKONRY_DATASTREAM_SLIDING_ID") else self.test_datastream
        assessment = falkonry.get_assessment(os.environ.get("FALKONRY_ASSESSMENT_SLIDING_ID")) if os.environ.get("FALKONRY_ASSESSMENT_SLIDING_ID") else self.test_assessment
        facts_data = falkonry.get_facts(assessment.get_id(),{})
        default_datastream_data = """falkonry>> datastream_default_set --id {id}\nDefault datastream set : {id}\n""" \
            .format(
            id=str(datastream.get_id())
        )
        default_assessment_data = \
"""falkonry>> assessment_default_set --id {assessment_id}
Default datastream set : {datastream_id} Name : {datastream_name}
/(Default assessment set : {assessment_id}|Assessment id : {assessment_id} does not belong to default datastream)/
""".format(
            assessment_id=str(assessment.get_id()),
            datastream_id=str(datastream.get_id()),
            datastream_name=str(datastream.get_name())
        )

        data = \
"""falkonry>> assessment_get_facts
Default assessment set : {assessment_id} Name : {assessment_name}
Facts Data : 
==================================================================================================================
{data}/.*/
""".format(
            data=str(facts_data.text),
            assessment_id = str(assessment.get_id()),
            assessment_name = str(assessment.get_name())
        )
        file_write("check", self.login_data + default_datastream_data + default_assessment_data + data)


    # todo:look for optimization
    def tearDown(self):
        with open('resources/assessments.txt','w') as file:
            for ds in created_datastreams:
                file.write(ds)
                file.write("\\")

if __name__ == "__main__":
    unittest.main()
