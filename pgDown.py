import subprocess

l = open('link.txt', 'r')
li = l.readlines()
l.close()

subprocess.call("wget "+li[0], shell=True)
