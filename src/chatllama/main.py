import requests

headers = {
    'authority': 'us-central1-arched-keyword-306918.cloudfunctions.net',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

while True:
    prompt = input("👦: ")
    
    json_data = {
        'prompt': prompt,
    }

    response = requests.post('https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1', headers=headers, json=json_data).json()
    print(f"🤖: {response['completion']}")
