import numpy as np
import matplotlib.pyplot as plt
import math

from bs4 import BeautifulSoup
from urllib.request import urlopen

import argparse

parser = argparse.ArgumentParser(description="Get your username's QR code from the 3rd HackMIT puzzle!")
parser.add_argument('u', metavar='username', type=str,
                   help='your username here')
parser.set_defaults(u="uthsavc")
args = parser.parse_args()
user=args.u

url = "http://0xd09eb17e.dogemit.party/p/" + user

soup = BeautifulSoup(urlopen(url).read())

num = int(soup.find('h1').get_text()) # that huge number
num_binary = bin(num)[2:] # that huge number in binary. AS A STRING. AS. A. STRING.
num_bits = len(num_binary) # i've seen 21**2 and 25**2...

num_bits_sqrt = math.sqrt(num_bits)

arr = np.zeros([num_bits_sqrt, num_bits_sqrt])
for i in range(len(num_binary)):
    c = i % num_bits_sqrt
    r = (i - c)/num_bits_sqrt
    arr[r, c] = int(num_binary[i])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.spy(arr)
plt.axis('off')
plt.show()

# can't figure out a way to read QR codes using python3 though.

