# Copyright (c) 2022 CircularEcoBIM, authors: Artur Tomczak <artomczak@gmail.com>, Ana Mestre <amestre@3drivers.pt >, Joana Fernandes <joanabfernandes@tecnico.ulisboa.pt>
# This file is part of CircularEcoBIM.

from urllib import request, parse
import json
from datetime import datetime

ip_address = request.urlopen('https://ident.me').read().decode('utf8')
response = request.urlopen(f'https://ipapi.co/{ip_address}/json/') #.json()

body = response.read()
decoded_body = body.decode("utf-8")

data = json.loads(decoded_body)

now = datetime.now()
current_time = now.strftime("%Y.%m.%d %H:%M:%S")

# data to be sent to api
stats = {'datetime':current_time,
        'ip_address':ip_address,
        'city':data["city"],
        #'region':data["region"],
        'country_name':data["country_name"],
        'other': ', '.join(list(IN[0]))
        }

url = "https://artomczak.pythonanywhere.com/" + "ecobim_stats"

stats = parse.urlencode(stats).encode()
req =  request.Request(url, data=stats) # this will make the method "POST"
resp = request.urlopen(req)

OUT = 'Sent.'
#OUT = "Usage stats: " + ", ".join( [current_time, ip_address, data["city"], data["country_name"]] )