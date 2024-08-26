import pandas
import polars
import requests
import json

import datetime as dt
import time
from random import randrange

API_URL = "https://www2.deepl.com/jsonrpc"

def calculate_valid_timestamp(timestamp, i_count):
    try:
        return timestamp + (i_count - timestamp % i_count)
    except ZeroDivisionError:
        return timestamp

def generate_timestamp(sentences):
    now = int(time.time() * 1000)
    i_count = 1
    for sentence in sentences:
        i_count += sentence.count("i")
        print('sentence.count("i")',sentence.count("i"))

    print("now", now)
    print("i_count", i_count)
    print("now % i_count", now % i_count)
    print(now + (i_count - now % i_count))

    return calculate_valid_timestamp(now, i_count)


def generate_id():
    return randrange(1_000_000, 100_000_000)


# headers = {
#     "accept": "*/*",
#     "accept-language": "en-US;q=0.8,en;q=0.7",
#     "authority": "www2.deepl.com",
#     "content-type": "application/json",
#     "origin": "https://www.deepl.com",
#     "referer": "https://www.deepl.com/translator",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": (
#         "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/83.0.4103.97 Mobile Safari/537.36"
#     ),
# }

headers = {
    'accept': '*/*' ,
    'accept-encoding': 'gzip, deflate, br, zstd' ,
    'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'content-length': '517',
    'content-type': 'application/json',
    'cookie': 'INGRESSCOOKIE=f4d08450b06158746f113f8935e6ca09|a6d4ac311669391fc997a6a267dc91c0; userCountry=US; dapUid=901238e2-9200-41d6-94b0-09de4efcdf58; releaseGroups=3613.WDW-267.2.2_10449.DF-3959.2.2_12074.DEM-1270.2.1_13287.AAEXP-11439.1.1_9824.AP-523.2.3_12316.DM-1846.1.1_12749.TACO-233.2.2_13380.DM-1417.1.1_3283.DWFA-661.2.2_12500.DF-3968.1.1_13274.AAEXP-11426.2.1_13281.AAEXP-11433.2.1_13284.AAEXP-11436.1.1_13297.AAEXP-11449.1.1_4854.DM-1255.2.5_11549.DM-1149.2.2_13290.AAEXP-11442.1.1_13293.AAEXP-11445.1.1_8287.TC-1035.2.5_11072.B2B-1154.2.5_12642.DM-1870.1.1_12646.MTD-779.2.2_13238.DM-1579.1.1_13379.DM-1372.1.1_5562.DWFA-732.2.2_13269.AAEXP-11421.1.1_13292.AAEXP-11444.1.1_3961.B2B-663.2.3_6732.DF-3818.2.4_13294.AAEXP-11446.1.1_220.DF-1925.1.9_12498.DM-1867.2.3_13291.AAEXP-11443.1.1_10382.DF-3962.1.2_10550.DWFA-884.2.2_10551.DAL-1134.2.2_12645.DAL-1151.2.1_13176.B2B-1035.2.1_13271.AAEXP-11423.2.1_13272.AAEXP-11424.1.1_13288.AAEXP-11440.2.1_7616.DWFA-777.2.2_12457.WDW-653.2.2_13135.DF-4076.2.1_13275.AAEXP-11427.2.1_13277.AAEXP-11429.2.1_13278.AAEXP-11430.1.1_13286.AAEXP-11438.1.1_13295.AAEXP-11447.1.1_13276.AAEXP-11428.2.1_2962.DF-3552.2.6_8393.DPAY-3431.2.2_8635.DM-1158.2.3_8776.DM-1442.2.2_12003.DM-1857.2.1_12644.WTT-1296.2.2_13273.AAEXP-11425.2.1_6402.DWFA-716.2.3_7584.TACO-60.2.2_12499.MTD-319.2.5_13134.DF-3988.2.1_13289.AAEXP-11441.1.1_2455.DPAY-2828.2.2_6359.DM-1411.2.10_11861.CEX-77.1.6_13280.AAEXP-11432.1.1_13283.AAEXP-11435.2.1_13298.AAEXP-11450.1.1_13381.DM-1917.2.2_9683.SEO-747.2.2_13132.DM-1798.2.1_13279.AAEXP-11431.1.1_13296.AAEXP-11448.1.1_10794.DF-3869.2.1_12687.TACO-153.1.1_13270.AAEXP-11422.2.1_13282.AAEXP-11434.1.1_4121.WDW-356.2.5_7759.DWFA-814.2.2_11547.DF-3929.2.2_13285.AAEXP-11437.1.1; privacySettings=%7B%22v%22%3A2%2C%22t%22%3A1724630400%2C%22m%22%3A%22LAX_AUTO%22%2C%22consent%22%3A%5B%22NECESSARY%22%2C%22PERFORMANCE%22%2C%22COMFORT%22%2C%22MARKETING%22%5D%7D; dapVn=1; LMTBID=v2|d40b8a90-319d-405c-bb4c-2c5f820fda65|7c9c332e58559ab733a8739f4b8376c5; _ga_66CXJP77N5=GS1.1.1724700694.1.0.1724700694.0.0.1273216881; _ga=GA1.1.1559873423.1724700694; FPID=FPID2.2.9MzRwflFvBMLZAKDZ1yqroLtbzMVPW7Sh%2F3wP2Lf5yY%3D.1724700694; FPLC=H5ojUe%2BJz2UVvGQi4kegQyojy796w5aipKb683BPwdsBCoZUcm48R6QhPnvlGuyOUMY%2BpquqPEmaQLwnb24%2BaGXNB7rP7oFkxttPyffR6wO8gXz1gUxFaJkZ6G9iFQ%3D%3D; FPAU=1.2.176948772.1724700696; dapSid=%7B%22sid%22%3A%22054c0a96-ae3c-4089-89cb-1866bd8e029d%22%2C%22lastUpdate%22%3A1724700913%7D',
    'origin': 'https://www.deepl.com',
    'priority': 'u=1, i',
    'referer': 'https://www.deepl.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

# resp = requests.post("https://www2.deepl.com/jsonrpc?method=LMT_split_text",
#     headers = headers,
#     data={"jsonrpc":"2.0","method": "LMT_split_text","params":{"texts":["I like chinese girls and girls and"],"commonJobParams":{"mode":"translate","textType":"plaintext"},"lang":{"lang_user_selected":"EN","preference":{"weight":{"DE":0.16948,"EN":7.78366,"ES":0.0716,"FR":0.10785,"IT":0.16032,"JA":0.02796,"NL":0.15389,"PL":0.0133,"PT":0.01705,"RU":0.01128,"ZH":0.77952,"BG":0,"CS":0.0053,"DA":0.03459,"EL":0,"ET":0.02114,"FI":0.00046,"HU":0.00209,"ID":0.0008,"KO":0,"LV":0.00127,"LT":0.00829,"NB":0.23829,"RO":0.00437,"SK":0.01054,"SL":0.0154,"SV":0.01962,"TR":0.0029,"UK":0,"AR":0},"default":"default"}}},"id":id}
# )
# print(resp.status_code)
# print(resp.json())

id = generate_id()
ts = generate_timestamp(["I like chinese girls and girls and"])
resp = requests.post("https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs",
    headers = headers,
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": [
            {
                "kind": "default",
                "sentences": [
                {
                    "text": "I like chinese girls and girls and",
                    "id": 1,
                    "prefix": ""
                }
                ],
                "raw_en_context_before": [],
                "raw_en_context_after": [],
                "preferred_num_beams": 4
            }
            ],
            "lang": {
            "target_lang": "ZH",
            "preference": {
                "weight": {},
                "default": "default"
            },
            "source_lang_computed": "EN"
            },
            "priority": 1,
            "commonJobParams": {
            "quality": "normal",
            "regionalVariant": "zh-Hans",
            "mode": "translate",
            "browserType": 1,
            "textType": "plaintext"
            },
            "timestamp": ts
        },
        "id": id
        })
)
print(resp.status_code)
print(resp.json())