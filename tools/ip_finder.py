import hashlib
import urllib.request
import urllib.error
import socket
import secrets
import string
import base64
import time
import ssl
import random
import whois
import json
import os
from datetime import datetime
from contextlib import redirect_stdout
import io
import sys
import dns.resolver
import socket
import ssl
import time

def IP_Finder():

    while True:

        IP_typ = input(
            "Enter 1/l for Local IP and 2/p for Public IP "
            "(B = back, E = exit): "
        )

        if IP_typ.lower() == "b":
            return "back"

        if IP_typ.lower() == "e" or IP_typ.lower() == "exit":
            return "exit"

        if IP_typ == "1" or IP_typ.lower() == "l":

            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)

            print("Your Local IP:", ip)

        elif IP_typ == "2" or IP_typ.lower() == "p":

            ip = urllib.request.urlopen(
                "https://api.ipify.org"
            ).read().decode()

            print("Your Public IP:", ip)
