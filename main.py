#Read the README.md file for some information before getting started. 

# Line 4 - line 13 is the setup to get on the Instagram Page
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)
driver.get("https://www.instagram.com/")
#since the browser closes right after the program is done executing steps, I use time.sleep() to keep the browser open a certain amount of time, depending on the number I input between the parantheses. Side Note: the number I input is in seconds. 
time.sleep(3)

#IMPORTANT - If you have already logged into Instagram before, you can simply use line 30 to line 32 and remove line 18 to line 28 as well as line 34 to line 51. Make sure to remove the hashtags from line 28 to 30 if you are doing this step. If you are not doing this step, you can ignore this and carry on. :D 


#Input your username, email, or phone number into line 19, between the quotations marks :D
driver.find_element("name", "username").send_keys(" ")
time.sleep(3)

#Repeat line 18 but input your password into line 23
driver.find_element("name", "password").send_keys(" ")
time.sleep(3)

login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")     
login.click()
time.sleep(10)
 
#continue_as_username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/div/div[1]/button/span")
#continue_as_username.click()
#time.sleep(10)

backup_code_link = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/button")
backup_code_link.click()
time.sleep(10)
#Grab a Backup Code and input it into line 36, between the quotation marks
driver.find_element("name", "verificationCode").send_keys(" ")
time.sleep(10)

confirm = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button")
confirm.click()
time.sleep(10)

not_now_to_save_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
not_now_to_save_login.click()
time.sleep(10)

no_to_notification = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
no_to_notification.click()
time.sleep(15)

direct_messages = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
direct_messages.click()
time.sleep(10)

direct_message_from_sender = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[2]/div/div/span[1]/span")
direct_message_from_sender.click()
time.sleep(10)

message_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hi, this is Andy's bot, Bob. Andy is currently not available. He is either coding, sleeping, or away from the screen. Please text him back in an hour or wait for him to see your message.")
time.sleep(10)

send_message = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
send_message.click()
time.sleep(10)

