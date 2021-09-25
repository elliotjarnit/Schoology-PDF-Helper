import requests
from PIL import Image
from requests_oauthlib import OAuth1
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from colorama import Fore, Style, init
import img2pdf
from PIL import Image
from selenium import webdriver
import os
from sys import platform
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear():
    print("\n" * 100)


def ifStatement(prompt, answers):
    while True:
        answer = input(prompt)
        if answer in answers:
            return answer
        else:
            print("\nThat is not a valid answer")


def ifStatementNum(prompt):
    while True:
        answer = input(prompt)
        if answer.isdigit():
            return answer
        else:
            print("\nThat is not a valid answer")


def printError(message, newline=False):
    if newline == True:
        print("\n" + Fore.RED + "[ERROR]" + Style.RESET_ALL + " " + message)
    else:
        print(Fore.RED + "[ERROR]" + Style.RESET_ALL + " " + message)


def makeRequest(method, site, oauth, headers="None"):
    try:
        if headers == "None":
            if method == "get":
                answer = requests.get(url=site, auth=oauth, headers=headers)
            elif method == "post":
                answer = requests.post(url=site, auth=oauth, headers=headers)
            elif method == "put":
                answer = requests.put(url=site, auth=oauth, headers=headers)
            else:
                pass
        else:
            if method == "get":
                answer = requests.get(url=site, auth=oauth)
            elif method == "post":
                answer = requests.post(url=site, auth=oauth)
            elif method == "put":
                answer = requests.put(url=site, auth=oauth)
            else:
                pass
        return answer
    except:
        printError("No internet connection", True)
        exit()