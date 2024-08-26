# import requests

# API_KEY="bJ0Y18hAWlh7fkdxz4NQHfpkqX55uMDk"
# PATH_TO_FILE="src/chinese.mp3"

# resp = requests.post("https://asr.api.speechmatics.com/v2/jobs/",
#     headers={
#         "Authorization": f"Bearer ${API_KEY}",
#         "data_file":f"@${PATH_TO_FILE}",
#         "config": '{"type": "transcription","transcription_config": { "operating_point":"enhanced", "language": "cmm" }}'
#     }
# )

# print(resp.text)

import requests
import json
import time

# Set your API key and file path
api_key = "bJ0Y18hAWlh7fkdxz4NQHfpkqX55uMDk"
file_path = "src/chinese_short.mp3"

# Set the API endpoint and headers
url = "https://asr.api.speechmatics.com/v2/jobs/"
headers = {
    "Authorization": f"Bearer {api_key}",
    # "Content-Type": "multipart/form-data; boundary=---------------------------374202262145210062887129654"
}

# Set the transcription configuration
config = {
    "type": "transcription",
    "transcription_config": {
        "operating_point": "enhanced",
        "language": "cmn"
    }
}

# Open the file in binary mode
response = requests.post(url, 
headers=headers, 
files={"data_file": open(r'src/chinese.mp3', 'rb')}, 
data={"config": json.dumps(config)})

# Check if the request was successful
if response.status_code == 201:
    print("Transcription job created successfully!")
    print(response.json())
else:
    print("Error creating transcription job:")
    print(response.text)

# {'id': 'zy2ekq0rlb'}
# job_id = "yzxcwqfx1c"
job_id = response.json()['id']

time.sleep(30)

# Set the API endpoint and headers
url = f"https://asr.api.speechmatics.com/v2/jobs/{job_id}/transcript"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Transcript retrieved successfully!")
    print(response.text)
else:
    print("Error retrieving transcript:")
    print(response.text)