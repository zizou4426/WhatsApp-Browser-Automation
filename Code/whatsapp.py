from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time, os 


options = webdriver.ChromeOptions()

# Replace --user-data-dir="C:/Users/Chaitanya V/AppData/Local/Google/Chrome/User Data" with your path
options.add_argument("--user-data-dir=C:/Users/chaitanya.vankadaru/AppData/Local/Google/Chrome/User Data")

# Replace below path with the executable path to chromedriver in your computer ( You have to download version specific chromedriver) 
driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe', chrome_options=options)

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Recipient Name' with the name of your friend or the name of a group 
x_arg= '//*[contains(@title,"Zuckerberg")]'
# x_arg= '//*[contains(@title,"Recipient Name")]'

# Replace the below string with your own message 
string = "So, how's everything going on?"
# string = "Your Message"

group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 

group_title.click() 
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
for i in range(1): # Increase the range to send continuous messages range(n) => 'n' messages
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) # Increase the sleep timer if you want the time interval between messages.

delete_paths = ['../selenium/chrome_profile/Local State',
                '../selenium/chrome_profile/Default/Preferences']
for delete_path in delete_paths:
    if os.path.exists(delete_path):
        os.remove(delete_path)
  
# This code is solely to be used for academic purposes only. I'm not responsible if you get into trouble or get banned due to this.

# Note: This code won't work if your input friend's name/group title is in archieved chats/or if they aren't on homescreen of WhatsApp.
