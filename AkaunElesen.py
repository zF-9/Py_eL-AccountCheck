# import module
import time
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
 
# the target website 
url = "https://portal.digitalsabah.gov.my/"  #https://portal.digitalsabah.gov.my/
 
# the interface for turning on headless mode 
options = Options() 
options.add_argument("-headless") 
 
# using Firefox headless webdriver to secure connection to Firefox 
with webdriver.Firefox(options=options) as browser: 
	# opening the target website in the browser 
	browser.get(url) 
 
	#printing the target website url and title 
	print(browser.current_url) # https://scrapeme.live/shop/ 
	print(browser.title) # Products - ScrapeMe
	#browser.get_screenshot_as_file("screenshot.png")
	
	time.sleep(3)

# admin login
penjawat_awam = browser.find_element("xpath", '//*[@id="dgd"]')
penjawat_awam.click()
time.sleep(1)

myKad = '880621125761' # your own ga'damn ic
pswd = '#'  # your own ga'daman password

ic = browser.find_element("xpath", '//*[@id="dgdlogin"]')
klaluan = browser.find_element("xpath", '//*[@id="dgdpassword"]')

ic.send_keys(myKad)
klaluan.send_keys(pswd)

# execute login 
log_masuk = browser.find_element("xpath", '//*[@id="DGDLogin"]')
log_masuk.click()
