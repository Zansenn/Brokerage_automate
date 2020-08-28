import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\nazse\\chromedriver\\chromedriver.exe",)

def site_login():
    driver.get("https://herefordshirebrokerage.care-for-it.com/index.php/login")
    userID = driver.find_element_by_name("txtEmail")
    userID.send_keys("email_address_here")
    driver.find_element_by_name("txtPassword").send_keys("passwordhere")
    driver.find_element_by_id("login_button").click()

site_login()

def find_postcode():
  select_table = driver.find_element_by_css_selector('.col-sm-6:nth-child(2)')
  select_table.find_element_by_partial_link_text("HR2").click()
 
find_postcode()
