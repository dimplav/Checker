#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
web_mta = ""
def listajLinkove():
    global web_mta
    #web_mta = "http://www.matf.bg.ac.rs/p/jelena/vest/6779/unm-obavestenje/"
    response = requests.get(web_mta)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    lista = []
    for x in soup.findAll('a'):
        lista.append(x)
    return lista
