import os
import subprocess
from datetime import datetime as dt
from falkonryclient import client as Falkonry

host = os.environ['FALKONRY_HOST_URL'] if os.environ.get('FALKONRY_HOST_URL') else 'https://localhost:8080'
token = os.environ['FALKONRY_TOKEN'] if os.environ.get('FALKONRY_TOKEN') else 't6vl8dty74ngy9r4vy29r6pkth4b4npj'
falkonry = Falkonry(host,token)
falkonry_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

subprocess.call("rm -r {path}/tests/test_transcripts/*.txt".format(path=falkonry_path),shell=True)
subprocess.call('pytest')
files = os.listdir("test_transcripts")
print("Testing Transcripts")


with open("RunTransciptTest.sh",'w') as f:
    f.write('#!/usr/bin/env bash\n')
    for file in files:
        f.writelines("python {falkonry_path}/falkonry.py --test {falkonry_path}/tests/test_transcripts/{file}\n".format(file = file, falkonry_path=falkonry_path))
subprocess.call("/bin/sh {falkonry_path}/tests/RunTransciptTest.sh".format(falkonry_path=falkonry_path),shell=True, stdout=subprocess.PIPE)

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