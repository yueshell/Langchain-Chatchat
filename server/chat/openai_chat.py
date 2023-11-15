import os

from fastapi.responses import StreamingResponse
from typing import List, Optional
import openai
# from openai import OpenAI
from configs import LLM_MODELS, logger, log_verbose
from server.utils import get_model_worker_config, fschat_openai_api_address
from pydantic import BaseModel


class OpenAiMessage(BaseModel):
    role: str = "user"
    content: str = "hello"


class OpenAiChatMsgIn(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: List[OpenAiMessage]
    temperature: float = 0.7
    n: int = 1
    max_tokens: Optional[int] = None
    stop: List[str] = []
    stream: bool = False
    presence_penalty: int = 0
    frequency_penalty: int = 0


async def openai_chat(msg: OpenAiChatMsgIn):
    config = get_model_worker_config(msg.model)
    openai.api_key = config.get("api_key", "EMPTY")
    print(f"{openai.api_key=}")
    openai.api_base = config.get("api_base_url", fschat_openai_api_address())
    openai.proxy = config.get("openai_proxy", "EMPTY")
    print(f"{openai.api_base=}",f"{openai.proxy=}")
    print(msg)

    async def get_response(msg):
        data = msg.dict()

        try:
            response = await openai.ChatCompletion.acreate(**data)
            if msg.stream:
                async for data in response:
                    if choices := data.choices:
                        if chunk := choices[0].get("delta", {}).get("content"):
                            print(chunk, end="", flush=True)
                            yield chunk
            else:
                if response.choices:
                    answer = response.choices[0].message.content
                    print(answer)
                    yield(answer)
        except Exception as e:
            msg = f"获取ChatCompletion时出错：{e}"
            logger.error(f'{e.__class__.__name__}: {msg}',
                         exc_info=e if log_verbose else None)

    return StreamingResponse(
        get_response(msg),
        media_type='text/event-stream',
    )
# async def openai_chat(msg: OpenAiChatMsgIn):
#     config = get_model_worker_config(msg.model)
#     # openai.api_key = config.get("api_key", "EMPTY")
#     os.environ["OPENAI_API_KEY"] = config.get("api_key", "EMPTY")
#     os.environ["https_proxy"] = config.get("openai_proxy", "EMPTY")
#     # os.environ["https_proxy"] = "http://heyue:heyue2019@172.16.6.7:1080"
#     client = OpenAI()
#     # print(f"{openai.api_key=}")
#     # openai.api_base = config.get("api_base_url", fschat_openai_api_address())
#     # print(f"{openai.api_base=}")
#     print(msg)
#
#     async def get_response(msg):
#         data = msg.dict()
#
#         try:
#             response = await client.chat.completions.create(**data)
#             print("sssssssss",response)
#             if msg.stream:
#                 async for data in response:
#                     if choices := data.choices:
#                         if chunk := choices[0].get("delta", {}).get("content"):
#                             print(chunk, end="", flush=True)
#                             yield chunk
#             else:
#                 if response.choices:
#                     answer = response.choices[0].message.content
#                     print(answer)
#                     yield(answer)
#         except Exception as e:
#             msg = f"获取ChatCompletion时出错：{e}"
#             logger.error(f'{e.__class__.__name__}: {msg}',
#                          exc_info=e if log_verbose else None)
#
#     return StreamingResponse(
#         get_response(msg),
#         media_type='text/event-stream',
#     )