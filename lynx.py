import requests as rq 
import os
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="enable debugging info", action=("store_true"))
parser.add_argument("target", type=str, help="Target to search")
args = parser.parse_args() 

if args.debug:
    print("debugging info enabled")
    debug = True
else:
    debug = False
if args.target:
    if debug == True: print("debug: target set to " + args.target)


brave_key=os.getenv("BRAVE_KEY")
if debug == True: 
    if brave_key:
        print("debug: key found")
    else:
        print("debug: no brave search API key found, set 'BRAVE_KEY' using the export command in bash, or set in windows cmd.")

print("\n\n\033[33m+-----------------------------------------------+\033[0m")
print("\033[1;33m|                                               |\033[0m")
print("\033[1;33m|      LYNX - Information Gathering Tool        |\033[0m")
print("\033[1;33m|\033[0m"+"                 Version: Alpha"+"\033[1;33m                |\033[0m")
print("\033[1;33m|                                               |\033[0m")
print("\033[33m+-----------------------------------------------+\033[0m\n\n")

print("Target: " + args.target)
print("[~] Searching for publicly available information...")

url = "https://api.search.brave.com/res/v1/llm/context"

params = {
    "q": args.target
}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "X-Subscription-Token": brave_key
}

response = rq.get(url, params=params, headers=headers)
