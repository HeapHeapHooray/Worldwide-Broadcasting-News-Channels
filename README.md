# Worldwide-Broadcasting-News-Channels
## What it is
A collection of Worldwide Broadcasting Channels with stream urls that can be used with the [Streamlink API](https://github.com/streamlink/streamlink), and an utility script to manage the collection.
## How the collection is organized
The collection is composed of JSONs organized by country, the JSONs are dictionaries where the keys are the channel names and the values are the data. The data is a dictionary and has the following structure:
Property Name | Property Value
---|---
channel_name | The name of the channel.
source_url | The source page of the channel.
stream_url | The url of the stream.
## Requirements / Dependencies
The utility script requires **Python 3.4 or higher** and the Streamlink API that can be obtained with the following pip command:
```
pip3 install streamlink
```
you can also check the [Streamlink's PyPI webpage](https://pypi.org/project/streamlink/).
## Example of usage
Accessing the data of a channel and using the Streamlink API on the stream url can be done the following way using Python:
```python
from pathlib import Path
import json
import streamlink

file_path = Path("data/Japan.json")
file = open(file_path)
json_data = file.read()
file.close()

channels_dict = json.loads(json_data)
channel = channels_dict["ANN News"]

print("Channel's Name:",channel["channel_name"])
print("Source Page:",channel["source_url"])
print("Stream URL:",channel["stream_url"])

best_url = streamlink.streams(channel["stream_url"])["best"].url

print("Best Extracted URL:",best_url)
```
## About offline streams
You may find some streams that are offline, keep in mind that it doesn't means a stream is dead, the stream may be temporarily offline.
## Sources
The collection is extracted from the following sources:
wwitv.com
freeintertv.com
