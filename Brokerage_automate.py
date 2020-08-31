import selenium
import bs4
import var1 

from var1 import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#specifies chrome and driver location 
#options = Options()
#options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\nazse\\chromedriver\\chromedriver.exe",)

#opens brokerage site and logs in
def site_login():
  driver.get("https://herefordshirebrokerage.care-for-it.com/index.php/login")
  userID = driver.find_element_by_name("txtEmail")
  userID.send_keys(user_name)
  driver.find_element_by_name("txtPassword").send_keys(pass_word)
  driver.find_element_by_id("login_button").click()

#finds a postcode in a webpage (not in beautiful soup)
def find_postcode(postcode):
  postcode = str(postcode)
  select_table = driver.find_element_by_css_selector('.col-sm-6:nth-child(2)')
  select_table.find_element_by_partial_link_text(postcode).click()


#First changes to new tab then clicks the respond button
#then writes in the comments popup  box that appears 
def request_package():
  driver.switch_to_window(driver.window_handles[1])
  driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/ul/li/form[1]/button/i").click()
  driver.find_element_by_xpath("/html/body/div[5]/div[2]/form/div/textarea").send_keys("Ready to start asap")

#specifies the parser and the soup
def cook_soup():
  soup = BeautifulSoup(driver.page_source, features="html.parser")

#uncomment below if you want the user to be prompted to enter their user name
#input(" what's your email address")
#input("what's your password")

if __name__ == "__main__":

  options = Options()
  options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
  driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\nazse\\chromedriver\\chromedriver.exe",)

#site_login()
#cook_soup()
#find_postcode('HR2')
#change_tab()
#driver.implicitly_wait(5)
#request_package()
#driver.implicitly_wait(15)
#write_response()