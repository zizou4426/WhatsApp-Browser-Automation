# Importing libraries
# If you don't have selenium, install it using "pip3 install selenium" in your command prompt or powershell

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 


options = webdriver.ChromeOptions()

# Replace --user-data-dir="C:/Users/Chaitanya V/AppData/Local/Google/Chrome/User Data" with your path
options.add_argument("--user-data-dir=C:/Users/Chaitanya V/AppData/Local/Google/Chrome/User Data")

# Replace below path with the executable path to chromedriver in your computer ( You have to download version specific chromedriver) 
driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe', chrome_options=options)

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend or the name of a group 
target = '"Zuckerberg"'
#target = '"Friend Name/Group Title"'

# Replace the below string with your own message 
string = "Data is money, right?"
# string = "Your Message"

x_arg = '//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div[1]/span/span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
for i in range(5): # Increase the range to send continuous messages range(n) implies n messages
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) 
  
  
# This code is solely to be used for academic purposesonly. I'm not responsible if you get banned due to this.

# Note: This code won't work if your entered friend name/group title is in archieved chats.
