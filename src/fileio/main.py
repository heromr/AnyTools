import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

while True:
    file_path_or_url = input("👦 Enter file path or url: ")

    if file_path_or_url.startswith('http'):
        response = requests.head(file_path_or_url)
        content_type = response.headers.get('content-type', 'application/octet-stream')
        file_content = requests.get(file_path_or_url).content
        file_name = os.path.basename(file_path_or_url)

    else:
        with open(file_path_or_url, 'rb') as local_file:
            content_type = 'application/octet-stream'
            file_content = local_file.read()
            file_name = os.path.basename(file_path_or_url)

    files = {
        'file': (file_name, file_content, content_type),
        }

    response = requests.post("https://file.io/", headers=headers, files=files).json()

    print(f"🤖: {response['link']}")
