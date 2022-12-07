# Web UI load time checker
This program was writen with a very specific use case in mind. To check the load timing of web components that take too long to load. Hence this might not be suitable for pages that load in milliseconds.

## Setup
Check Setup.md

## How to
### Step 1: 
First load the page that you want to test. And take a screenshot of the page and save it to **sample_images** folder. Note instead of full page you can take a screenshot of a particular component also.

### Step 2: 
copy *lifecycle.sample.py* and save it as *lifecycle.py*. The program will navigate you to the  **initialURL** set in .environment file. You can add extra functionality like login or page navigation by adding it under **afterInit** function in *lifecycle.py*  
sample usage  
```
def afterInit(driver):
    loginUser='YOUR_USER_NAME'
    loginPassword='YOUR_PASSWORD'
    unameField = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
    unameField.send_keys(loginUser)
    passField = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    passField.send_keys(loginPassword)
    passField.send_keys(Keys.RETURN)
```
Instead of doing this you can manually log in once the page loads.

### Step 3:  
copy *.environment.sample* and save it as *.environment*. further details about the variables are given in the *.environment.sample* file

### Step 4:
You can now run the code with
```python3 main.py```

## Versions
* Python 3.8.10
* Java(openjdk) 11.0.17