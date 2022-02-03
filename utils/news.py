from main.settings import settings


def format_data(data: list) -> tuple:
    """Helper function to reformat the response data from all APIs

    Args:
        data[list]: List containing json responses from all news APIs
    """
    formatted_data = []
    acceptable_data_keys = ["data", "articles"]
    error = ()
    data_keys_to_parse = settings.other_api_query_keys.spilt(" ") if settings.other_api_query_keys else ""
    if data_keys_to_parse:
        acceptable_data_keys.extend(data_keys_to_parse)
    for index, value in enumerate(data):
        source = "reddit" if index == 0 else "newsapi" if index == 1 else "other"
        data_list = map(value.get, acceptable_data_keys)

        data_list = [article_set for article_set in list(data_list) if article_set]
        if data_list:
            data_to_format = []

            for article_set in data_list:
                data_to_format.extend(article_set)
            if source != "reddit":
                formatted_articles = [
                    {
                        "headline": article.get("title"),
                        "url": article.get("url"),
                        "source": source
                    }
                    for article in data_to_format
                ]
                formatted_data.extend(formatted_articles)
                error = ()
            else:
                formatted_articles = [
                    {
                        "headline": article_set.get("data")["title"],
                        "url": article_set.get("data")["url"],
                        "source": source
                    }
                    for article_set in article_set.get("children")
                ]
                formatted_data.extend(formatted_articles)
        else:
            error = (
                False, "Please check the data keys you passed in your environment variables."
                " Ensure it's a top level key in your API's response body whose value is the"
                " list of articles")
    return (True, formatted_data) if not error else error
