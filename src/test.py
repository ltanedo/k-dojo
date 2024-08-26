import requests
import json
import time
from random import randrange

API_URL = "https://www2.deepl.com/jsonrpc"


def generate_timestamp(sentence):
    now = int(time.time() * 1000)
    i_count = 1
    i_count += sentence.count("i")

    # print("now", now)
    # print("i_count", i_count)
    # print("now % i_count", now % i_count)
    # print(now + (i_count - now % i_count))

    try:
        return now + (i_count - now % i_count)
    except ZeroDivisionError:
        return now


def generate_id():
    return randrange(1_000_000, 100_000_000)


headers = {
    "accept": "*/*",
    "accept-language": "en-US;q=0.8,en;q=0.7",
    "authority": "www2.deepl.com",
    "content-type": "application/json",
    "origin": "https://www.deepl.com",
    "referer": "https://www.deepl.com/translator",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    # "user-agent": ("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
    #                "AppleWebKit/537.36 (KHTML, like Gecko) "
    #                "Chrome/83.0.4103.97 Mobile Safari/537.36"),
}

id = generate_id()


def translate(sentance, source_lang_computed="auto", target_lang="EN"):
    # id = generate_id() # 44670072
    ts = generate_timestamp(sentance)
    resp = requests.post(
        "https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs",
        headers=headers,
        data=json.dumps({
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [{
                    "kind":
                    "default",
                    "sentences": [{
                        "text": sentance,
                        "id": 1,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [],
                    "raw_en_context_after": [],
                    "preferred_num_beams":
                    1
                }],
                "lang": {
                    "target_lang": target_lang,
                    "preference": {
                        "weight": {},
                        "default": "default"
                    },
                    "source_lang_computed": source_lang_computed
                },
                "quality":
                "normal",
                "regionalVariant":
                "zh-Hans",
                "mode":
                "translate",
                "priority":
                1,
                "timestamp":
                ts
            },
            "id": id
        }))
    print(resp.status_code)
    print(resp.json())
    return resp.json()




for i in range(60):

    sentance = """
    Translate up to 1,500 characters
    """

    print("\n\n", i)
    translate(sentance, source_lang_computed="auto", target_lang="ZH")

    # time.sleep(2)
