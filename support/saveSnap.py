from time import sleep

def saveSnap(driver,path,delay=1):
    driver.save_screenshot(path)