# Setup
## Create Virtual Environment and activate it:
```
sudo apt install python3.8-venv   
python3 -m venv ./.env   
source ./.env/bin/activate  
```

## Install Requirements
`sudo apt-get install scrot python3-tk python3-dev -y  `
and then
`pip install -r requirements.txt`

Once done add ca-certificate-*.cer files to google chrome to avoid ssl warnings.


In case you get errors after installing requirements read the following(if not ignore it)
## The following packages have to be installed
#### Install Selenium:
```pip install selenium webdriver-manager```

####  Install pyautogui:
```
python3 -m pip install opencv_python
python3 -m pip install pyautogui
```

####  Setup browsermob-proxy::
Download package from :: http://bmp.lightbody.net/  
Extract to folder, add path in environments file.
```
pip install browsermob-proxy
```
