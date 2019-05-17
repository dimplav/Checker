#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
web_mta = ""
tag = 'a'
def listajLinkove():
    global web_mta
    global tag
    #web_mta = "http://www.matf.bg.ac.rs/p/jelena/vest/6779/unm-obavestenje/"
    response = requests.get(web_mta)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")

    lista = []
    for x in soup.findAll(tag):
        lista.append(x)
    print(lista)
    return lista