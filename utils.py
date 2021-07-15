from pathlib import Path
import json
import streamlink

collection_folder = "data"

def get_path_to_file(filename) -> str :
    folder = Path(collection_folder)
    file = folder / filename

    path = str(file.resolve())

    return path

def load_json(filename) -> dict :
    path = get_path_to_file(filename)

    json_file = open(path)
    json_data = json_file.read()
    json_file.close()
    
    return json.loads(json_data)

def get_collection_folder_content() -> list:
    folder = Path(collection_folder)

    folder_content = [item.name for item in folder.iterdir()]

    return folder_content

def get_collection_folder_files() -> list:
    folder = Path(collection_folder)
    folder_content = get_collection_folder_content()

    paths = [folder / name for name in folder_content]

    folder_files = [file for file,path in zip(folder_content,paths)
                    if path.is_file()]

    return folder_files


def get_collection_folder_jsons() -> list :
    folder_files = get_collection_folder_files()

    folder_jsons = [file for file in folder_files if is_valid_json(file)]

    return folder_jsons

def is_valid_json(filename) -> bool :
    try:
        load_json(filename)
    except:
        return False
    return True

def is_stream_offline(stream_url) -> bool :
    try:
        streams = streamlink.streams(stream_url)
        assert(streams["best"].url != "")
    except:
        return True
    return False

def get_offline_streams(filename) -> list :
    offline_streams = []
    json_dict = load_json(filename)

    for key,value in json_dict.items():
        stream_url = value["stream_url"]
        if is_stream_offline(stream_url):
            offline_streams.append("Stream: " + '"' + key + '"'
                                   + " on file: " + '"' + filename + '"'
                                   + " is offline.")

    return offline_streams

def get_all_offline_streams() -> list :
    # WARNING: It takes a long time to complete.
    # Make sure to update Streamlink before using this function
    # so you don't waste your time with a wrong output.
    offline_streams = []

    folder_jsons = get_collection_folder_jsons()

    for file in folder_jsons:
        offline_streams.extend(get_offline_streams(file))

    return offline_streams

def get_all_invalid_jsons() -> list:
    invalid_jsons = []

    folder_files = get_collection_folder_files()

    for file in folder_files:
        if not is_valid_json(file):
            invalid_jsons.append(file + " is an invalid json.")
    return invalid_jsons

    
            
