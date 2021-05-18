from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
import time
import subprocess
import webbrowser

subprocess.Popen() #to open discord 
time.sleep(8)

driver = webdriver.Firefox(executable_path=r'C:\\Users\\user\\Desktop\\Python Automation\\geckodriver.exe')
driver.maximize_window()

meetLink = "" #enter meet room link

stackOverflowLink = "https://stackoverflow.com/users/login"
driver.get(stackOverflowLink)
try:
    login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "s-btn__google")))
    time.sleep(2)
    login_btn.click()
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
    time.sleep(2)
    email_input.send_keys() #enter Gmail ID
    email_input.send_keys(Keys.ENTER)
    pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    time.sleep(2)
    pass_input.send_keys() #enter Password
    pass_input.send_keys(Keys.ENTER)
    
except Exception as e:
    print(e)
time.sleep(2)

driver.get(meetLink)
webbrowser.open() #to open any site on default browser
time.sleep(5)


try:
       
    dismiss = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")))
    dismiss.click()
        
    alert = Alert(driver)
    alert.dismiss()
        
    mic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div["
                       "1]/div/div[4]/div[1]/div/div/div")))
    
    mic.click()
except Exception as e:
    print(e)
    
time.sleep(5)
    

try:
    join_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")))
    join_now.click()
except Exception as e:
        print(e) 
        
time.sleep(1000)  
