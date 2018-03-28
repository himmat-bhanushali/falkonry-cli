import os
import subprocess
from datetime import datetime as dt


subprocess.call('pytest')
files = os.listdir("test_transcripts")
falkonry_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Testing Transcripts")

with open("RunTransciptTest.sh",'w') as f:
    f.write('#!/usr/bin/env bash\n')
    for file in files:
        f.writelines("python {falkonry_path}/falkonry.py --test {falkonry_path}/tests/test_transcripts/{file}\n".format(file = file, falkonry_path=falkonry_path))
subprocess.call("/bin/sh {falkonry_path}/tests/RunTransciptTest.sh".format(falkonry_path=falkonry_path),shell=True, stdout=subprocess.PIPE)
