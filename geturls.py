from duckduckgo_search import DDGS  # type: ignore
from colorama import Fore, Style
import sys,json

def contains_any_string(main_string, strings_to_check):
    for string in strings_to_check:
        if (string in main_string):
            return True
    return False

with open("categories/scam.json") as lists:
    lists_urls = []
    for i in json.loads(lists.read())["links"]:
        lists_urls.append(i)
    

results = DDGS().text(sys.argv[1], max_results=2000)

for item in results:
    if not contains_any_string(item['href'], lists_urls):
        if not any(url in item['href'] for url in ["microsoft.com", "msn.com", "scratch.mit.edu", "xbox.com", "facebook.com", "linkedin.com", "chromewebstore.google.com", "withgoogle.com", "safetydetectives.com", "bestbuy.com", "support.google.com", "wikipedia.org", "minecraft.net", "sourceforge.net", "archive.org", "java.com", "gamesradar.com", "makeuseof.com", "techradar.com", "tynker.com", "apps.apple.com", "chrome.google.com"]):
            if not "sites.google.com" in item["href"]:
                hrefsplit = item['href'].split("/")[2].replace("www.", "")
            else:
                hrefsplit = item['href'].split("https://")[1]
                if hrefsplit[-1] == "/":
                    hrefsplit = hrefsplit[:-1]
                if len(hrefsplit.split("/")) > 2:
                    hrefsplit = f"{hrefsplit.split('/')[0]}/{hrefsplit.split('/')[1]}/{hrefsplit.split('/')[2]}"
            print(f"{Fore.GREEN}{Style.BRIGHT}{hrefsplit}{Style.RESET_ALL}")
            
            #  - {Fore.YELLOW}{item['body'][0:50]}{Style.RESET_ALL}