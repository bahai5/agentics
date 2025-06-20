from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.agent_toolkits import GmailToolkit 
toolkit = GmailToolkit()
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)


@tool
def web_search_duckduckgo(search_phrase: str):
    """Search the web using duckduckgo."""
    search = DuckDuckGoSearchResults()
    results = search.run(search_phrase) 
    return results

@tool
def news_search_duckduckgo(search_phrase: str):
    """Search news using duckduckgo."""
    search = DuckDuckGoSearchResults(backend="news")
    results = search.run(search_phrase) 
    return results

@tool
def gmail_send(search_phrase: str):
    """Search news using duckduckgo."""
    credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
    )
   api_resource = build_resource_service(credentials=credentials)
   toolkit = GmailToolkit(api_resource=api_resource)
   tools = toolkit.get_tools()

    results = search.run(search_phrase) 
    return results

tool_choices = {
    "web_search_duckduckgo": web_search_duckduckgo,
    "news_search_duckduckgo": news_search_duckduckgo,
}
