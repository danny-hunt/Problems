import urllib.request
import re

first_id = 12345

regex_matcher = re.compile(r" [0-9]+")

print(regex_matcher.search("sdaf asoifdjaosd 234 0"))

def search_id(id=first_id):
    try:
        output = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(id)).read()
    except:
        print(id)
    print(output)
    output = str(output)
    if regex_matcher.search(output) is not None:
        search_id(regex_matcher.search(output).group(0).strip())
    else:
        print(id)

search_id(63579)


