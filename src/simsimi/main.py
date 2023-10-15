import requests

headers = {
    'os': 'i',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'av': '8.5.3',
    'appcheck': 'SIMSIMI_IOS_APPCHECK',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'SimsimiReactNative/3 CFNetwork/1408.0.4 Darwin/22.5.0'
    }

language = input("🤖: Choose language (en, ar, ...): ")

while True:
    prompt = input("👦: ")

    json_data = {
        'uid': 430918161,
        'av': '8.5.3',
        'os': 'i',
        'lc': language,
        'cc': 'IQ',
        'tz': 'Asia/Baghdad',
        'cv': '',
        'free_level': 10,
        'logUID': '430918161',
        'reg_now_days': 3,
        'message': prompt
        }
    
    response = requests.post('https://bumcomingo.simsimi.com/simtalk/get_talk_set', headers=headers, json=json_data).json()
    print(f"🤖: {response['sentence']}")
