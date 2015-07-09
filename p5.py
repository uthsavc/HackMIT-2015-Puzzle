from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
from queue import Queue
import webbrowser

init = "http://0xd09eeffec7.dogemit.party/"

on = "http://0xd09eeffec7.dogemit.party/"

visited = set()

urls = set()

q = Queue()

def get_coords(end):
    u = 0
    l = 0
    for char in end:
        if char=="U":
            u += 1
        elif char=="D":
            u = u - 1
        elif char=="L":
            l += 1
        elif char == "R":
            l = l - 1
    return (l,u)

def explore(url):
    soup = BeautifulSoup(urlopen(url).read())
    a_list = soup.findAll('a')
    to_return = []
    for i in range(len(a_list)):
        href = a_list[i]['href'][1:]
        if href[0] != "s":
            coords = get_coords(href)
            to_return.append((href, coords))
        else:
            to_return.append((href,-1))
    return to_return



#initialize
to_return = explore(init)
for i in to_return:
    h = i[0]
    c = i[1]
    q.put((h,c))


while len(urls) < 9:
    h, c = q.get()

    # visit
    if c not in visited:
        visited.add(c)

        # currently on
        on = init + h

        neighbors = explore(on)

        for n in neighbors:
            h = n[0]
            c = n[1]
            if c == -1:
                urls.add(h)
                webbrowser.open(init+h)
                print(init+h)
            else:
                q.put((h,c))

for i in range(len(urls)):
    urls[i] = init + urls[i]

print(urls)

