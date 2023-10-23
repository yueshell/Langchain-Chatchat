# prompt模板使用Jinja2语法，简单点就是用双大括号代替f-string的单大括号
# 本配置文件支持热加载，修改prompt模板后无需重启服务。


# LLM对话支持的变量：
#   - input: 用户输入内容

# 知识库和搜索引擎对话支持的变量：
#   - context: 从检索结果拼接的知识文本
#   - question: 用户提出的问题


PROMPT_TEMPLATES = {
    # LLM对话模板
    "llm_chat": "{{ input }}",

    # 基于本地知识问答的提示词模
    "knowledge_base_chat": """<指令>根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题”，不允许在答案中添加编造成分，答案请使用中文。 </指令>

<已知信息>{{ context }}</已知信息>

<问题>{{ question }}</问题>""",
    # 基于agent的提示词模板
    "agent_chat":
    """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    history:
    {history}

    Question: {input}
    Thought: {agent_scratchpad}
"""
}

## GPT或Qwen 的Prompt
# """
# Answer the following questions as best you can. You have access to the following tools:
#
# {tools}
#
# Please note that the "知识库查询工具" is information about the "西交利物浦大学" ,and if a question is asked about it, you must answer with the knowledge base
#
# Use the following format:
#
# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question
#
# Begin!
#
# history:
# {history}
#
# Question: {input}
# Thought: {agent_scratchpad}
# """


## ChatGLM-Pro的Prompt

# """
# 请请严格按照提供的思维方式来思考。你的知识不一定正确，所以你一定要用提供的工具来思考，并给出用户答案。
# 你有以下工具可以使用:
# {tools}
# ```
# Question: 用户的提问或者观察到的信息，
# Thought: 你应该思考该做什么，是根据工具的结果来回答问题，还是决定使用什么工具。
# Action: 需要使用的工具，应该是在[{tool_names}]中的一个。
# Action Input: 传入工具的内容
# Observation: 工具给出的答案（不是你生成的）
# ... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
# Thought: 通过工具给出的答案，你是否能回答Question。
# Final Answer是你的答案
#
# 现在，我们开始！
# 你和用户的历史记录:
# History:
# {history}
#
# 用户开始以提问：
# Question: {input}
# Thought: {agent_scratchpad}
#
# """
