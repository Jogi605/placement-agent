from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

search = TavilySearchResults(max_results=1)
results = search.invoke({"query": "test tavily connection"})
print("✅ TAVILY WORKS!" if results else "❌ TAVILY FAILED")
print("Results:", [r["content"][:100] for r in results])