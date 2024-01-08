#!/bin/bash

cd /workspace/LLM_Server_Baichuan && nohup python manage_llm_server_baichuan.py >/dev/null 2>&1 &
echo "server runing"
/bin/bash
