import json

import requests

from models import RequestDTO, ResponseDTO


def send_request_to_chat(message: str) -> str:
    base_url = 'https://chatbot.theb.ai'

    session = requests.session()
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,ro;q=0.6",
        "Content-Type": "application/json",
        "Dnt": "1",
        "Origin": "https://chatbot.theb.ai",
        "Referer": "https://chatbot.theb.ai/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    session.get(base_url, headers=headers)

    resp = session.post(f'{base_url}/api/chat-process', json={
        "options": {},
        "prompt": message
    }, headers=headers)
    text = resp.text.split('}]}}')[-2].strip() + '}]}}'
    data = json.loads(text)
    return data['text']


def get_response(dto: RequestDTO) -> ResponseDTO | None:
    try:
        message = send_request_to_chat(dto.message)
        return ResponseDTO(message=message)
    except:
        return None
