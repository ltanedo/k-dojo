import requests
import json
import time

api_key    = "cd4f5e5b-0cc9-4637-85af-618906bd648f"
audio_file = "samples/chinese_short.mp3"


# curl --request POST \
#   --url https://api.gladia.io/v2/upload \
#   --header 'Content-Type: multipart/form-data' \
#   --header 'x-gladia-key: cd4f5e5b-0cc9-4637-85af-618906bd648f' \
#   --form audio=@samples/chinese.mp3
response = requests.post("https://api.gladia.io/v2/upload", 
    headers={ "x-gladia-key": f"{api_key}" }, 
    files={
        "audio": ("chinese.mp3", open(audio_file, "rb"), "audio/mpeg"),
    }
)

# print(json.dumps(response.json(), indent=2))
"""
{"audio_url":"https://api.gladia.io/file/f7d9f805-1c8a-415a-ba07-68e59bcf069c","audio_metadata":{"id":"f7d9f805-1c8a-415a-ba07-68e59bcf069c","filename":"chinese.mp3","extension":"mp3","size":318485,"audio_duration":19.905313,"number_of_channels":1}}
"""

# curl --request POST \
# --url https://api.gladia.io/v2/transcription \
# --header 'Content-Type: application/json' \
# --header 'x-gladia-key: cd4f5e5b-0cc9-4637-85af-618906bd648f' \
# --data '{ "audio_url": "https://api.gladia.io/file/f7d9f805-1c8a-415a-ba07-68e59bcf069c" }'
audio_url = response.json()["audio_url"]
response = requests.post("https://api.gladia.io/v2/transcription", 
    headers={ 
        "x-gladia-key": f"{api_key}",
        'Content-Type': 'application/json'
    }, 
    json={
        "audio_url": audio_url,
        "language": "zh",
    }
)

# print(json.dumps(response.json(), indent=2))
"""
{"id":"4ae16cd5-a9f5-4a8d-9761-dc92b552ce95","result_url":"https://api.gladia.io/v2/transcription/4ae16cd5-a9f5-4a8d-9761-dc92b552ce95"}
"""


result_url = response.json()["result_url"]
while True:
    response = requests.get(result_url,
        headers={
            'x-gladia-key': f"{api_key}"
        }
    )

    if response.json()["status"] in ["processing","queued"]:
        print(response.json()["status"])
    else: 
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        break

    time.sleep(1)

