# *_*coding:utf-8 *_*
# @Author : YueMengRui

FASTAPI_HOST = '0.0.0.0'
FASTAPI_PORT = 5000

BAICHUAN_CONFIG = {
    "model_name": "Baichuan2_13B_8k",
    "model_name_or_path": "",
    "device": "cuda"
}

# API LIMIT
API_LIMIT = {
    "chat": "15/minute",
    "token_count": "60/minute",
}
