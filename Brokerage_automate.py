import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\nazse\\chromedriver\\chromedriver.exe",)

user_name = input(" what's your email address")
pass_word = input("what's your password")

def site_login():
  driver.get("https://herefordshirebrokerage.care-for-it.com/index.php/login")
  userID = driver.find_element_by_name("txtEmail")
  userID.send_keys(user_name)
  driver.find_element_by_name("txtPassword").send_keys(pass_word)
  driver.find_element_by_id("login_button").click()

site_login()

def find_postcode(postcode):
  postcode = str(postcode)
  select_table = driver.find_element_by_css_selector('.col-sm-6:nth-child(2)')
  select_table.find_element_by_partial_link_text(postcode).click()


#find_postcode('HR2')