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
* Supported Python: Python 3.6 or higher
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
* Add historical narrow input data (json format) to multi entity Datastream
* Add historical narrow input data (csv format) single entity to Datastream
* Add historical wide input data (json format) to single entity Datastream
* Add historical wide input data (csv format) to multi entity Datastream
* Add historical narrow input data to single entity batch datastream
* Add historical narrow input data to multi entity batch datastream
* Add historical wide input data to single entity batch datastream
* Add historical wide input data to multi entity batch datastream
* Add live input data (json format) to a Datastream (Used for live monitoring)
* Add live input data (csv format) to a Datastream (Used for live monitoring)
* Create Assessment
* Retrieve Assessments
* Retrieve Assessment by Id
* Delete Assessment
* Set default Assessment
* Get default Assessment
* Get Condition List Of Assessment
* Add facts data (json format) to Assessment of single entity datastream
* Add facts data (json format) with addition tag to Assessment of multi entity datastream
* Add facts data (csv format) to Assessment of single entity datastream
* Add facts data (csv format) with tags Assessment of single entity datastream
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
falkonry>> datastream_create --path=/Users/user/NarrowSingleEntity.json
Datastream successfully created : anbsivd1h7h1sd
falkonry>>
```

#### Create Datastream for narrow/historian style data from multiple entity

Data :

```
{"time" :"2016-03-01 01:01:01", "signal" : "signal1", "entity" : "entity1", "value" : 3.4}
{"time" :"2016-03-01 01:01:02", "signal" : "signal2", "entity" : "entity2", "value" : 1.4}
{"time" :"2016-03-01 01:01:03", "signal" : "signal3", "entity" : "entity3", "value" : 9.3}
{"time" :"2016-03-01 01:01:04", "signal" : "signal2", "entity" : "entity2", "value" : 4.3}

or

time,signal,entity,value
2016-03-01 01:01:01,signal1,entity1,3.4
2016-03-01 01:01:01,signal2,entity2,1.4
2016-03-01 01:01:01,signal3,entity3,9.3
2016-03-01 01:01:01,signal4,entity4,4.3
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
"entityIdentifier": "entity"
"signal": {
"valueIdentifier": "value",
"signalIdentifier": "signal"
}
}
}
```

Usage :
```
falkonry>> datastream_create --path=/Users/user/NarrowMultipleEntity.json
Datastream successfully created : anbsivd1h7h1sd
falkonry>>
```

#### Create Datastream for wide style data from a single entity

Data :

```
{"time":1467729675422, "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
{"time":1467729668919, "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

or

time,signal1,signal2,signal3,signal4
1467729675422,41.11,62.34,77.63,4.8
1467729675445,43.91,82.64,73.63,3.8
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
falkonry>> datastream_create --path=/Users/user/WideSingleEntity.json
Datastream successfully created : anb109d1h7h1po
falkonry>>
```

#### Create Datastream for wide style data from multiple entities

Data :

```python
{"time":1467729675422, "entity": "entity1", "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
{"time":1467729668919, "entity": "entity2", "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

or

time, entity, signal1, signal2, signal3, signal4
1467729675422, entity1, 41.11, 62.34, 77.63, 4.8
1467729675445, entity1, 43.91, 82.64, 73.63, 3.8
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
"entityIdentifier": "entity"
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
falkonry>> datastream_create --path=/Users/user/WideMultiEntity.json
Datastream successfully created : anb109d1h7h1po
falkonry>>
```

#### Create Datastream with microseconds precision

Data :

```
{"time" :"2016-03-01 01:01:01", "signal" : "signal1", "value" : 3.4}
{"time" :"2016-03-01 01:01:02", "signal" : "signal2", "value" : 9.3}

or

time,signal,value
2016-03-01 01:01:01,signal1,3.4
2016-03-01 01:01:02,signal2,9.3

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
"signalIdentifier": "signal",
"valueIdentifier": "value"
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

#### Create Datastream for batched usecase

Data :

```
{"time" :"2016-03-01 01:01:01", "signal" : "signal1", "value" : 3.4, "batchId": "batch-1"}
{"time" :"2016-03-01 01:01:02", "signal" : "signal2", "value" : 9.3, "batchId": "batch-1"}

or

time,signal,value,batchId
2016-03-01 01:01:01,signal1,3.4,batch-1
2016-03-01 01:01:02,signal2,9.3,batch-1

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
"signalIdentifier": "signal",
"valueIdentifier": "value"
},
"batchIdentifier": "batchId" // set batch identifier here.
}
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

#### Add historical narrow input data (json format) to multi entity Datastream

Data :

```
{"time":"2016-03-01T01:01:01.000Z","signal":"current","value":12.4,"car":"car1"}
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/Input.json --timeIdentifier=time --entityIdentifier=car --timeFormat=iso_8601 --timeZone=GMT --signalIdentifier=signal --valueIdentifier=value

Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```

#### Add historical narrow input data (csv format) single entity to Datastream
Data :

```
time,signal,value
2011-01-03T18:16:00.000Z,current,32.96
2011-01-03T21:57:00.000Z,vibration,3.4

```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputNarrow.csv --timeIdentifier=time --timeFormat=iso_8601 --timeZone=GMT --signalIdentifier=signal --valueIdentifier=value

Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```


#### Add historical wide input data (json format) to single entity Datastream

Data :

```
{"time":"2011-01-03T18:16:00.000Z","Signal1":9.95,"Signal2":30.6,"Signal3":41.7}
{"time":"2011-01-04T18:16:00.000Z","Signal1":19.95,"Signal2":40.6,"Signal3":43.7}

```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputNarrow.csv --timeIdentifier=time --timeFormat=iso_8601 --timeZone=GMT --signalIdentifier=signal --valueIdentifier=value

Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```


#### Add historical wide input data (csv format) to multi entity Datastream

Data :

```
time,device,Signal1,Signal2,Signal3
2011-01-03T18:16:00.000Z,Device1,9.95,32.96,42.91
2011-01-03T21:57:00,000Z,Device1,9.95,32.96,42.91

```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputNarrow.csv --timeIdentifier=time --timeFormat=iso_8601 --timeZone=GMT --signalIdentifier=signal --valueIdentifier=value --entityIdentifier=device

Default datastream set : oii0djojxc2lxt Name : New Ds -1
{u'status': u'PENDING', u'datastream': u'oii0djojxc2lxt', u'__$createTime': 1500538975912, u'__$id': u'q68cho8foyml3gv4', u'user': u'Tza1q4g0kw5epo', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'el7rvvqx2xr6v5', u'dataSource': u'Lp1nfea7z5lrtk'}
falkonry>>
```


#### Add historical narrow input data (json format) to single entity batch Datastream

Data :

```
{"time": 1467729675010,"batchId": "batch_1","signal": "signal1","value": 9.95}
{"time": 1467729675020,"batchId": "batch_1","signal": "signal1","value": 4.45}
{"time": 1467729675030,"batchId": "batch_2","signal": "signal1","value": 1.45}
{"time": 1467729675040,"batchId": "batch_2","signal": "signal1","value": 8.45}
{"time": 1467729675050,"batchId": "batch_2","signal": "signal1","value": 2.45}
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputNarrowBatchSingleEntity.json --timeIdentifier="time" --timeFormat="Unix Time Milliseconds" --timeZone="GMT" --signalIdentifier="signal" --batchIdentifier="batchId" --valueIdentifier="value"
Default datastream set : wlybjb4tq776n9 Name : Narrow Single Entity Batch Test DS
{u'status': u'PENDING', u'datastream': u'wlybjb4tq776n9', u'__$createTime': 1516013313895, u'__$id': u'kpgly6d2tg9v27b6', u'user': u'e6q8ienqs9celz', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'iqn80x6e2ku9id', u'dataSource': u'y8ibr9co7hqkkd'}
falkonry>>
```


#### Add historical narrow input data (csv format) to multi entity batch Datastream

Data :

```
time,batchId,unit,signal,value
1467729675010,batch_1,unit1,signal1,9.95
1467729675020,batch_1,unit1,signal1,4.45
1467729675030,batch_2,unit1,signal1,1.45
1467729675040,batch_2,unit1,signal1,8.45
1467729675050,batch_2,unit1,signal1,2.45
1467729675010,batch_1,unit1,signal2,19.95
1467729675020,batch_1,unit1,signal2,14.45
1467729675030,batch_2,unit1,signal2,10.45
1467729675040,batch_2,unit1,signal2,18.45
1467729675050,batch_2,unit1,signal2,12.45
1467729675010,batch_1,unit1,signal3,39.95
1467729675020,batch_1,unit1,signal3,34.45
1467729675030,batch_2,unit1,signal3,30.45
1467729675040,batch_2,unit1,signal3,38.45
1467729675050,batch_2,unit1,signal3,32.45
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputNarrowBatchMultiEntity.csv --timeIdentifier="time" --timeFormat="Unix Time Milliseconds" --timeZone="GMT" --entityIdentifier="unit" --signalIdentifier="signal" --batchIdentifier="batchId" --valueIdentifier="value"
Default datastream set : hn6cq2lpcwg49c Name : Narrow Multiple Entity Batch Test DS
{u'status': u'PENDING', u'datastream': u'hn6cq2lpcwg49c', u'__$createTime': 1516013971506, u'__$id': u'4hqpj9hw2vmcjqwh', u'user': u'e6q8ienqs9celz', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'iqn80x6e2ku9id', u'dataSource': u'Rp8euhiyg3ctt4'}
falkonry>> 

```


#### Add historical wide input data (json format) to single entity Datastream

Data :

```
{"time": 1467729675010,"batchId": "batch_1","signal1": 9.95,"signal2": 19.95,"signal3": 39.95}
{"time": 1467729675020,"batchId": "batch_1","signal1": 4.45,"signal2": 14.45,"signal3": 34.45}
{"time": 1467729675030,"batchId": "batch_2","signal1": 1.45,"signal2": 10.45,"signal3": 30.45}
{"time": 1467729675040,"batchId": "batch_2","signal1": 8.45,"signal2": 18.45,"signal3": 38.45}
{"time": 1467729675050,"batchId": "batch_2","signal1": 2.45,"signal2": 12.45,"signal3": 32.45}
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputWideBatchSingleEntity.json --timeIdentifier="time" --timeFormat="Unix Time Milliseconds" --timeZone="GMT" --batchIdentifier="batchId"
Default datastream set : cm492hm4j74wrn Name : Wide Single Entity Batch Test DS
{u'status': u'PENDING', u'datastream': u'cm492hm4j74wrn', u'__$createTime': 1516015544894, u'__$id': u'wmgllwgjwwjtp7w4', u'user': u'e6q8ienqs9celz', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'iqn80x6e2ku9id', u'dataSource': u'Teqm2nwjpbhbs3'}
falkonry>> 
```


#### Add historical wide input data (csv format) to multi entity Datastream

Data :

```
time,batchId,unit,signal1,signal2,signal3
1467729675010,batch_1,unit1,9.95,19.95,39.95
1467729675020,batch_1,unit1,4.45,14.45,34.45
1467729675030,batch_2,unit1,1.45,10.45,30.45
1467729675040,batch_2,unit1,8.45,18.45,38.45
1467729675050,batch_2,unit1,2.45,12.45,32.45
```

Usage :

```
falkonry>> datastream_add_historical_data --path=/Users/user/InputWideBatchMultiEntity.csv --timeIdentifier="time" --timeFormat="Unix Time Milliseconds" --timeZone="GMT" --entityIdentifier="unit" --batchIdentifier="batchId"
Default datastream set : 7wgwm68b9p24n4 Name : Wide Multiple Entity Batch Test DS
{u'status': u'PENDING', u'datastream': u'7wgwm68b9p24n4', u'__$createTime': 1516016064677, u'__$id': u'mlc2pt7y87jhwlw2', u'user': u'e6q8ienqs9celz', u'action': u'ADD_DATA_DATASTREAM', u'__$tenant': u'iqn80x6e2ku9id', u'dataSource': u'Lita7m408qq9j9'}
falkonry>>
```


#### Add live input data (json format) to a Datastream (Used for live monitoring)

Data :

```
time,activity,person,end
1447882550000,walking,p1,1447882565000
1447882565000,sitting,p1,1447882570000
1447882575000,cycling,p1,1447882580000
1447882580000,sitting,p1,1447882585000
1447882590000,sitting,p1,1447882595000
1447882595000,walking,p1,1447882600000
1447882600000,cycling,p1,1447882605000
1447882625000,rowing,p1,1447882630000
1447882630000,rowing,p1,1447882635000
1447882635000,sitting,p1,1447882640000
1447882660000,rowing,p1,1447882665000
1447882665000,cycling,p1,1447882670000
```

Usage :

```
datastream_add_live_data --path=/Users/user/Input.json
Default datastream set : lg7k1a5jor1nvh Name : Human Activity
{u'message': u'Data submitted successfully'}
```

#### Add live input data (csv format) to a Datastream (Used for live monitoring)

Data :

```
{"time":"1447882550000","activity":"walking","person":"p1","end":"1447882565000"}
{"time":"1447882565000","activity":"sitting","person":"p1","end":"1447882570000"}
{"time":"1447882575000","activity":"cycling","person":"p1","end":"1447882580000"}
{"time":"1447882580000","activity":"sitting","person":"p1","end":"1447882585000"}
{"time":"1447882590000","activity":"sitting","person":"p1","end":"1447882595000"}
{"time":"1447882595000","activity":"walking","person":"p1","end":"1447882600000"}
{"time":"1447882600000","activity":"cycling","person":"p1","end":"1447882605000"}
{"time":"1447882625000","activity":"rowing","person":"p1","end":"1447882630000"}
{"time":"1447882630000","activity":"rowing","person":"p1","end":"1447882635000"}
{"time":"1447882635000","activity":"sitting","person":"p1","end":"1447882640000"}
{"time":"1447882660000","activity":"rowing","person":"p1","end":"1447882665000"}
{"time":"1447882665000","activity":"cycling","person":"p1","end":"1447882670000"}
```

Usage :

```
datastream_add_live_data --path=/Users/user/Input.csv
Default datastream set : lg7k1a5jor1nvh Name : Human Activity
{u'message': u'Data submitted successfully'}
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

#### Add facts data (json format) to Assessment of single entity datastream

Sample JSONFile / Facts Data:
```
{"time":1456774261072,"end":1456774261116,"value":"label1"}
{"time":1456774261321,"end":1456774261362,"value":"label2"}
{"time":1456774261538,"end":1456774261570,"value":"label1"}
{"time":1456774261723,"end":1456774261754,"value":"label2"}
```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/NarrowFacts.json --startTimeIdentifier=time --endTimeIdentifier=end --timeFormat=millis --timeZone=GMT --valueIdentifier=value
Default assessment set : hv987ptckdc6n7 Name : New Test Assessment
{u'status': u'PENDING', u'datastream': u'cr77vk6mkwqwqq', u'__$createTime': 1516022010240, u'__$id': u'lcq4pp9jcvwgcgmp', u'action': u'ADD_FACT_DATA', u'__$tenant': u'iqn80x6e2ku9id', u'assessment': u'hv987ptckdc6n7'}
falkonry>> 

```

#### Add facts data (json format) with addition tag to Assessment of multi entity datastream

Sample JSONFile / Facts Data:
```
{"time":1456774261061,"end":1456774261103,"value":"label1"}
{"time":1456774261213,"end":1456774261258,"value":"label2"}
{"time":1456774261455,"end":1456774261512,"value":"label1"}
{"time":1456774261715,"end":1456774261767,"value":"label2"}
```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/MoreFacts.json --startTimeIdentifier=time --endTimeIdentifier=end --timeFormat=millis --timeZone=GMT --valueIdentifier=value --additionalTag=testTag
Default assessment set : hv987ptckdc6n7 Name : New Test Assessment
{u'status': u'PENDING', u'datastream': u'cr77vk6mkwqwqq', u'__$createTime': 1516087411723, u'__$id': u'4l8bgmd6rv2qj77j', u'action': u'ADD_FACT_DATA', u'__$tenant': u'iqn80x6e2ku9id', u'assessment': u'hv987ptckdc6n7'}
falkonry>>

```


#### Add facts data (csv format) to Assessment of single entity datastream

Sample CSVFile / Facts Data:
```
time,end,value
"1456774261072","1456774261116","label1"
"1456774261321","1456774261362","label2"
"1456774261538","1456774261570","label1"
"1456774261723","1456774261754","label2"

```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/NarrowFacts.csv --startTimeIdentifier=time --endTimeIdentifier=end --timeFormat=millis --timeZone=GMT --valueIdentifier=value
Default assessment set : bqn8vjdb7yr9km Name : new test
{u'status': u'PENDING', u'datastream': u'cr77vk6mkwqwqq', u'__$createTime': 1516089750789, u'__$id': u'm7b2l694wcptccmk', u'action': u'ADD_FACT_DATA', u'__$tenant': u'iqn80x6e2ku9id', u'assessment': u'bqn8vjdb7yr9km'}
falkonry>>
```

#### Add facts data (csv format) with tags Assessment of single entity datastream

Sample CSVFile / Facts Data:
```
time,end,value,tagId
"1456774261072","1456774261116","label1","tag1"
"1456774261321","1456774261362","label2","tag1"
"1456774261538","1456774261570","label1","tag2"
"1456774261723","1456774261754","label2","tag2"
```
Usage:

```
falkonry>> assessment_add_facts --path=/Users/user/TagFacts.csv --startTimeIdentifier=time --endTimeIdentifier=end --timeFormat=millis --timeZone=GMT --valueIdentifier=value --tagIdentifier=tagId
Default assessment set : 4rrp97lk9gcvwc Name : test new
{u'status': u'PENDING', u'datastream': u'cr77vk6mkwqwqq', u'__$createTime': 1516090649022, u'__$id': u'hly8b4727wm9prq8', u'action': u'ADD_FACT_DATA', u'__$tenant': u'iqn80x6e2ku9id', u'assessment': u'4rrp97lk9gcvwc'}
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
Default assessment set : 424ltd4jphnm69 Name : Sports Activity
Facts Data : 
==================================================================================================================
{"time":1447882550000000,"end":1447882565000000,"entity":"p1","value":"walking"}
{"time":1447882565000000,"end":1447882570000000,"entity":"p1","value":"sitting"}
{"time":1447882575000000,"end":1447882580000000,"entity":"p1","value":"cycling"}
{"time":1447882580000000,"end":1447882585000000,"entity":"p1","value":"sitting"}
{"time":1447882590000000,"end":1447882595000000,"entity":"p1","value":"sitting"}
{"time":1447882595000000,"end":1447882600000000,"entity":"p1","value":"walking"}
{"time":1447882600000000,"end":1447882605000000,"entity":"p1","value":"cycling"}
{"time":1447882625000000,"end":1447882635000000,"entity":"p1","value":"rowing"}
{"time":1447882635000000,"end":1447882640000000,"entity":"p1","value":"sitting"}
{"time":1447882660000000,"end":1447882665000000,"entity":"p1","value":"rowing"}
{"time":1447882665000000,"end":1447882670000000,"entity":"p1","value":"cycling"}
{"time":1447882670000000,"end":1447882675000000,"entity":"p1","value":"rowing"}
{"time":1447882675000000,"end":1447882680000000,"entity":"p1","value":"sitting"}
{"time":1447882680000000,"end":1447882685000000,"entity":"p1","value":"rowing"}
{"time":1447882685000000,"end":1447882690000000,"entity":"p1","value":"walking"}
{"time":1447882695000000,"end":1447882700000000,"entity":"p1","value":"cycling"}
{"time":1447882700000000,"end":1447882705000000,"entity":"p1","value":"sitting"}
{"time":1447882715000000,"end":1447882720000000,"entity":"p1","value":"cycling"}
{"time":1447882720000000,"end":1447882725000000,"entity":"p1","value":"walking"}
{"time":1447882725000000,"end":1447882730000000,"entity":"p1","value":"rowing"}
{"time":1447882750000000,"end":1447882755000000,"entity":"p1","value":"walking"}
{"time":1447882770000000,"end":1447882775000000,"entity":"p1","value":"rowing"}
{"time":1447882775000000,"end":1447882785000000,"entity":"p1","value":"cycling"}
{"time":1447882795000000,"end":1447882800000000,"entity":"p1","value":"rowing"}
{"time":1447882800000000,"end":1447882805000000,"entity":"p1","value":"cycling"}
{"time":1447882805000000,"end":1447882810000000,"entity":"p1","value":"rowing"}
{"time":1447882820000000,"end":1447882825000000,"entity":"p1","value":"rowing"}
{"time":1447882830000000,"end":1447882835000000,"entity":"p1","value":"cycling"}
{"time":1447882835000000,"end":1447882840000000,"entity":"p1","value":"sitting"}
{"time":1447882840000000,"end":1447882845000000,"entity":"p1","value":"walking"}

==================================================================================================================
falkonry>>
```

2. Writing facts Data to file
```
falkonry>> assessment_get_facts --format=application/json --modelIndex=2 --path=facts.json
Default assessment set : 424ltd4jphnm69 Name : Sports Activity
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
