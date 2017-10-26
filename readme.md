# Falkonry CLI tool
[![Falkonry Logo](https://app.falkonry.ai/img/logo.png)](http://falkonry.com/)

[![Build status](https://img.shields.io/travis/Falkonry/falkonry-python-client.svg?style=flat-square)](https://travis-ci.org/Falkonry/falkonry-python-client)

Falkonry CLI tool to access [Falkonry Condition Prediction](falkonry.com) APIs

[Releases](https://github.com/Falkonry/falkonry-cli/releases)

## Installation
Installation may require administrative privileges in some operating systems

```bash
$ pip install falkonry-cli
```

## Requirements
```
* Supported Python: Python 2.7
* Supported Platform : MacOS / Windows 7 or higher/ Ubuntu 14.0 or higher
```
## Features Supported
#### Utility features
```
* help
* history
* login
* logout
* login_details
* quit
* exit
```
#### Falkonry specific features (You need to log in for using any of the below features)
```
* Create Datastream for narrow/historian style data from a single entity
* Create Datastream for narrow/historian style data from multiple entities
* Create Datastream for wide style data from a single entity
* Create Datastream for wide style data from multiple entities
* Create Datastream with microseconds precision
* Retrieve Datastreams
* Retrieve Datastream by Id
* Delete Datastream
* Set default Datastream
* Get default Datastream
* Add EntityMeta to a Datastream
* Get EntityMeta of a Datastream
* Add historical input data to Datastream
* Add live input data to Datastream
* Create Assessment
* Retrieve Assessments
* Retrieve Assessment by Id
* Delete Assessment
* Set default Assessment
* Get default Assessment
* Get Condition List Of Assessment
* Add facts data to Assessment
* Get Historian Output from Assessment
* Get Streaming Output
* Get Facts Data
* Get Datastream Data
* Datastream On (Start live monitoring of datastream)
* Datastream Off (Stop live monitoring of datastream)
```

## Quick Start
```
* Get auth token from Falkonry Service UI
* Type falkonry on your terminal it will land you in falkonry shell
* Read the examples provided for integration with various data formats
```

## Examples

#### Run Falkonry CLI
Type "falkonry" in command prompt/terminal it will land you in the falkonry shell.
```
user$ falkonry
Welcome to Falkonry Shell !!!
falkonry>>
```
#### Help
For help type either "help" or "?". After this, all the available functions will be displayed on the console.
```
falkonry>> help

Documented commands (type help <topic>):
========================================

_relative_load                    datastream_add_live_data    history      
assessment_add_facts              datastream_create           load         
assessment_create                 datastream_default_get      login        
assessment_default_get            datastream_default_set      login_details
assessment_default_set            datastream_delete           logout       
assessment_delete                 datastream_get_by_id        py           
assessment_get_by_id              datastream_get_data         pyscript     
assessment_get_facts              datastream_get_entity_meta  quit         
assessment_get_historical_output  datastream_get_list         run          
assessment_get_list               datastream_start_live       save         
assessment_output_listen          datastream_stop_live        set          
cmdenvironment                    edit                        shell        
datastream_add_entity_meta        exit                        shortcuts    
datastream_add_historical_data    help                        show         
falkonry>>
```

for getting help on particular topic type "help <topic>" or "? <topic>"

```
falkonry>> help login
login to the falkonry
Usage: login [options] arg

Options:
-h, --help show this help message and exit
--host=HOST URL of the host
--token=TOKEN auth token

falkonry>>
```

#### history
For going through the history of commands in the current session type "history"
```
falkonry>> history
-------------------------[1]
help
-------------------------[2]
? login
falkonry>>
```

#### login
For login use host and authorization token.
```
falkonry>> login --host=https://localhost:8080 --token=el7rvvqx2xr6v5-30qba1dl0pu36pi
logged in to falkonry
falkonry>>
```
If wrong url or token is passed appropriate error will be displayed.

#### login_details
For login details type "login_details"
```
falkonry>> login_details
Host : https://localhost:8080
Token : el7rvvqx2xr6v5-30qba1dl0pu36pi
falkonry>>
```

#### logout
For logging out of the current falkonry session
```
falkonry>> logout
logged out from falkonry
falkonry>>
```

#### quit / exit / Ctr+C
For exiting from falkonry shell type "quit", "exit" or press "Ctr+C"
```
falkonry>> quit
user$
```

#### Create Datastream for narrow/historian style data from a single entity

Data :

```
{"time" :"2016-03-01 01:01:01", "tag" : "signal1", "value" : 3.4}
{"time" :"2016-03-01 01:01:02", "tag" : "signal2", "value" : 9.3}

or

time, tag, value
2016-03-01 01:01:01, signal1, 3.4
2016-03-01 01:01:02, signal2, 9.3

```
Sample JSONFile:
```
{
"name": "Test DS",
"dataSource": {
"type": "STANDALONE"
},
"field": {
"time": {
"zone": "Asia/Calcutta",
"identifier": "time",
"format": "YYYY-MM-DD HH:mm:ss"
},
"signal": {
"tagIdentifier": "tag",
"valueIdentifier": "value",
"delimiter": null,
"isSignalPrefix": false
}
}
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/DatastreamRequest.json
Datastream successfully created : anbsivd1h7h1sd
falkonry>>
```

#### Create Datastream for narrow/historian style data from multiple things

Data :

```
{"time" :"2016-03-01 01:01:01", "tag" : "signal1_thing1", "value" : 3.4}
{"time" :"2016-03-01 01:01:01", "tag" : "signal2_thing1", "value" : 1.4}
{"time" :"2016-03-01 01:01:02", "tag" : "signal1_thing2", "value" : 9.3}
{"time" :"2016-03-01 01:01:02", "tag" : "signal2_thing2", "value" : 4.3}

or

time, tag, value
2016-03-01 01:01:01, signal1_thing1, 3.4
2016-03-01 01:01:01, signal2_thing1, 1.4
2016-03-01 01:01:02, signal1_thing2, 9.3
2016-03-01 01:01:02, signal2_thing2, 4.3
```

Sample JSONFile:
```
{
"name": "Test DS",
"dataSource": {
"type": "STANDALONE"
},
"field": {
"time": {
"zone": "Asia/Calcutta",
"identifier": "time",
"format": "YYYY-MM-DD HH:mm:ss"
},
"signal": {
"tagIdentifier": "tag",
"valueIdentifier": "value",
"delimiter": "_",
"isSignalPrefix": true
}
}
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/DatastreamRequest.json
Datastream successfully created : anbsivd1h7h1sd
falkonry>>
```

#### Create Datastream for wide style data from a single entity

Data :

```
{"time":1467729675422, "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
{"time":1467729668919, "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

or

time, signal1, signal2, signal3, signal4
1467729675422, 41.11, 62.34, 77.63, 4.8
1467729675445, 43.91, 82.64, 73.63, 3.8
```

Sample JSONFile:
```
{
"name": "New Ds -1",
"dataSource": {
"type": "STANDALONE"
},
"field": {
"time": {
"zone": "Asia/Calcutta",
"identifier": "time",
"format": "millis"
},
"entityIdentifier": null
},
"inputList": [
{
"name": "signal1",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal2",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal3",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal4",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
}
]
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/DatastreamRequest.json
Datastream successfully created : anb109d1h7h1po
falkonry>>
```

#### Create Datastream for wide style data from multiple entities

Data :

```python
{"time":1467729675422, "thing": "Thing1", "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
{"time":1467729668919, "thing": "Thing2", "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

or

time, thing, signal1, signal2, signal3, signal4
1467729675422, thing1, 41.11, 62.34, 77.63, 4.8
1467729675445, thing1, 43.91, 82.64, 73.63, 3.8
```

Sample JSONFile:
```
{
"name": "New Ds -1",
"dataSource": {
"type": "STANDALONE"
},
"field": {
"time": {
"zone": "Asia/Calcutta",
"identifier": "time",
"format": "millis"
},
"entityIdentifier": "things"
},
"inputList": [
{
"name": "signal1",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal2",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal3",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
},
{
"name": "Signal4",
"valueType": {
"type": "Numeric"
},
"eventType": {
"type": "Samples"
}
}
]
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/DatastreamRequest.json
Datastream successfully created : anb109d1h7h1po
falkonry>>
```

#### Create Datastream with microseconds precision

Data :

```
{"time" :"2016-03-01 01:01:01", "tag" : "signal1", "value" : 3.4}
{"time" :"2016-03-01 01:01:02", "tag" : "signal2", "value" : 9.3}

or

time, tag, value
2016-03-01 01:01:01, signal1, 3.4
2016-03-01 01:01:02, signal2, 9.3

```
Sample JSONFile:
```
{
"name": "Test DS",
"dataSource": {
"type": "STANDALONE"
},
"field": {
"time": {
"zone": "Asia/Calcutta",
"identifier": "time",
"format": "YYYY-MM-DD HH:mm:ss"
},
"signal": {
"tagIdentifier": "tag",
"valueIdentifier": "value",
"delimiter": null,
"isSignalPrefix": false
}
},
"timePrecision": "micro" // this is use to store your data in different date time format. You can store your data in milliseconds("millis") or microseconds("micro"). Default will be "millis"
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/DatastreamRequest.json
Datastream successfully created : anbsivd1h7h1sd
falkonry>>
```

#### Retrieve Datastreams

Fetch list of datastreams
```
falkonry>> datastream_get_list
Listing Datastreams...
==================================================================================================================
Datastream Name Id Created By Live Status
==================================================================================================================
New Ds -1 oii0djojxc2lxt Tza1q4g0kw5epo OFF
Example DS-1 5v8drr2eqtp7cy Y36zulie5as5bu OFF
Sample Datastream z0cenywoi3jlxj Tza1q4g0kw5epo OFF
==================================================================================================================
falkonry>>
```

#### Retrieve Datastream by id
```
falkonry>> datastream_get_by_id --id=oii0djojxc2lxt
Fetching Datastreams
==================================================================================================================
Id : oii0djojxc2lxt
Name : New Ds -1
Created By : Tza1q4g0kw5epo
Create Time : 2017-07-20 13:30:55.305000
Update Time : 2017-07-20 13:30:55.305000
Events # : 0
Events Start Time : N/A
Events End Time : N/A
Time Format : millis
Time Zone : Asia/Calcutta
Live Monitoring: OFF
Signals: signal1, Signal2, Signal3, Signal4
==================================================================================================================
falkonry>>
```

#### Delete Datastream by id
```
falkonry>> datastream_delete --id=oii0djojxc2lxt
Datastream successfully deleted : oii0djojxc2lxt
falkonry>>
```

#### Set default Datastream
You need to select default datastream for using features like adding data to datastream, adding entity meta to datastream and all assessment related features.
```
falkonry>> datastream_default_set --id=oii0djojxc2lxt
Default datastream set: oii0djojxc2lxt
falkonry>>
```

#### Get default Datastream
For fetching default datastream
```
falkonry>> datastream_default_get
Default datastream set : oii0djojxc2lxt Name : New Ds -1
falkonry>>
```

#### Add EntityMeta to a Datastream

Sample JSONFile :

```
[{"sourceId": "testId","label": "testName","path": "root/path"}]
```

Usage :
```
falkonry>> datastream_add_entity_meta --path=/Users/user/EntityMetaRequest.json
Entity Meta successfully added to datastream: oii0djojxc2lxt
falkonry>>
```

#### Get EntityMeta of a Datastream

Usage :
```
falkonry>> datastream_get_entity_meta
Entity Meta of datastream: oii0djojxc2lxt
Entity Label : testName. Entity Id : testId
falkonry>>
```

#### Add historical input data (json format) to a Datastream (Used for model revision)

Data :

```
{"time" :"2016-03-01 01:01:01", "tag" : "signal1_thing1", "value" : 3.4}
{"time" :"2016-03-01 01:01:01", "tag" : "signal2_thing1", "value" : 1.4}
{"time" :"2016-03-01 01:01:02", "tag" : "signal1_thing2", "value" : 9.3}
{"time" :"2016-03-01 01:01:02", "tag" : "signal2_thing2", "value" : 4.3}
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/Input.json
Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```

#### Add historical input data (csv format) to a Datastream (Used for model revision)
Data :

```
time, tag, value
2016-03-01 01:01:01, signal1_thing1, 3.4
2016-03-01 01:01:01, signal2_thing1, 1.4
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/Input.csv
Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```

#### Add live input data (json format) to a Datastream (Used for live monitoring)

Data :

```
{"time" :"2016-03-01 01:01:01", "tag" : "signal1_thing1", "value" : 3.4}
{"time" :"2016-03-01 01:01:01", "tag" : "signal2_thing1", "value" : 1.4}
{"time" :"2016-03-01 01:01:02", "tag" : "signal1_thing2", "value" : 9.3}
{"time" :"2016-03-01 01:01:02", "tag" : "signal2_thing2", "value" : 4.3}
```

Usage :

```
falkonry>> datastream_add_live_data --path=/Users/user/Input.json
Default datastream set : oii0djojxc2lxt Name : New Ds -1
Data submitted successfully
falkonry>>
```

#### Add live data (csv format) to a Datastream (Used for live monitoring)

Data :

```
time, tag, value
2016-03-01 01:01:01, signal1_thing1, 3.4
2016-03-01 01:01:01, signal2_thing1, 1.4
```

Usage :

```
falkonry>> datastream_add_live_data --path=/Users/user/Input.csv
Default datastream set : oii0djojxc2lxt Name
Data submitted successfully
falkonry>>
```

#### Create Assessment

Sample JSONFile:
```
{
"name":"Assessment Test -1",
"datastream":"oii0djojxc2lxt",
"rate": "PT0S"
}
```
Usage :

```
falkonry>> assessment_create --path=/Users/user/AssessmentRequest.json
Assessment successfully created : 2d6bh2xvjfcugp
falkonry>>
```

#### Retrieve Assessments

Usage :

```
falkonry>> assessment_get_list
Default datastream set : oii0djojxc2lxt Name : New DS -1
Fetching assessment list of datastream : oii0djojxc2lxt...
==================================================================================================================
Assessment Name Id Created By Live Status
==================================================================================================================
Assessment 123 2d6bh2xvjfcugp Tza1q4g0kw5epo OFF
Robo Arm Test 1 mhai7bxygkawq8 Tza1q4g0kw5epo OFF
==================================================================================================================
falkonry>>
```

#### Retrieve Assessment by Id

Usage :

```
falkonry>> assessment_get_by_id --id=2d6bh2xvjfcugp
==================================================================================================================
Id : 2d6bh2xvjfcugp
Name : Assessment 123
Created By : Tza1q4g0kw5epo
Create Time : 2017-07-20 14:01:50.362000
Update Time : 2017-07-20 14:01:50.362000
Datastream : 5kzugwm1natt0l
Live : OFF
Rate : PT0S
Condition List : N/A
==================================================================================================================
falkonry>>
```

#### Delete Assessment

Usage :

```
falkonry>> assessment_delete --id=2d6bh2xvjfcugp
Assessment deleted successfully: 2d6bh2xvjfcugp
falkonry>>
```

#### Set default Assessment
You need to select default assessment for using features like adding facts to assessment, retrieving output data.
```
falkonry>> assessment_default_set --id=mhai7bxygkawq8
Default datastream set: 5kzugwm1natt0l Name: Robo Arm Test 1
Default assessment set: mhai7bxygkawq8
falkonry>>
```

#### Get default Assessment
For fetching default assessment
```
falkonry>> assessment_default_get
Default assessment set : mhai7bxygkawq8 Name : Robo Arm Test 1
falkonry>>
```

#### Add facts data (json format) to Assessment

Sample JSONFile / Facts Data:
```
{"time":"2011-09-08T02:22:12.702+05:30","end":"2012-09-22T17:33:25.000+05:30","device":"Device1","Assessment1":"Fouling"}
{"time":"2012-09-22T17:33:25.000+05:30","end":"2013-09-07T00:26:03.108+05:30","device":"Device1","Assessment1":"Failure"}
{"time":"2011-01-02T02:53:00.000+05:30","end":"2011-09-08T02:22:12.702+05:30","device":"Device2","Assessment1":"Normal"}
{"time":"2013-09-07T00:26:03.108+05:30","end":"2014-04-07T06:38:39.189+05:30","device":"Device2","Assessment1":"Normal"}
{"time":"2011-01-02T02:53:00.000+05:30","end":"2011-09-08T02:22:12.702+05:30","device":"Device3","Assessment1":"Normal"}
{"time":"2013-09-07T00:26:03.108+05:30","end":"2014-04-07T06:38:39.189+05:30","device":"Device3","Assessment1":"Failure"}
```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/Facts.json
Default assessment set : mhai7bxygkawq8 Name : Robo Arm Test 1
{u'status': u'PENDING', u'datastream': u'5kzugwm1natt0l', u'__$createTime': 1500540954245, u'__$id': u'4v64vkyawmqmf74a', u'action': u'ADD_FACT_DATA', u'__$tenant': u'el7rvvqx2xr6v5', u'assessment': u'mhai7bxygkawq8'}
falkonry>>
```

#### Add facts data (csv format) to Assessment

Sample CSVFile / Facts Data:
```
"time","end","device","Assessment1"
1378493763108,1396832919189,"Device1","Normal"
1293916980000,1315428732702,"Device1","Normal"
1348315405000,1378493763108,"Device2","Failure"
1315428732702,1348315405000,"Device2","Fouling"
1348315405000,1378493763108,"Device3","Failure"
1315428732702,1348315405000,"Device3","Normal"
```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/Facts.csv
Default assessment set : mhai7bxygkawq8 Name : Robo Arm Test 1
{u'status': u'PENDING', u'datastream': u'5kzugwm1natt0l', u'__$createTime': 1500540954245, u'__$id': u'4v64vkyawmqmf74a', u'action': u'ADD_FACT_DATA', u'__$tenant': u'el7rvvqx2xr6v5', u'assessment': u'mhai7bxygkawq8'}
falkonry>>
```

#### Get Historian Output from Assessment (Generate output for given time range)
Options:
```
--path=PATH file path to write output
--trackerId=TRACKERID
tracker id of the previous output request
--modelIndex=MODELINDEX
index of the model of which output needs to be fetched
--startTime=STARTTIME
startTime of the output range
--endTime=ENDTIME endTime of the output range
--format=FORMAT format of the output. For csv pass text/csv. For JSON
output pass application/json
```
Usage:
1. Fetching data which is already processed
```
falkonry>> assessment_get_historical_output --startTime=2017-07-19T14:04:06+05:30 --format=text/csv
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
==================================================================================================================
time,entity,value
1500453246798,UNIT-1,unlabeled5
1500453251847,UNIT-1,unlabeled2
1500453256896,UNIT-1,unlabeled6
1500453261945,UNIT-1,unlabeled1
1500453266994,UNIT-1,unlabeled4
1500453272043,UNIT-1,unlabeled1
1500453277092,UNIT-1,unknown
1500453282141,UNIT-1,unlabeled1
1500453287190,UNIT-1,unlabeled1
1500453292239,UNIT-1,unknown
1500453297288,UNIT-1,unknown
1500453302337,UNIT-1,unknown
1500453307386,UNIT-1,unlabeled1

==================================================================================================================
falkonry>>
```
2. Fetching data which is not processed
```
If data is not readily available then, a tracker id will be sent with 202 status code. While falkonry will genrate ouptut data
Client should do timely pooling on the using same method, sending tracker id (__id) in the query params
Once data is available server will response with 200 status code and data in json/csv format.

falkonry>> assessment_get_historical_output --startTime=2016-07-19T14:04:06+05:30 --format=text/csv
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
{"status":"WAITING","assessment":"743cveg32hkwl2","datastream":"qh6rg4ce5g3p5j","outputSummary":"c8cr9bedv4y2jg","model":"r1ao169d3icdl3","pid":"A8vkl6bxn86qh0_umm1j0j08f1pbd","mode":"ANALYSIS","userEmail":"aniket.amrutkar@falkonry.com","userId":"c8s6wwrfczrwos","entities":null,"__$id":"nphnmcc81vqkgpvo","__$tenant":"A8vkl6bxn86qh0","__$createTime":1500544370048,"__id":"nphnmcc81vqkgpvo"}
Falkonry is generating your output. Please try following command in some time.
assessment_get_historical_output --trackerId=nphnmcc81vqkgpvo
falkonry>> assessment_get_historical_output --trackerId=nphnmcc81vqkgpvo --format=application/json
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
==================================================================================================================
{"time":1500453241749,"entity":"UNIT-1","value":"unlabeled3"}
{"time":1500453246798,"entity":"UNIT-1","value":"unlabeled5"}
{"time":1500453251847,"entity":"UNIT-1","value":"unlabeled2"}
{"time":1500453256896,"entity":"UNIT-1","value":"unlabeled6"}
{"time":1500453261945,"entity":"UNIT-1","value":"unlabeled1"}
{"time":1500453266994,"entity":"UNIT-1","value":"unlabeled4"}
{"time":1500453272043,"entity":"UNIT-1","value":"unlabeled1"}
{"time":1500453277092,"entity":"UNIT-1","value":"unknown"}
{"time":1500453282141,"entity":"UNIT-1","value":"unlabeled1"}
{"time":1500453287190,"entity":"UNIT-1","value":"unlabeled1"}
{"time":1500453292239,"entity":"UNIT-1","value":"unknown"}
{"time":1500453297288,"entity":"UNIT-1","value":"unknown"}
{"time":1500453302337,"entity":"UNIT-1","value":"unknown"}
{"time":1500453307386,"entity":"UNIT-1","value":"unlabeled1"}

==================================================================================================================
falkonry>>
```
3. Writing output Data to file
```
falkonry>> assessment_get_historical_output --trackerId=nphnmcc81vqkgpvo --format=application/json --path=/Users/user/Output.json
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
Output data is written to the file : /Users/user/Output.json
falkonry>>
```

#### Get Facts Data For Default Assessment
Options:
```
  -h, --help            show this help message and exit
  --path=PATH           file path to write output
  --modelIndex=MODELINDEX
                        index of the model of which facts needs to be fetched
  --startTime=STARTTIME
                        startTime of the facts range
  --endTime=ENDTIME     endTime of the facts range
  --format=FORMAT       format of the facts data. For csv pass text/csv. For
                        JSON output pass application/json
```
Usage:
1. Fetching facts data
```
falkonry>> assessment_get_facts --format=application/json --modelIndex=2
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
Facts Data : 
==================================================================================================================
{"id":"zjE7gRjij2aAtn","tenant":"A8vkl6bxn86qh0","createTime":1501756952620,"type":"entities.Verification","time":1472628618962,"end":1475258391805,"entity":"UNIT-1","value":"normal","assessment":"743cveg32hkwl2","tags":["USER ADDED","Test",""],"sysCreateTime":1501756952620,"falkonry_source":"1501756363467"}
{"id":"BdPJyBwtOia6y5","tenant":"A8vkl6bxn86qh0","createTime":1501757081175,"type":"entities.Verification","time":1475300807496,"end":1477972996029,"entity":"UNIT-1","value":"good","assessment":"743cveg32hkwl2","tags":["USER ADDED","GoodTag",""],"sysCreateTime":1501757081175,"falkonry_source":"1501756363467"}
{"id":"4Yx5vcg7qYa1W8","tenant":"A8vkl6bxn86qh0","createTime":1501757152737,"type":"entities.Verification","time":1477972996029,"end":1483147710332,"entity":"UNIT-1","value":"failure","assessment":"743cveg32hkwl2","tags":["USER ADDED","Failed",""],"sysCreateTime":1501757152737,"falkonry_source":"1501756363467"}
{"id":"NUR1dP3PGtI5nW","tenant":"A8vkl6bxn86qh0","createTime":1500546860111,"type":"entities.Verification","time":1500453248322,"end":1500453256182,"entity":"UNIT-1","value":"bad","assessment":"743cveg32hkwl2","tags":["USER ADDED"],"sysCreateTime":1500546860111,"falkonry_source":"1500546477175"}
{"id":"EmdxDwHrQd4X1v","tenant":"A8vkl6bxn86qh0","createTime":1500546642589,"type":"entities.Verification","time":1500453256182,"end":1500453256896,"entity":"UNIT-1","value":"new","assessment":"743cveg32hkwl2","tags":["USER ADDED"],"sysCreateTime":1500546642589,"falkonry_source":"1500546477175"}
{"id":"MBLD2yA0cSG2fM","tenant":"A8vkl6bxn86qh0","createTime":1500546681069,"type":"entities.Verification","time":1500453256896,"end":1500453261945,"entity":"UNIT-1","value":"normal","assessment":"743cveg32hkwl2","tags":["USER ADDED"],"sysCreateTime":1500546681069,"falkonry_source":"1500546477175"}
==================================================================================================================
falkonry>>
```

2. Writing facts Data to file
```
falkonry>> assessment_get_facts --format=application/json --modelIndex=2 --path=facts.json
Default assessment set : 743cveg32hkwl2 Name : Standalone DS
Facts data is written to the file : facts.json
falkonry>>
```

#### Get Datastream Data
Options:
```
  -h, --help            show this help message and exit
  --format=FORMAT       format of the facts data. For csv pass text/csv. For
                        JSON output pass application/json
```
Usage:
1. Fetching input data
```
falkonry>> datastream_get_data --format=application/json
Default datastream set : 1scyeeoxbdh7if Name : New Standalone
Input Data : 
==================================================================================================================
{"time":1294078560000,"tag":"Device1:device","value":"Device1"}
{"time":1294091820000,"tag":"Device1:device","value":"Device1"}
{"time":1294099380000,"tag":"Device1:device","value":"Device1"}
{"time":1294078560000,"tag":"Device2:device","value":"Device2"}
{"time":1294091820000,"tag":"Device2:device","value":"Device2"}
{"time":1294099380000,"tag":"Device2:device","value":"Device2"}
{"time":1294078560000,"tag":"Device3:device","value":"Device3"}
{"time":1294091820000,"tag":"Device3:device","value":"Device3"}
{"time":1294099380000,"tag":"Device3:device","value":"Device3"}
{"time":1294078560000,"tag":"Device1:device","value":"Device1"}
{"time":1294091820000,"tag":"Device1:device","value":"Device1"}
==================================================================================================================
falkonry>>
```

2. Writing input Data to file
```
falkonry>> datastream_get_data --format=application/json --path=input.json
Default datastream set : 1scyeeoxbdh7if Name : New Standalone
Input data is written to the file : input.json
falkonry>> 
```
#### Get Streaming output of Assessment
Fetch live output data
```
falkonry>>assessment_output_listen --format=application/json
Fetching live assessments :
{"time":1500453241749,"entity":"UNIT-1","value":"unlabeled3"}
{"time":1500453246798,"entity":"UNIT-1","value":"unlabeled5"}
```

#### Datastream On (Start live monitoring of datastream)
Usage:
```
falkonry>> datastream_start_live
Default datastream set: 5kzugwm1natt0l Name: Robo Arm Test 1
Turning on Live monitoring for datastream : 5kzugwm1natt0l
Datastream is ON for live monitoring
falkonry>>
```

#### Datastream Off (Stop live monitoring of datastream)
Usage:
```
falkonry>> datastream_stop_live
Default datastream set: 5kzugwm1natt0l Name : Robo Arm Test 1
Turning off Live monitoring for datastream : 5kzugwm1natt0l
Datastream is OFF for live monitoring
falkonry>>

```

## Docs

[Falkonry APIs](https://app.falkonry.ai/api)

## License

Available under [MIT License](LICENSE)
