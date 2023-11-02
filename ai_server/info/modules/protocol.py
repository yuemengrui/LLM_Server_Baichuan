# *_*coding:utf-8 *_*
# @Author : YueMengRui
from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class ErrorResponse(BaseModel):
    object: str = 'error'
    errcode: int
    errmsg: str


class GenerationConfigs(BaseModel):
    max_new_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float]


class ChatRequest(BaseModel):
    prompt: str
    history: List = Field(default=[], description="历史记录")
    generation_configs: Dict[GenerationConfigs]
    stream: bool = Field(default=True, description="是否流式输出")


class TokenCountRequest(BaseModel):
    prompt: str


class TokenCountResponse(BaseModel):
    object: str = 'token_count'
    model_name: str
    prompt: str
    prompt_tokens: int
    max_tokens: int
    status: str
