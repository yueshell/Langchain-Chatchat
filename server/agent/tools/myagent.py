## 单独运行的时候需要添加
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain.prompts import PromptTemplate
from langchain import LLMChain
from server.agent import model_container

_PROMPT_TEMPLATE = """
你需要根据以下信息回复用户关于商品价格的查询，如果你无法从以下信息中解答用户问题，请说我不知道。
商品信息列表如下：
    可口可乐单价5元
    百事可乐单价3元
    美式咖啡22元一杯
    拿铁和澳白的单价都是28元，澳白加奶单价需要加5元
    一杯摩卡价格是36元
    一杯卡布奇洛的价格是30元

这是用户输入的问题：
{input}
"""
PROMPT = PromptTemplate(
    input_variables=["input"],
    template=_PROMPT_TEMPLATE,
)
def search_chain(query: str):
    model = model_container.MODEL
    llm_math = LLMChain(llm=model, verbose=True, prompt=PROMPT)
    ans = llm_math.run(query)
    return ans


if __name__ == "__main__":
    result = search_chain("2的三次方")
    print("答案:",result)

