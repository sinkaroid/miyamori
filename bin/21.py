#!python
#!C:\Python37\python.exe
from colorama import Fore, Style
import feedparser

print(Fore.RED)
print("""
        _                                  _ 
  /\/\ (_)_   _  __ _ _ __ ___   ___  _ __(_)
 /    \| | | | |/ _` | '_ ` _ \ / _ \| '__| |
/ /\/\ \ | |_| | (_| | | | | | | (_) | |  | |
\/    \/_|\__, |\__,_|_| |_| |_|\___/|_|  |_|
          |___/    LK21

                        genre args: """+Fore.CYAN+"""
                        (action, action-adventure, adventure, animation, comedy, crime, documentary, drama, 
                        family, fantasy, history, horror, kids, music, mystery, romance, 
                        sci-fi-fantasy, science-fiction, thriller, tv-movie, war, western)                          
""")
print(Style.RESET_ALL)
genre = input("genre: ")
halaman = input("page: ")
if genre.strip():
    print("ok")
else:
    print("null")

print ("\nyou are make request for: genre "+Fore.RED+genre+" // and page" +halaman)

feed = feedparser.parse("https://dunialk21.me/"+genre+"/feed/"+"?paged="+halaman)

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link

    content = entry.summary
    print ("{} -> [ {} ]".format(Fore.GREEN + article_title, Fore.BLUE +article_link+'play/' + Fore.GREEN))
