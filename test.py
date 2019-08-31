# # from common import browsrStart
# #
# # # ！！！引用报错
# # browsrStart.browser_start()
# # # cappic.capture_pic(driver)
# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get("https://www.xueqingyun.com/user/sign-in/login")
# driver.find_element(By.ID, "loginform-identity").send_keys("boweifengbj")
# driver.find_element(By.ID, "loginform-password").send_keys('boweifeng')
# driver.find_element(By.NAME, "login-button").click()
# time.sleep(3)
# drop_down = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
# ActionChains(driver).click(drop_down).
# drop_down.send_keys(Keys.DOWN)
# drop_down.send_keys(Keys.DOWN)
# drop_down.send_keys(Keys.DOWN)
# drop_down.send_keys(Keys.DOWN)
# drop_down.send_keys(Keys.DOWN)
# drop_down.send_keys(Keys.ENTER)
# # Select(dropdown).select_by_visible_text("注销")
# # dropdown.find_element(By.CLASS_NAME, "#w8 > li:nth-child(5) > a").click()
# # driver.find_element(By.CLASS_NAME, "#w8 > li:nth-child(5) > a").click()
# # driver.find_element(By.XPATH, "//*[@id='w8']/li[5]/a").click()
# time.sleep(3)
