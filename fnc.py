import subprocess

def init(filename):
    subprocess.call("rm "+filename, shell=True)
    subprocess.call("touch "+filename, shell=True)
