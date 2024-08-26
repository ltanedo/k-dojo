import requests
import time

"""
curl -X POST https://api.salad.com/api/public/organizations/{my-organization}/inference-endpoints/transcribe/jobs \
   -H "Salad-Api-Key: {your-api-key}" \
   -H "Content-Type: application/json" \
   -d '{
      "input": {
         "url": "https://example.com/path/to/file.mp3",
         "language_code": "en",
         "sentence_level_timestamps": "true"
         "word_level_timestamps": false,
         "diarization": false,
         "srt": false,
         "translate": "to_eng"
      },
    "webhook": {your webhook url},
	  "metadata": {
      "my-job-id": 1234
      }
   }'
"""
API_SALAD_KEY = "salad_cloud_user_xjT4mymxibZwH1OMjEIU66Sa5yFah78U4L2sBMBfK7S1lbDCS"
resp = requests.post("https://api.salad.com/api/public/organizations/speech-dojo/inference-endpoints/transcribe/jobs",
    headers={
        "Salad-Api-Key": API_SALAD_KEY,
        # "Content-Type": "application/json",
        "Content-Type": "audio/*"
    },
    json={
        "input" : {
            "url": "https://chinese.voiceoversamples.com/CHI_MAN_F_MaYue.mp3",
            "language_code": "zh",
            # "sentence_level_timestamps": "true",
            # "word_level_timestamps": False,
            # "diarization": False,
            # "srt": False,
            "translate": "to_eng"
        },
    }
    
)
job = resp.json()
job_id = job["id"]

time.sleep(10)

resp = requests.get(f"https://api.salad.com/api/public/organizations/speech-dojo/inference-endpoints/transcribe/jobs/{job_id}",
    headers={
        "Salad-Api-Key": API_SALAD_KEY,
    },
)
print(resp.json())