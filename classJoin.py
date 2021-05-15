





# from selenium import webdriver

# driver = webdriver.Firefox(executable_path=r'C:\\Users\\user\\Desktop\\Python Automation\\geckodriver.exe')

# driver.get('https://accounts.google.com/')
# enterEmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
# enterEmail.send_keys('deepakpattnayak2013@gmail.com')
# searchButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
# searchButton.click()

# def sign_in_gmail():
#     """
#     Login into gmail via stackoverflow
#     :return: None
#     """
#     print("Logging in into Gmail account...")
#     url = "https://stackoverflow.com/users/login"
#     driver.get(url)
#     try:
#         login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "s-btn__google")))
#         time.sleep(2)
#         login_btn.click()
#         email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
#         time.sleep(2)
#         email_input.send_keys("deepakpattnayak2013@gmail.com")
#         email_input.send_keys(Keys.ENTER)
#         pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
#         time.sleep(2)
#         pass_input.send_keys("gofuckyourself")
#         pass_input.send_keys(Keys.ENTER)
#         print("Logged in into Gmail account")
#     except Exception as e:
#         print(e)


# sign_in_gmail()


# import webbrowser
# from selenium import webdriver
# webbrowser.open('https://meet.google.com/fxf-cwxo-tui', new=2)
# driver = webdriver
# camera = driver.find_element_by_xpath()

# import subprocess
# subprocess.Popen('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')



# from typing import KeysView
# from selenium.webdriver.support.ui import WebDriverWait

# # Github credentials
# username = "deepakpattnayak2013@gmail.com"
# password = "password"



# # initialize the Chrome driver
# driver.find_element_by_xpath('//*[@id="identifierId"]').sendKeys(Keys.CONTROL +"t");
# # driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL +"t");
# # head to github login page
# driver.get('https://accounts.google.com/')
# # find username/email field and send the username itself to the input field
# driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
# # find password input field and insert password as well
# # driver.find_element_by_id("password").send_keys(password)
# # click login button
# driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

# # wait the ready state to be complete
# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# error_message = "Incorrect username or password."
# # get the errors (if there are)
# errors = driver.find_elements_by_class_name("flash-error")
# # print the errors optionally
# # for e in errors:
# #     print(e.text)
# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")
    
# driver.close


# # from selenium import webdriver



# # driver = webdriver.Chrome()
# # driver.get('https://accounts.google.com/')
# # enterEmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
# # enterEmail.send_keys('deepakpattnayak2013@gmail.com')
# # searchButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
# # searchButton.click()


# # # # searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# # # # 
# # # 
# # # searchButton.click()
# # # # # import webbrowser
# # # # # webbrowser.open('https://meet.google.com/fxf-cwxo-tui', new = 2)

# # # import time 
# # # from selenium import webdriver
 
# # # # Here Chrome  will be used 
# # # driver = webdriver.Chrome()
 
# # # # URL of website
# # # url = "https://www.geeksforgeeks.org/"
 
# # # # Opening the website
# # # driver.get(url)
 
# # # # getting the button by class name
# # # button = driver.find_element_by_class_name("slide-out-btn")
 
# # # # clicking on the button
# # # button.click()
