from typing import Dict, List

from langchain.utilities import DuckDuckGoSearchAPIWrapper
from configs.kb_config import PROXYS

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