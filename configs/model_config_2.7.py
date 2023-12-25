import os

# 可以指定一个绝对路径，统一存放所有的Embedding和LLM模型。
# 每个模型可以是一个单独的目录，也可以是某个目录下的二级子目录。
# 如果模型目录名称和 MODEL_PATH 中的 key 或 value 相同，程序会自动检测加载，无需修改 MODEL_PATH 中的路径。
MODEL_ROOT_PATH = ""

# 选用的 Embedding 名称
EMBEDDING_MODEL = "bge-large-zh-v1.5"  # bge-large-zh

# Embedding 模型运行设备。设为"auto"会自动检测，也可手动设定为"cuda","mps","cpu"其中之一。
EMBEDDING_DEVICE = "auto"

# 如果需要在 EMBEDDING_MODEL 中增加自定义的关键字时配置
EMBEDDING_KEYWORD_FILE = "keywords.txt"
EMBEDDING_MODEL_OUTPUT_PATH = "output"

# 要运行的 LLM 名称，可以包括本地模型和在线模型。
# 第一个将作为 API 和 WEBUI 的默认模型
LLM_MODELS = ["peft_Baichuan2-13B-Chat"]
LLM_MODEL = "peft-Qwen-14B-Chat"

# AgentLM模型的名称 (可以不指定，指定之后就锁定进入Agent之后的Chain的模型，不指定就是LLM_MODELS[0])
Agent_MODEL = None

# LLM 运行设备。设为"auto"会自动检测，也可手动设定为"cuda","mps","cpu"其中之一。
LLM_DEVICE = "auto"

# 历史对话轮数s
HISTORY_LEN = 20

# 大模型最长支持的长度，如果不填写，则使用模型默认的最大长度，如果填写，则为用户设定的最大长度
MAX_TOKENS = None

# LLM通用对话参数
TEMPERATURE = 0.1
# TOP_P = 0.95 # ChatOpenAI暂不支持该参数
LANGCHAIN_LLM_MODEL = {
    # "OpenAI": {
    #     "model_name": "gpt-3.5-turbo",
    #     "device": "cpu",
    #     "api_base_url": "https://api.openai.com/v1",
    #     "api_key": "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",
    #     "openai_proxy": "socks5://172.16.6.7:9050",
    #     "placeholder": "OpenaiWorker",
    # },
}
ONLINE_LLM_MODEL = {
    # 线上模型。请在server_config中为每个在线API设置不同的端口

    "gpt-3.5-turbo": {
        "model_name": "gpt-3.5-turbo",
        "device": "cpu",
        "api_base_url": "https://api.openai.com/v1",
        "api_key": "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",
        "openai_proxy": "http://heyue:heyue2019@172.16.6.7:1080",
    },

    # # 具体注册及api key获取请前往 http://open.bigmodel.cn
    # "zhipu-api": {
    #     "api_key": "",
    #     "version": "chatglm_turbo",  # 可选包括 "chatglm_turbo"
    #     "provider": "ChatGLMWorker",
    # },
    #
    # # 具体注册及api key获取请前往 https://api.minimax.chat/
    # "minimax-api": {
    #     "group_id": "",
    #     "api_key": "",
    #     "is_pro": False,
    #     "provider": "MiniMaxWorker",
    # },
    #
    # # 具体注册及api key获取请前往 https://xinghuo.xfyun.cn/
    # "xinghuo-api": {
    #     "APPID": "",
    #     "APISecret": "",
    #     "api_key": "",
    #     "version": "v1.5",  # 你使用的讯飞星火大模型版本，可选包括 "v3.0", "v1.5", "v2.0"
    #     "provider": "XingHuoWorker",
    # },
    #
    # # 百度千帆 API，申请方式请参考 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/4lilb2lpf
    # "qianfan-api": {
    #     "version": "ERNIE-Bot",  # 注意大小写。当前支持 "ERNIE-Bot" 或 "ERNIE-Bot-turbo"， 更多的见官方文档。
    #     "version_url": "",  # 也可以不填写version，直接填写在千帆申请模型发布的API地址
    #     "api_key": "",
    #     "secret_key": "",
    #     "provider": "QianFanWorker",
    # },
    #
    # # 火山方舟 API，文档参考 https://www.volcengine.com/docs/82379
    # "fangzhou-api": {
    #     "version": "chatglm-6b-model",  # 当前支持 "chatglm-6b-model"， 更多的见文档模型支持列表中方舟部分。
    #     "version_url": "",  # 可以不填写version，直接填写在方舟申请模型发布的API地址
    #     "api_key": "",
    #     "secret_key": "",
    #     "provider": "FangZhouWorker",
    # },
    #
    # # 阿里云通义千问 API，文档参考 https://help.aliyun.com/zh/dashscope/developer-reference/api-details
    # "qwen-api": {
    #     "version": "qwen-turbo",  # 可选包括 "qwen-turbo", "qwen-plus"
    #     "api_key": "",  # 请在阿里云控制台模型服务灵积API-KEY管理页面创建
    #     "provider": "QwenWorker",
    # },
    #
    # # 百川 API，申请方式请参考 https://www.baichuan-ai.com/home#api-enter
    # "baichuan-api": {
    #     "version": "Baichuan2-53B",  # 当前支持 "Baichuan2-53B"， 见官方文档。
    #     "api_key": "",
    #     "secret_key": "",
    #     "provider": "BaiChuanWorker",
    # },
    #
    # # Azure API
    # "azure-api": {
    #     "deployment_name": "",  # 部署容器的名字
    #     "resource_name": "",  # https://{resource_name}.openai.azure.com/openai/ 填写resource_name的部分，其他部分不要填写
    #     "api_version": "",  # API的版本，不是模型版本
    #     "api_key": "",
    #     "provider": "AzureWorker",
    # },

}
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
        # "m3e-base": "/content/models/embedding_models/m3e-base",
        # "bge-large-zh": "/content/models/embedding_models/bge-large-zh",
        # "text2vec-bge-large-chinese": "/content/models/embedding_models/text2vec-bge-large-chinese",
    },
    # TODO: add all supported llm models
    "llm_model": {
        "chatglm2-6b": "/content/models/chatglm2-6b",
        "chatglm3-6b-32k": "/content/models/chatglm3-6b-32k",
        # "Qwen-7B-Chat": "/content/models/Qwen-7B-Chat",
        "peft_Baichuan2-13B-Chat": "/content/models/peft_models/peft_Baichuan2-13B-Chat",
        "Baichuan2-13B-Chat": "/content/models/baichuan-inc/Baichuan2-13B-Chat",
        # "Qwen-14B-Chat": "/content/models/Qwen-14B-Chat",
        "peft-Qwen-14B-Chat": "/content/models/peft_models/peft_Qwen-14B-Chat",
        # "peft_Qwen-7B-Chat-lora": "/content/models/peft_models/peft_Qwen-7B-Chat-lora",
        # "peft-ChatGLM2-6B-Chat": "/content/models/peft_models/peft_ChatGLM2-6B-Chat",
    },
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
# 你认为支持Agent能力的模型，可以在这里添加，添加后不会出现可视化界面的警告
SUPPORT_AGENT_MODEL = [
    "azure-api",
    "openai-api",
    "claude-api",
    "zhipu-api",
    "qwen-api",
    "Qwen",
    "baichuan-api",
    "agentlm",
    "chatglm3",
    "xinghuo-api",
    "Baichuan2-7B-Chat",
    "Baichuan2-13B-Chat",
    "peft-Qwen-14B-Chat",
]
