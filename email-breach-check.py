#!/usr/bin/python
import requests
import argparse
import sys
from time import sleep
from datetime import datetime
from termcolor import colored
import re

parser = argparse.ArgumentParser(description='This script injests a file containing email addresses to verify if they have been a part of a previous breach!')
parser.add_argument('-inputfile', help='Path to the file containing email addresses, one per line.')
parser.add_argument('-email', help='an email address to check for breaches.')
defaultdir = f"email-breach-check-results-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
parser.add_argument('-outputfile', help='Path to where you would like the output to be stored.', default=defaultdir)

args = parser.parse_args()

def check_email_breach(email):
    url = f"https://leakcheck.io/api/public?check={email}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        sleep(3)
        return response.json()
    except requests.RequestException as e:
        print(colored(f"Error fetching data: {e}", "yellow"))
        sys.exit(1)

def display_breach_info(email, data, write:bool=True):
    if not data['success']:
        print(colored(f"No breaches found for: {email}", "green"))
        if write:
            write_file(f"No breaches found for: {email}")
        return
    names = []
    for item in data['sources']:
        names.append(item['name'])
    # print(colored(f"The email address, '{email}', has been a part of compromises on the following domains: {names}", "red"))
    print(colored(f"{email} : {names}", "red"))
    if write:
        write_file(f"The email address, '{email}', has been a part of compromises on the following domains: {names}")
    
def open_file(path):
    with open(path) as file:
        raw = file.readlines()
    emails = []
    for item in raw:
        is_valid = bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', item))
        if is_valid:
            emails.append(str(item).strip())
        else:
            continue
    return emails

def write_file(data):
    with open(args.outputfile, "a") as file:
        file.write(data)

if args.email:
    email = args.email.strip()
    response = check_email_breach(email)
    display_breach_info(email, response, write=False)

if args.inputfile:
    emails = open_file(args.inputfile)
    for email in emails:
        response = check_email_breach(email)
        display_breach_info(email, response)
    print(f"\nCheck out the following file for the results: {args.outputfile}")