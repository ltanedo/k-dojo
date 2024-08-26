import requests

API_KEY = "0a9f88c6622e5f95e4f39512e21003aab4669bb8"

# API_KEY = "b310a289ea96048ebcea31bf68b56d3dbc501b6f"
# token b310a289ea96048ebcea31bf68b56d3dbc501b6f

resp = requests.post("https://api.deepgram.com/v1/listen?smart_format=true&language=zh-CN&model=base",
    headers={
        "authorization":  f"Token {API_KEY}",
        # "content-Type": "application/json",
        "Content-Type": "audio/*"
    },
    # json = {
    #     "url":"https://chinese.voiceoversamples.com/CHI_MAN_F_MaYue.mp3"
    # },
    data=open(r'samples/chinese.mp3', 'rb')
)

print(resp.json())