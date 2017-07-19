import sys
import re
import json
import io
import os
import datetime

from cmd2 import Cmd,make_option,options
from falkonryclient import client as Falkonry
from falkonryclient.helper import schema as Schemas
from pprint import pprint

global _assessmentId
global _datastreamId
global _falkonry
global _self

_self = None
_falkonry = None
_assessmentId = None
_datastreamId = None


class REPL(Cmd):
    prompt = "falkonry>> "

    def __init__(self):
        Cmd.__init__(self)
        global  _self
        _self = self
        print_custom("Welcome to Falkonry Shell !!!", "green")

    @options([make_option('--host', help="host url"),
              make_option('--token',help="auth token")
             ])
    def do_login(self, arg, opts=None):
        """login to the falkonry"""
        if opts.host is None:
            print_error("Please pass host url")
        if opts.token is None:
            print_error("Please pass token")
        if opts.host.find("https://") == -1:
            opts.host = "https://" + opts.host
        #if validate_login('https://dev.falkonry.ai', 'ffwaqz371ae52m4j2f7e3o408b2bf1cv'):
        #if validate_login('https://localhost:8080', 'lmm3orvm1yaa4j1y5b78i8f870fhon6z'):
        if validate_login(opts.host,opts.token):
            print_success("logged in to falkonry")

    def do_logout(self, line):
        """logout from the falkonry"""
        if check_login():
            global _falkonry
            _falkonry = None
            print_success("logged out from falkonry")

    def do_login_details(self, line):
        """get login details"""
        if check_login():
            print_info('Host : ' + _falkonry.host + "\n" + 'Token : ' +_falkonry.token)

    def do_datastream_get_list(self, line):
        """list datastreams"""
        if check_login():
            print_info("Listing Datastreams...")
            print_info("==================================================================================================================")
            datastreamList = _falkonry.get_datastreams()
            if len(datastreamList) == 0 :
                print_info("No Datastreams found")
            print_row("Datastream Name", "Id", "Created By", "Live Status")
            print_info("==================================================================================================================")
            for datastream in datastreamList:
                print_row(datastream.get_name(), datastream.get_id(), datastream.get_created_by(), datastream.get_live())
            print_info("==================================================================================================================")

    @options([make_option('--id', help="datastream id")])
    def do_datastream_get_by_id(self, arg, opts=None):
        """get datastream by id """
        if check_login():
            if opts.id is None:
                print_error("Please pass datastream id")
                return
            print_info("Fetching Datastreams")
            try:
                datastreamObject = _falkonry.get_datastream(opts.id)
                print_datastream_details(datastreamObject.to_json())
            except Exception as error:
                handle_error(error)

    @options([make_option('--id', help="datastream id")])
    def do_datastream_default_set(self, arg, opts=None):
        """set default datastream"""
        if check_login():
            try:
                if opts.id is None:
                    print_error("Please pass datastream id")
                    return
                global _datastreamId
                datastreamObject = _falkonry.get_datastream(opts.id)
                _datastreamId = opts.id
                print_success("Default datastream set : "+ opts.id)
                return
            except Exception as error:
                handle_error(error)
                return

    def do_datastream_default_get(self, line):
        """get default datastream"""
        global _datastreamId
        if check_login():
            if _datastreamId is None:
                print_error("No default datastream set")
                return
            else:
                try:
                    datastreamObject = _falkonry.get_datastream(_datastreamId)
                    print_info("Default datastream set : " + _datastreamId + " Name : " + datastreamObject.get_name())
                except Exception as error:
                    _datastreamId = None;
                    handle_error(error)
                    print_error("Please set the default datastream again")
        return

    @options([make_option('--path', help="file path of request")])
    def do_datastream_create(self,  arg, opts=None):
        """create datastream"""
        if check_login():
            try:
                if opts.path is None:
                    print_error("Please pass json file path for creating datastream")
                    return
                # read file
                try:
                    file_extension = get_file_extension(opts.path)
                    if file_extension != ".json":
                        print_error("Only JSON file is accepted.")
                        return
                    with open(opts.path) as data_file:
                        data = json.load(data_file)
                except Exception as error:
                    print_error("Error in reading file." + str(error))
                    return
                created_datastream = _falkonry.create_datastream(data)
                print_success("Datastream successfully created : "+ created_datastream.get_id())
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--id', help="datastream id")])
    def do_datastream_delete(self, arg, opts=None):
        """delete datastream"""
        if check_login():
            try:
                if opts.id is None:
                    print_error("Please pass datastream id")
                    return
                _falkonry.delete_datastream(opts.id)
                print_success("Datastream successfully deleted : "+ opts.id)
                return
            except Exception as error:
                handle_error(error)
                return

    def do_datastream_start_live(self, line):
        """ turn on live monitoring of datastream """
        global _datastreamId
        if check_login():
            try:
                if check_default_datastream():
                    print_info("Turning on Live monitoring for datastream : " + _datastreamId)
                    _falkonry.on_datastream(_datastreamId)
                return
            except Exception as error:
                handle_error(error)
                return
        return

    def do_datastream_stop_live(self, line):
        """ turn off live monitoring of datastream """
        global _datastreamId
        if check_login():
            try:
                if check_default_datastream():
                    print_info("Turning off Live monitoring for datastream : " + _datastreamId)
                    _falkonry.off_datastream(_datastreamId)
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--path', help="file path of request")])
    def do_datastream_send_historical_data(self, arg, opts=None):
        """ send historical data to datastream for model learning """
        if check_login():
            try:
                if opts.path is None:
                    print_error("Please pass historical data file path")
                    return
                if check_default_datastream():
                    file_extension = get_file_extension(opts.path)
                    if file_extension != ".csv" and file_extension != ".json":
                        print_error("Only CSV or JSON file is accepted.")
                        return
                    data = io.open(opts.path)
                    data_options = {'streaming': False, 'hasMoreData':False}
                    response = _falkonry.add_input_stream(_datastreamId, file_extension.split(".")[1], data_options, data)
                    print_info(str(response))
            except Exception as error:
                handle_error(error)
                return

    @options([make_option('--path', help="file path of request")])
    def do_datastream_send_live_data(self, arg, opts=None):
        """send live data to datastream for live monitoring """
        if check_login():
            try:
                if opts.path is None:
                    print_error("Please pass historical data file path")
                    return
                if check_default_datastream():
                    file_extension = get_file_extension(opts.path)
                    if file_extension != ".csv" and file_extension != ".json":
                        print_error("Only CSV or JSON file is accepted.")
                        return
                    data = io.open(opts.path)
                    data_options = {'streaming': True, 'hasMoreData':False}
                    response = _falkonry.add_input_stream(_datastreamId, file_extension.split(".")[1], data_options, data)
                    print_info(response)
            except Exception as error:
                handle_error(error)
                return
        return

    def do_assessment_get_list(self, line):
        """ list assessments for default datastream"""
        if check_login():
            try:
                if check_default_datastream():
                    print_info("Fetching assessment list of datastream : " + _datastreamId + "...")
                    print_info("==================================================================================================================")
                    assessmentList = _falkonry.get_assessments()
                    if len(assessmentList) == 0:
                        print_info("No assessment found")
                    print_row("Assessment Name", "Id", "Created By", "Live Status")
                    print_info("==================================================================================================================")
                    for assessment in assessmentList:
                        if assessment.get_datastream() == _datastreamId :
                            print_row(assessment.get_name(), assessment.get_id(), assessment.get_created_by(), assessment.get_live())
                    print_info("==================================================================================================================")
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--id', help="assessment id")])
    def do_assessment_get_by_id(self, arg, opts=None):
        """ fetch assessment by id for default datastream"""
        if check_login():
            try:
                if opts.id is None:
                    print_error("Please pass assessment id")
                    return
                assessmentObject = _falkonry.get_assessment(opts.id)
                print_assessment_details(assessmentObject.to_json())
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--path', help="file path of request")])
    def do_assessment_create(self, arg, opts=None):
        """ create assessment in default datastream"""
        if check_login():
            try:
                if opts.path is None:
                    print_error("Please pass json file path for creating assessment")
                    return
                # read file
                try:
                    file_extension = get_file_extension(opts.path)
                    if file_extension != ".json":
                        print_error("Only JSON file is accepted.")
                        return
                    with open(opts.path) as data_file:
                        data = json.load(data_file)
                except Exception as error:
                    print_error("Error in reading file." + str(error))
                    return
                created_assessment = _falkonry.create_assessment(data)
                print_success("Assessment successfully created : "+ created_assessment.get_id())
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--id', help="assessment id")])
    def do_assessment_delete(self, arg, opts=None):
        """ delete assessment by id default datastream"""
        if check_login():
            try:
                if opts.id is None:
                    print_error("Please pass assessment id")
                    return
                _falkonry.delete_assessment(opts.id)
                print_info("Assessment deleted successfully: " + opts.id)
                return
            except Exception as error:
                handle_error(error)
                return
        return

    @options([make_option('--id', help="assessment id")])
    def do_assessment_default_set(self, arg, opts=None):
        """ set default assessment"""
        if check_login():
            try:
                if opts.id is None:
                    print_error("Please pass assessment id")
                    return
                if check_default_datastream():
                    global _assessmentId
                    assessmentObj = _falkonry.get_assessment(opts.id)
                    _assessmentId = opts.id
                    print_success("Default assessment set : "+ opts.id)
                return
            except Exception as error:
                handle_error(error)
                return
        return

    def do_assessment_default_get(self, line):
        """ get default assessment"""
        global _assessmentId
        if check_login():
            if _assessmentId is None:
                print_error("No default assessment set")
                return
            else:
                try:
                    assessmentObj = _falkonry.get_assessment(_assessmentId)
                    print_info("Default assessment set : " + _assessmentId + " Name : " + assessmentObj.get_name())
                except Exception as error:
                    _assessmentId = None;
                    handle_error(error)
                    print_error("Please set the default assessment again")
        return

    @options([make_option('--path', help="file path of facts file")])
    def do_assessment_add_facts(self, arg, opts=None):
        """ add facts to assessment"""
        if check_login():
            try:
                if opts.path is None:
                    print_error("Please pass facts data file path")
                    return
                if check_default_assessment():
                    file_extension = get_file_extension(opts.path)
                    if file_extension != ".csv" and file_extension != ".json":
                        print_error("Only CSV or JSON file is accepted.")
                        return
                    data = io.open(opts.path)
                    response = _falkonry.add_facts_stream(_assessmentId, file_extension.split(".")[1], {}, data)
                    print_info(str(response))
                return
            except Exception as error:
                handle_error(error)
                return
        return


    '''@options([make_option('--path', help="file path to write output")])
    @options([make_option('--trackerId', help="tracker id of the previous output request")])
    @options([make_option('--modelIndex', help="index of the model of which output needs to be fetched ")])
    @options([make_option('--startTime', help="startTime of the output range")])
    @options([make_option('--endTime', help="endTime of the output range")])'''
    def do_assessment_get_historical_output(self, arg, opts=None):
        """ get learn/test output of assessment"""
        '''if check_login():
            try:
                if check_default_assessment():
                    if opts.trackerId is None and opts.modelIndex is None:
                        print_error("TrackerID or modelIndex is need to be passed")
                    print_info(str(response))
                return
            except Exception as error:
                errorObj = json.loads(error.message)
                print_error(errorObj['message'])
                return'''
        return

    def do_assessment_output_listen(self, arg, opts=None):
        """ get live output of assessment"""
        return


def validate_login(host,token):
    """validate Login"""
    try:
        global _falkonry
        if not(not host or not token):
            p = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            m = p.match(host)
            if m:
                _falkonry = Falkonry(host=host, token=token, options={"header":"falkonry-cli"})
                # test auth token validation
                try:
                    datastream = _falkonry.get_datastream('test-id')
                except Exception as error:
                    if hasattr(error, 'message'):
                        errorObj = json.loads(error.message)
                        if errorObj['message'] == "Unauthorized Access":
                            print_error('Unauthorized Access. Please verify your details.')
                            _falkonry = None
                            return False
                        elif errorObj['message'] == "No such Datastream available":
                            return True
                        else:
                            _falkonry = None
                            return False
                    else:
                        _falkonry = None
                        print_error('Unable to connect to falkonry. Please verify your details.')
                        return False
            else:
                print_error("Invalid Host Url")
                return False
    except Exception as error:
        _falkonry = None
        print_error('Unable to connect to falkonry. Please verify your details.')
        return False


def check_default_datastream():
    global _datastreamId
    if _datastreamId is None:
        print_error("Set default datastream first")


def check_login():
    if _falkonry is None:
        print_error("Please login first")
        return False
    else:
        return True


def print_info(msg):
    print _self.colorize(msg, "blue")


def print_success(msg):
    print _self.colorize(msg, "green")


def print_error(msg):
    print _self.colorize(msg + "\n Try help <command> for info", "red")


def print_custom(msg, color):
    print _self.colorize(msg, color)


def get_file_extension(path):
    file_extension = os.path.splitext(path)
    return file_extension[1]


def check_default_datastream():
    global _datastreamId
    if check_login():
        if _datastreamId is None:
            print_error("No default datastream set")
            return
        else:
            try:
                datastreamObject = _falkonry.get_datastream(_datastreamId)
                print_info("Default datastream set : " + _datastreamId + " Name : " + datastreamObject.get_name())
                return True
            except Exception as error:
                _datastreamId = None;
                errorObj = json.loads(error.message)
                print_error(errorObj['message'])
                print_error("Please set the default datastream again")
                return False
    return


def check_default_assessment():
    global _assessmentId
    if check_login():
        if _assessmentId is None:
            print_error("No default assessment set")
            return
        else:
            try:
                assessmentObj = _falkonry.get_assessment(_assessmentId)
                print_info("Default assessment set : " + _assessmentId + " Name : " + assessmentObj.get_name())
                return True
            except Exception as error:
                _assessmentId = None;
                errorObj = json.loads(error.message)
                print_error(errorObj['message'])
                print_error("Please set the default assessment again")
                return False
    return


def print_row(name, id, user_id, live_status):
    print_info(" %-45s %-20s %-20s %-20s" % (name, id, user_id, live_status))


def handle_error(error):
    try:
        errorObj = json.loads(error.message)
        print_error(errorObj['message'])
    except Exception as error_new:
        print _self.colorize("Unhandled Exception : " + str(error), "red")

def print_datastream_details(datastream_str):
    datastream = json.loads(datastream_str)
    print_info("==================================================================================================================")
    print_info("Id : " + datastream['id'])
    print_info("Name : " + datastream['name'])
    print_info("Created By : " + datastream['createdBy'])
    print_info("Create Time : " + (str(datetime.datetime.fromtimestamp(datastream['createTime']/1000.0))))
    print_info("Update Time : " + (str(datetime.datetime.fromtimestamp(datastream['updateTime']/1000.0))))
    print_info("Events # : " + str(datastream['stats']['events']))
    if datastream['stats']['events'] > 0:
        print_info("Events Start Time : " + (str(datetime.datetime.fromtimestamp(datastream['stats']['earliestDataPoint']/1000.0))))
        print_info("Events End Time : " + (str(datetime.datetime.fromtimestamp(datastream['stats']['latestDataPoint']/1000.0))))
    else:
        print_info("Events Start Time : N/A")
        print_info("Events End Time : N/A")
    print_info("Time Format : " + datastream['field']['time']['format'])
    print_info("Time Zone : " + datastream['field']['time']['zone'])
    #print_info("Assessments: " + datastream.get_create_time())
    print_info("Live Monitoring: " + datastream['live'])
    if len(datastream['inputList']):
        signalList=[]
        for input in datastream['inputList']:
            signalList.append(input['name'])
        print_info("Signals: " +', '.join(signalList))
    else:
        print_info("Signals: N/A")
    #print_info("Entities: " + datastream['dataSource'])
    print_info("==================================================================================================================")


def print_assessment_details(assessment_str):
    assessment = json.loads(assessment_str)
    print_info("==================================================================================================================")
    print_info("Id : " + assessment['id'])
    print_info("Name : " + assessment['name'])
    print_info("Created By : " + assessment['createdBy'])
    print_info("Create Time : " + (str(datetime.datetime.fromtimestamp(assessment['createTime']/1000.0))))
    print_info("Update Time : " + (str(datetime.datetime.fromtimestamp(assessment['updateTime']/1000.0))))
    print_info("Datastream : " + assessment['datastream'])
    print_info("Live : " + assessment['live'])
    print_info("Rate : " + assessment['rate'])
    if len(assessment['aprioriConditionList']) ==0:
        print_info("Apriori Condition List : N/A")
    else:
        print_info("Apriori Condition List : " + ', '.assessment['aprioriConditionList'])
    print_info("==================================================================================================================")


def cli():
    app = REPL()
    app.cmdloop()

if __name__ == '__main__':
    cli()
