# *_*coding:utf-8 *_*
# @Author : YueMengRui
import os

FASTAPI_TITLE = 'LLM_Server_Baichuan'
FASTAPI_HOST = '0.0.0.0'
FASTAPI_PORT = 24620

MODEL_REGISTER_URL = 'http://paimongpt_server:24601/ai/model/register'
THIS_SERVER_HOST = 'http://paimongpt_baichuan_server:' + str(FASTAPI_PORT)


LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

BAICHUAN_CONFIG = {
    "model_name": "Baichuan2_13B_8k",
    "model_name_or_path": "/workspace/Models/Baichuan2_13B",
    "device": "cuda"
}

# API LIMIT
API_LIMIT = {
    "chat": "15/minute",
    "token_count": "60/minute",
}
