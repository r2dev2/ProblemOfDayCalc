import subprocess
import fnc

fnc.init("link.txt")
subprocess.call("cat htmlSource.txt | grep href | grep png >> link.txt", shell=True)

unparsed = open("link.txt", "r")
lunparsed = unparsed.readlines()
unparsed.close()

lunparsed = lunparsed[0]
fno = 0
for i in range(len(lunparsed)):
    if lunparsed[i] == "/":
        fno = i
        break

flunparsed = lunparsed[fno:]
eurl = ""

for i in flunparsed:
    if i == '"':
        break
    eurl += i

durl = "rkorsunsky.weebly.com"+eurl
fnc.init("link.txt")
l = open("link.txt", "w")
l.write(durl)
l.close()
