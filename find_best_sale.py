# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:10:50 2019

@author: Apoorva
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
s=input("name of item to search")
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
search_input_box = driver.find_element_by_name("q")
search_input_box.send_keys(s)
search_input_box.send_keys(Keys.RETURN)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.snapdeal.com/")
search_input_box = driver.find_element_by_id("inputValEnter")
search_input_box.send_keys(s)
search_input_box.send_keys(Keys.RETURN)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.amazon.in/")
search_input_box = driver.find_element_by_id("twotabsearchtextbox")
search_input_box.send_keys(s)
search_input_box.send_keys(Keys.RETURN)
import time
time.sleep(10)
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
