import requests

headers = {
    'authority': 'api.prodia.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

while True:
    prompt = input("👦: ")

    params = {
        'new': 'true',
        'prompt': prompt,
        'model': 'anythingV5_PrtRE.safetensors [893e49b9]',
        'negative_prompt': '',
        'steps': '25',
        'cfg': '7',
        'seed': '3468934753',
        'sampler': 'DPM++ 2M Karras',
        'aspect_ratio': 'square',
    }

    image_id = requests.get('https://api.prodia.com/generate', headers=headers, params=params).json()['job']

    while True:
        response = requests.get(f'https://api.prodia.com/job/{image_id}', headers=headers).json()
        if response['status'] == 'succeeded':
            print(f"🤖: https://images.prodia.xyz/{image_id}.png")
            break
