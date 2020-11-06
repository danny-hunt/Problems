import pickle
import urllib.request

data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
after = pickle.loads(data)
print(after)

for line in after:
    for letter in line:
        print(letter[0]*letter[1], end='')
    print("")
