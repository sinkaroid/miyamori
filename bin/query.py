#!python
#!C:\Python37\python.exe
from colorama import Fore, Style
import feedparser


print(Fore.RED)
print("""
Scrape by query 
example query args:(marvel, avengers, x-men, and so on)                          
""")
print(Style.RESET_ALL)
que = input("query: ")
if que.strip():
    print("ok")
else:
    print("null")


feed = feedparser.parse("https://dunialk21.me/?s="+que+"&feed=rss2")

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link

    content = entry.summary
    print ("{} -> [ {} ]".format(Fore.GREEN + article_title, Fore.BLUE +article_link + Fore.GREEN))
 