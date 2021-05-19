#!/usr/bin/env python3

import requests
import json
import os
import sys
from pprint import pprint
try:
    import subprocess
except:
    print("Bitte das Modul subprocess installieren mit \"pip3 install subprocess\"")
    sys.exit(1)
try:
    import smtplib
except:
    print("Bitte das Modul smtplib installieren mit \"pip3 install smtplib\"")
    sys.exit(1)

try:
    import config
except:
    print("Bitte das Modul config installieren mit \"pip3 install config\"")
    sys.exit(1)



def checkAvailability():
    url = "https://impfterminradar.de/api/vaccinations/availability"
    head = {
        "Accept": "application/json"
    }


    with open(os.path.dirname(os.path.realpath(__file__)) + "/Impfzentren.json") as f:
        data = json.load(f)

    r = requests.patch(url, json=data, headers=head)
    result = r.json()
    # pprint(result)

    available = [x for x in result if x["Available"] ]

    print("Vefügbar:")
    pprint(available)
    return available


def getInformationToSlug(slug):
    kommando = os.path.dirname(os.path.realpath(__file__)) + "/parser " + str(slug)
    information = subprocess.check_output(kommando, shell=True, encoding='utf-8')
    return(information)



def sendmail(available, information):
    gmail_user = config.username
    gmail_password = config.password
    sent_from = gmail_user
    to = gmail_user
    subject = "Impftermin"
    body = str(information) + "\n\n" + str(available)

    email_text = "From: " + str(sent_from) + "\nTo: " + str(to) + "\nSubject: " + str(subject) + "\n" +  str(body)
    print(email_text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print("E-Mail wurde verschickt")
    except Exception as e:
        print("Etwas ist schiefgelaufen: " + str(e))


available = checkAvailability()

if available != []:
    slugs = [available["Slug"] for available in available]
    # counter=0
    # for slug in slugs:
    #     slugs[counter] = slug.split("_", 1)[0] + "_" + slug.split("_", 2)[1]
    #     counter+=1
    slugs = list(dict.fromkeys(slugs)) #Remove duplicates
    information = ""
    for slug in slugs:
        information += getInformationToSlug(slug) + "\n\n"

    sendmail(available, information)
else:
    print("Es sind keine Termine verfügbar")