from core.output_manager import Run_Tool
from tools.hasher import hasher
from tools.ip_finder import IP_Finder
from tools.password_generator import password_generator
from tools.base64_tool import Base64_Tool
from tools.dns_lookup import DNS_Lookup
from tools.ping import Ping
from tools.port_scanner import Port_Scanner
from tools.banner_grabber import Banner_Grabber
from tools.whois_lookup import WHOIS_Lookup
from tools.ip_geolocation import IP_Geolocation
from tools.http_headers import HTTP_Headers_Analyzer
from tools.dns_records import DNS_Record_Enumerator

def Menu():

    while True:

        print("""
        Enter 1 to hash your text
        Enter 2 to see your IP
        Enter 3 to generate a password
        Enter 4 to use Base64
        Enter 5 to DNS Lookup
        Enter 6 to Ping a host
        Enter 7 to scan ports
        Enter 8 to Banner Grab
        Enter 9 to WHOIS Lookup
        Enter 10 to IP Geolocation
        Enter 11 to HTTP Headers Analyzer
        Enter 12 to DNS Record Enumerator
        Enter B to go back
        Enter E to exit
        """)

        tool_number = input("Enter your tool number: ")

        if tool_number.lower() == "b":
            return "back"

        if tool_number.lower() == "e" or tool_number.lower() == "exit":
            return "exit"

        if tool_number == "1":

            result = Run_Tool("Hash", hasher)

            if result == "exit":
                return "exit"

        elif tool_number == "2":

            result = Run_Tool("IP_Finder", IP_Finder)

            if result == "exit":
                return "exit"
        elif tool_number == "3":

            result = Run_Tool("Password_Generator", password_generator)

            if result == "exit":
                return "exit"

        elif tool_number == "4":

            result = Run_Tool("Base64", Base64_Tool)

            if result == "exit":
                return "exit"

        elif tool_number == "5":

            result = Run_Tool("DNS_Lookup", DNS_Lookup)

            if result == "exit":
                return "exit"

        elif tool_number == "6":

            result = Run_Tool("Ping", Ping)

            if result == "exit":
                return "exit"

        elif tool_number == "7":

            result = Run_Tool("Port_Scanner", Port_Scanner)

            if result == "exit":
                return "exit"

        elif tool_number == "8":

            result = Run_Tool("Banner_Grabber", Banner_Grabber)

            if result == "exit":
                return "exit"

        elif tool_number == "9":

            result = Run_Tool("WHOIS_Lookup", WHOIS_Lookup)

            if result == "exit":
                return "exit"

        elif tool_number == "10":

            result = Run_Tool("IP_Geolocation", IP_Geolocation)

            if result == "exit":
                return "exit"

        elif tool_number == "11":

            result = Run_Tool("HTTP_Headers_Analyzer", HTTP_Headers_Analyzer)

            if result == "exit":
                return "exit"

        elif tool_number == "12":
            result = Run_Tool(
                "DNS_Record_Enumerator",
                DNS_Record_Enumerator
    )

            if result == "exit":
                return "exit"
