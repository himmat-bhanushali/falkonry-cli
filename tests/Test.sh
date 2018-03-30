#!/usr/bin/env bash

touch RunTranscriptTest.sh
chmod +x RunTranscriptTest.sh
mkdir -p test_transcripts
python testDriver.py
