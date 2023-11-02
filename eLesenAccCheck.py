# import module
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# browser instance
options = Options()
options.add_argument("--headless=new")
browser = webdriver.Firefox(options=options)

# target URL
browser.get('https://portal.digitalsabah.gov.my/')
time.sleep(3)

# admin login
penjawat_awam = browser.find_element("xpath", '//*[@id="dgd"]')
penjawat_awam.click()
time.sleep(1)

myKad = '880621125761' # your own ga'damn ic
pswd = input('enter password: ')  # your own ga'daman password

ic = browser.find_element("xpath", '//*[@id="dgdlogin"]')
klaluan = browser.find_element("xpath", '//*[@id="dgdpassword"]')

ic.send_keys(myKad)
klaluan.send_keys(pswd)

# execute login 
log_masuk = browser.find_element("xpath", '//*[@id="DGDLogin"]')
log_masuk.click()

# let the page load : adjust depends on load speed
time.sleep(7)

konfigurasi = browser.find_element("xpath", '/html/body/div[2]/header/ul[1]/div/nav/ul[2]/li[2]/a/div/span')  
konfigurasi.click()
time.sleep(1)
akaun_pengguna = browser.find_element("xpath", '/html/body/div[2]/header/ul[1]/div/nav/ul[2]/li[2]/ul/li[3]/a')
akaun_pengguna.click()

# wait for page to load again yang pling last
time.sleep(13)

# search for ic
search_box = browser.find_element("xpath", '/html/body/div[3]/div[5]/div[1]/div[2]/div/div[3]/div/div/div/div[1]/div/div[2]/div/label/input')

# customer ic
customer_ic = input('Please enter customer IC number : ')

#customer_ic = '800930125855' #'911025125537' # the ic yang kau mau search [debugger]
search_box.send_keys(customer_ic)

#print('Do you want to make changes (yes/no) ? : ')
user_input = ''

while user_input not in ('yes', 'no'):
    
    user_input = input('Do you want to make changes (yes/no) ? : ')
    
    if user_input.lower() == 'yes':
        print('yes')
        # ask for ic; then get the xpath of the profile email text field
        view_btn = browser.find_element("xpath", '/html/body/div[3]/div[5]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[2]/button')
        view_btn.click()
        # wait for it......
        time.sleep(2)
        
        name_field = browser.find_element("xpath", '//*[@id="PersonName"]')
        ic_field = browser.find_element("xpath", '//*[@id="IdentityNo"]')
        phone_field = browser.find_element("xpath", '//*[@id="PersonContactNo"]')
        email_field = browser.find_element("xpath", '//*[@id="PersonEmail"]')

        current_name = name_field.get_attribute('value')
        current_ic = ic_field.get_attribute('value')
        current_phone = phone_field.get_attribute('value') 
        current_email = email_field.get_attribute('value')
        
        edit_input = ''
        while edit_input not in ('y', 'n'):
            edit_input = input('Do you want to keep edit (y)/(n) ? : ')
            if edit_input.lower() == 'y':
                print(current_name, current_ic, current_phone, current_email)
                #break
                print(browser.find_element(By.XPATH, '//*[@id="PersonEmail"]').text)
            if edit_input.lower() == 'n':
                print(current_name, current_ic)
            else:
                print('please type y or n')
    if user_input.lower() == 'no':
        print('no')
        # end session / back to home portal
        #break
    else:
        print('get me back to senarai')
        doubleback = browser.find_element("xpath", '//*[@id="Back"]')
        doubleback.click()
        #user_input = input('Do you want to make changes (yes/no) ? : ')








