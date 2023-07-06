import yagooglesearch
from datetime import datetime
import json


# Scrape csrankings.org for all the university names (there are 174 in US). May use bs4 or selenium or scrapy.
# Make a list 👇 Here
uni_names = []

# Copy the dep names and format them appropriately, from wa texts.
#   here   👇
uni_deps = []

# all_urls = [] # for later


def app(i_tbs: str) -> None:
    query = "filetype:pdf Univ. of Illinois at Urbana-Champaign CS Computer Science"
    #         add 2 loop here {    👆 over uni names   }{    👆 over dept names}
    client = yagooglesearch.SearchClient(
        query,
        tbs=i_tbs,
        max_search_result_urls_to_return=1000,
        http_429_cool_off_time_in_minutes=45,
        http_429_cool_off_factor=1.5,
        # proxy="socks5h://127.0.0.1:9050",
        verbosity=5,
        verbose_output=True,  # False (only URLs) or True (rank, title, description, and URL)
    )
    client.assign_random_user_agent()

    urls = client.search()

    len(urls)
    # add the urls to the all_urls list
    with open("urls.txt", "w", encoding="utf-8") as f:
        json.dump(urls, f, ensure_ascii=False, indent=4)


# Change the print. Return a json dumps. Or just directly write to a json (NOT CSV, we still have work left)

if __name__ == "__main__":
    r = yagooglesearch.get_tbs(
        from_date=datetime(2020, 8, 31), to_date=datetime(2023, 6, 2)
    )
    app(r)
