#!python
#!C:\Python37\python.exe
from colorama import Fore, Style
import feedparser

print(Fore.RED)
print("""
Gudangmovie scraper 

genre args: """+Fore.CYAN+"""(action, barat, comedy, crime,
drama, family, horror, india, mystery, thriller)                          
""")
print(Style.RESET_ALL)
genre = input("genre: ")
halaman = input("page: ")
if genre.strip():
    print("ok")
else:
    print("null")

print ("\nyou are make request for: genre "+Fore.RED+genre+" // and page" +halaman)

feed = feedparser.parse("https://gudangmovies.cc/category/"+genre+"/feed/"+"?paged="+halaman)

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link

    content = entry.summary
    wrap = article_link.replace('https://gudangmovies.cc/','https://miyamori.kireisubs.org/get.php?id=')
    print ("{} -> [ {} ]".format(Fore.GREEN + article_title, Fore.BLUE +wrap))
 