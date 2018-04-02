import os
import subprocess
from datetime import datetime as dt
from falkonryclient import client as Falkonry

host = os.environ['FALKONRY_HOST_URL']
token = os.environ['FALKONRY_TOKEN']
falkonry = Falkonry(host,token)
falkonry_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_test_transcripts = falkonry_path + "/tests/test_transcripts"

try:
    files = os.listdir(path_test_transcripts)
    if(len(files) > 1):
        subprocess.call("rm -r {path}/tests/test_transcripts/*".format(path=falkonry_path),shell=True)
except Exception as e:
    print(e)

subprocess.call('python {path}/tests/test_assessment.py'.format(path=falkonry_path),shell=True)
subprocess.call('python {path}/tests/test_datastream.py'.format(path=falkonry_path),shell=True)

files = os.listdir("{path}/tests/test_transcripts".format(path=falkonry_path))
print("Testing Transcripts")


with open("RunTranscriptTest.sh",'w') as f:
    f.write('#!/usr/bin/env bash\n')
    for file in files:
        f.writelines("python {falkonry_path}/falkonry.py --test {falkonry_path}/tests/test_transcripts/{file}\n".format(file = file, falkonry_path=falkonry_path))
subprocess.call("/bin/sh {falkonry_path}/tests/RunTranscriptTest.sh".format(falkonry_path=falkonry_path),shell=True, stdout=subprocess.PIPE)

############### Clean Up ##########################
with open('{path}/tests/resources/datastreams.txt'.format(path=falkonry_path)) as f:
    datastreams_test_datastream = f.read()
    datastreams_test_datastream = datastreams_test_datastream.split('\\')

with open('{path}/tests/resources/assessments.txt'.format(path=falkonry_path)) as f:
    datastreams_test_assessment = f.read()
    datastreams_test_assessment = datastreams_test_assessment.split('\\')

datastreams = list(set(datastreams_test_assessment + datastreams_test_datastream))
for datastream in datastreams:
    if(datastream !=''):
        falkonry.delete_datastream(datastream)
subprocess.call("rm {path}/tests/resources/assessments.txt {path}/tests/resources/datastreams.txt".format(path=falkonry_path),shell=True)
####################################################