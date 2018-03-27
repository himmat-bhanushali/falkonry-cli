import os
import sys
import subprocess
from datetime import datetime as dt
p = subprocess.call('pytest')
files = os.listdir("test_transcripts")
print("Testing Transcripts")
with open("RunTransciptTest.sh",'w') as f:
    f.write('#!/usr/bin/env bash\n')
    for file in files:
        f.writelines("python /home/jaipreet/Projects/falkonry_src/falkonry-cli/falkonry.py --test /home/jaipreet/Projects/falkonry_src/falkonry-cli/tests/test_transcripts/{file}\n".format(file = file))
error_log_file = open('logs/ErrorTestLog{time}.txt'.format(time=dt.now()),'w')
output_log_file = open('logs/OutputTestLog{time}.txt'.format(time=dt.now()),'w')
process = subprocess.Popen("/bin/sh /home/jaipreet/Projects/falkonry_src/falkonry-cli/tests/RunTransciptTest.sh".format(time=str(datetime.datetime.now())),shell=True, stdout=output_log_file, stderr=error_log_file)
error_log_file.close()
output_log_file.close()