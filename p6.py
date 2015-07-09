#if you like waiting 20 minutes for puzzle solutions then i've got the thing for you!

from itertools import product
import time

start = time.time()

# alphabetic characters
avail = []

for i in range(ord('A'), ord('Z')+1):
    avail.append(chr(i))

for i in range(ord('a'), ord('z')+1):
    avail.append(chr(i))

left=[] #possible left halves of password
right=[] #possible right halves of password

def ck(str):
    x = map(ord, str)
    a=0
    b=0
    for i in x:
        a = (a+i) % 0xff
        b = (b+a) % 0xff
    return (b << 8) | a

#see if r appended to anything in l_list gives a valid password
#need to check even condition
def test_left(l_list, r):
    for l in l_list:
        if ck((l+r)[0::2]) == 0x0000:
            print("password: " + l + r)
            print("took: " + str(time.time() - start) + " seconds")

#same as above but w/ r_list and right
def test_right(r_list, l):
    for r in r_list:
        if ck((l+r)[0::2]) == 0x0000:
            print("password: " + l + r)
            print("took: " + str(time.time() - start) + " seconds")

def bash(l):
    for attempt in product(avail, repeat=l):
        w = ''.join(attempt)
        if ck(w) == 0xd06e:
            left.append(w)
            test_right(right, w)
        if ck(w) == 0xf00d:
            right.append(w)
            test_left(left, w)

bash(6) #chose to look at length 12 passwords


