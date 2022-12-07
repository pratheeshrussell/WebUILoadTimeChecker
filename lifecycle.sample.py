import os
import webbrowser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# copy this file as lifecycle.py
def beforeInit():
    # this function will run before selenium or anything else is initialized
    print('Before init hook')

def afterInit(driver):
    # this will run once page loads - you can run actions like
    # login or page navigation from here
    print('After init hook')

def onEnd(reportPath):
     # this will run after report has been generated
     print('Report saved to '+ reportPath)
     webbrowser.open('file://' + os.path.realpath(reportPath))