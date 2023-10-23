import os

# 可以指定一个绝对路径，统一存放所有的Embedding和LLM模型。
# 每个模型可以是一个单独的目录，也可以是某个目录下的二级子目录
MODEL_ROOT_PATH = ""

# 在以下字典中修改属性值，以指定本地embedding模型存储位置。支持3种设置方法：
# 1、将对应的值修改为模型绝对路径
# 2、不修改此处的值（以 text2vec 为例）：
#       2.1 如果{MODEL_ROOT_PATH}下存在如下任一子目录：
#           - text2vec
#           - GanymedeNil/text2vec-large-chinese
#           - text2vec-large-chinese
#       2.2 如果以上本地路径不存在，则使用huggingface模型
MODEL_PATH = {
    "embed_model": {
        "bge-large-zh-v1.5": "/content/models/embedding_models/bge-large-zh-v1.5",
        "m3e-base": "/content/models/embedding_models/m3e-base",
        "bge-large-zh": "/content/models/embedding_models/bge-large-zh",
        "text2vec-bge-large-chinese": "/content/models/embedding_models/text2vec-bge-large-chinese",
    },
    # TODO: add all supported llm models
    "llm_model": {
        # "chatglm2-6b": "/content/models/chatglm2-6b",
        # "Qwen-7B-Chat": "/content/models/Qwen-7B-Chat",
        # "Baichuan2-7B-Chat": "/content/models/Baichuan2-7B-Chat",
        "Qwen-14B-Chat": "/content/models/Qwen-14B-Chat",
        "peft_Qwen-14B-Chat": "/content/models/peft_models/peft_Qwen-14B-Chat",
        "peft_Qwen-7B-Chat-lora": "/content/models/peft_models/peft_Qwen-7B-Chat-lora",
        "peft_ChatGLM2-6B-Chat": "/content/models/peft_models/peft_ChatGLM2-6B-Chat",
    },
}

# 选用的 Embedding 名称
EMBEDDING_MODEL = "bge-large-zh-v1.5"

# Embedding 模型运行设备。设为"auto"会自动检测，也可手动设定为"cuda","mps","cpu"其中之一。
EMBEDDING_DEVICE = "auto"

# LLM 名称
LLM_MODEL = "peft_Qwen-14B-Chat"

# LLM 运行设备。设为"auto"会自动检测，也可手动设定为"cuda","mps","cpu"其中之一。
LLM_DEVICE = "auto"

# 历史对话轮数
HISTORY_LEN = 20

# LLM通用对话参数
TEMPERATURE = 0.05
# TOP_P = 0.95 # ChatOpenAI暂不支持该参数

LANGCHAIN_LLM_MODEL = {
    # 不需要走Fschat封装的，Langchain直接支持的模型。
    # 调用chatgpt时如果报出： urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.openai.com', port=443):
    #  Max retries exceeded with url: /v1/chat/completions
    # 则需要将urllib3版本修改为1.25.11
    # 如果依然报urllib3.exceptions.MaxRetryError: HTTPSConnectionPool，则将https改为http
    # 参考https://zhuanlan.zhihu.com/p/350015032

    # 如果报出：raise NewConnectionError(
    # urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x000001FE4BDB85E0>:
    # Failed to establish a new connection: [WinError 10060]
    # 则是因为内地和香港的IP都被OPENAI封了，需要切换为日本、新加坡等地

    # 如果出现WARNING: Retrying langchain.chat_models.openai.acompletion_with_retry.<locals>._completion_with_retry in
    # 4.0 seconds as it raised APIConnectionError: Error communicating with OpenAI.
    # 需要添加代理访问(正常开的代理软件可能会拦截不上)需要设置配置openai_proxy 或者 使用环境遍历OPENAI_PROXY 进行设置
    # 比如: "openai_proxy": 'http://127.0.0.1:4780'

    # 这些配置文件的名字不能改动
    # "Azure-OpenAI": {
    #     "deployment_name": "your Azure deployment name",
    #     "model_version": "0701",
    #     "openai_api_type": "azure",
    #     "api_base_url": "https://your Azure point.azure.com",
    #     "api_version": "2023-07-01-preview",
    #     "api_key": "your Azure api key",
    #     "openai_proxy": "",
    # },
    # "OpenAI": {
    #     "model_name": "your openai model name(such as gpt-4)",
    #     "api_base_url": "https://api.openai.com/v1",
    #     "api_key": "your OPENAI_API_KEY",
    #     "openai_proxy": "",
    # },
    # "Anthropic": {
    #     "model_name": "your claude model name(such as claude2-100k)",
    #     "api_key":"your ANTHROPIC_API_KEY",
    # }
}

ONLINE_LLM_MODEL = {
    # # 调用chatgpt时如果报出： urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.openai.com', port=443):
    # #  Max retries exceeded with url: /v1/chat/completions
    # # 则需要将urllib3版本修改为1.25.11
    # # 如果依然报urllib3.exceptions.MaxRetryError: HTTPSConnectionPool，则将https改为http
    # # 参考https://zhuanlan.zhihu.com/p/350015032
    #
    # # 如果报出：raise NewConnectionError(
    # # urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x000001FE4BDB85E0>:
    # # Failed to establish a new connection: [WinError 10060]
    # # 则是因为内地和香港的IP都被OPENAI封了，需要切换为日本、新加坡等地
    #
    # # 如果出现WARNING: Retrying langchain.chat_models.openai.acompletion_with_retry.<locals>._completion_with_retry in
    # # 4.0 seconds as it raised APIConnectionError: Error communicating with OpenAI.
    # # 需要添加代理访问(正常开的代理软件可能会拦截不上)需要设置配置openai_proxy 或者 使用环境遍历OPENAI_PROXY 进行设置
    # # 比如: "openai_proxy": 'http://127.0.0.1:4780'
    # # 线上模型。请在server_config中为每个在线API设置不同的端口
    # # 具体注册及api key获取请前往 http://open.bigmodel.cn
    # "zhipu-api": {
    #     "api_key": "",
    #     "version": "chatglm_pro",  # 可选包括 "chatglm_lite", "chatglm_std", "chatglm_pro"
    #     "provider": "ChatGLMWorker",
    # },
    # # 具体注册及api key获取请前往 https://api.minimax.chat/
    # "minimax-api": {
    #     "group_id": "",
    #     "api_key": "",
    #     "is_pro": False,
    #     "provider": "MiniMaxWorker",
    # },
    # # 具体注册及api key获取请前往 https://xinghuo.xfyun.cn/
    # "xinghuo-api": {
    #     "APPID": "",
    #     "APISecret": "",
    #     "api_key": "",
    #     "is_v2": False,
    #     "provider": "XingHuoWorker",
    # },
    # # 百度千帆 API，申请方式请参考 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/4lilb2lpf
    # "qianfan-api": {
    #     "version": "ernie-bot-turbo",  # 当前支持 "ernie-bot" 或 "ernie-bot-turbo"， 更多的见官方文档。
    #     "version_url": "", # 也可以不填写version，直接填写在千帆申请模型发布的API地址
    #     "api_key": "",
    #     "secret_key": "",
    #     "provider": "QianFanWorker",
    # },
    # # 火山方舟 API，文档参考 https://www.volcengine.com/docs/82379
    # "fangzhou-api": {
    #     "version": "chatglm-6b-model",  # 当前支持 "chatglm-6b-model"， 更多的见文档模型支持列表中方舟部分。
    #     "version_url": "",  # 可以不填写version，直接填写在方舟申请模型发布的API地址
    #     "api_key": "",
    #     "secret_key": "",
    #     "provider": "FangZhouWorker",
    # },
    # # 阿里云通义千问 API，文档参考 https://help.aliyun.com/zh/dashscope/developer-reference/api-details
    # "qwen-api": {
    #     "version": "qwen-turbo",  # 可选包括 "qwen-turbo", "qwen-plus"
    #     "api_key": "",  # 请在阿里云控制台模型服务灵积API-KEY管理页面创建
    #     "provider": "QwenWorker",
    # },
}

# 通常情况下不需要更改以下内容

# nltk 模型存储路径
NLTK_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "nltk_data")
VLLM_MODEL_DICT = {
    # "Qwen-14B-Chat": "/content/models/Qwen-14B-Chat",
    # "peft_Qwen-14B-Chat": "/content/models/peft_models/peft_Qwen-14B-Chat",
    # "peft_Qwen-7B-Chat-lora": "/content/models/peft_models/peft_Qwen-7B-Chat-lora",
    # "peft_ChatGLM2-6B-Chat": "/content/models/peft_models/peft_ChatGLM2-6B-Chat",
}
