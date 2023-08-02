import base64
from icecream import ic
import json
import logging


def check_padding(token: bytes) -> bytes:
    try:
        padding = b""
        if len(token) % 4 == 2:
            padding = b"=="
        elif len(token) % 4 == 3:
            padding = b"="
        return padding
    except Exception as e:
        logging.error(e)
        ic(e)
        ic()


def jwt_decode(token: str) -> list[str, str]:
    try:
        token = token.encode().split(b'.')
        if len(token) != 3:
            return ['Не валидный JWT']
        else:
            header = json.loads(base64.b64decode(token[0] + check_padding(token[0])).decode('utf-8'))
            payload = json.loads(base64.b64decode(token[1] + check_padding(token[1])).decode('utf-8'))
            json_header = json.dumps(header, indent=2)
            json_payload = json.dumps(payload, indent=2)
            return [json_header, json_payload]
    except Exception as e:
        logging.error(e)
        ic(e)
        ic()
