from pydantic import BaseModel, Field
from langchain.prompts.chat import ChatMessagePromptTemplate
from configs import logger, log_verbose
from typing import List, Tuple, Dict, Union

from langchain.utilities import DuckDuckGoSearchAPIWrapper
from configs.kb_config import PROXYS


class History(BaseModel):
    """
    对话历史
    可从dict生成，如
    h = History(**{"role":"user","content":"你好"})
    也可转换为tuple，如
    h.to_msy_tuple = ("human", "你好")
    """
    role: str = Field(...)
    content: str = Field(...)

    def to_msg_tuple(self):
        return "ai" if self.role=="assistant" else "human", self.content

    def to_msg_template(self, is_raw=True) -> ChatMessagePromptTemplate:
        role_maps = {
            "ai": "assistant",
            "human": "user",
        }
        role = role_maps.get(self.role, self.role)
        if is_raw: # 当前默认历史消息都是没有input_variable的文本。
            content = "{% raw %}" + self.content + "{% endraw %}"
        else:
            content = self.content

        return ChatMessagePromptTemplate.from_template(
            content,
            "jinja2",
            role=role,
        )

    @classmethod
    def from_data(cls, h: Union[List, Tuple, Dict]) -> "History":
        if isinstance(h, (list,tuple)) and len(h) >= 2:
            h = cls(role=h[0], content=h[1])
        elif isinstance(h, dict):
            h = cls(**h)

        return h
class CustomDuckDuckGoSearchAPIWrapper(DuckDuckGoSearchAPIWrapper):
    def results(
            self, query: str, num_results: int, backend: str = "api"
    ) -> List[Dict[str, str]]:
        """Run query through DuckDuckGo and return metadata.

        Args:
            query: The query to search for.
            num_results: The number of results to return.

        Returns:
            A list of dictionaries with the following keys:
                snippet - The description of the result.
                title - The title of the result.
                link - The link to the result.
        """
        from duckduckgo_search import DDGS

        with DDGS(proxies=PROXYS, timeout=20) as ddgs:
            results = ddgs.text(
                query,
                region=self.region,
                safesearch=self.safesearch,
                timelimit=self.time,
                backend=backend,
            )
            if results is None:
                return [{"Result": "No good DuckDuckGo Search Result was found"}]

            def to_metadata(result: Dict) -> Dict[str, str]:
                if backend == "news":
                    return {
                        "date": result["date"],
                        "title": result["title"],
                        "snippet": result["body"],
                        "source": result["source"],
                        "link": result["url"],
                    }
                return {
                    "snippet": result["body"],
                    "title": result["title"],
                    "link": result["href"],
                }

            formatted_results = []
            for i, res in enumerate(results, 1):
                if res is not None:
                    formatted_results.append(to_metadata(res))
                if len(formatted_results) == num_results:
                    break
        return formatted_results