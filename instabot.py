


# Author  : DIVS TECH

from selenium import webdriver
from time import sleep

class InstaBot:
	def __init__(self,username,password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.instagram.com")
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(password)		
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
			.click()
		self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
			.click()
		sleep(12)
InstaBot('yourusername','yourpassword')#Never Disclose it..




