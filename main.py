import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from browsermobproxy import Server
import pyautogui
import datetime
import json
from dotenv import load_dotenv
from pathlib import Path
from support.getHtmlData import saveHtmlReport
from support.saveSnap import saveSnap
from support.initialize import initialize
from lifecycle import afterInit, beforeInit, onEnd

load_dotenv(dotenv_path='.environment')
projectName=os.getenv('projectName')
initialURL=os.getenv('initialURL')
#image must be placed inside sample_images folder
imageToCompareWith=os.getenv('imageToCompareWith')
urlPathToMonitor=os.getenv('urlPathToMonitor')
maxWaitTime=int(os.getenv('maxWaitTime'))
## to get request data
browserMobProxyPath=os.getenv('browserMobProxyPath')
browserMobProxyPort=int(os.getenv('browserMobProxyPort'))

## for report
reportedRequests=os.getenv('reportedRequests')
filterReqUrl=os.getenv('filterReqUrl')

####################################
beforeInit()
## Initialize folders ##
initialize()
####
server = Server(browserMobProxyPath,options={'port': browserMobProxyPort})
server.start()
proxy = server.create_proxy(params={'trustAllServers':'true'})
options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--proxy-server={}".format(proxy.proxy))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(initialURL)
## Stuff like login or initial processing here
afterInit(driver)
#######
proxy.new_har(projectName)
WebDriverWait(driver, maxWaitTime).until(lambda driver: (urlPathToMonitor in driver.current_url))
saveSnap(driver,f'./tmp/{projectName.replace(" ", "_")}_initial.png',0)
start_time = datetime.datetime.now()
imgFound= None 
while imgFound is None:
    # NOTE::increasing the confidence would require clearer images
    imgFound=pyautogui.locateOnScreen('./sample_images/'+imageToCompareWith, confidence=0.7)
end_time = datetime.datetime.now()
delta = end_time - start_time
saveSnap(driver,f'./tmp/{projectName.replace(" ", "_")}_final.png',0)
saveHtmlReport(proxy.har,reportedRequests,filterReqUrl,delta,imageToCompareWith,projectName)
f = open("./reports/"+projectName.replace(" ", "_")+"_full_har.json", "w")
f.write(json.dumps(proxy.har))
f.close()
onEnd("reports/"+projectName.replace(" ", "_")+".html")
driver.close()
server.stop()
