from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

my_email = EMAIL
my_password = PASSWORD

chrome_driver_path = "C:/Users/Dawid/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")

time.sleep(2)

#login button
log_in = driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()

time.sleep(2)

#clicking login by facebook
login_by_facebook = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_by_facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

#switching to login window
driver.switch_to.window(fb_login_window)

#logging by facebook
email = driver.find_element(By.NAME, "email")
email.send_keys(my_email)

password = driver.find_element(By.NAME, "pass")
password.send_keys(my_password)

time.sleep(0.5)

password.send_keys(Keys.ENTER)

#switching back to main_window
driver.switch_to.window(base_window)

#wait for page to load
time.sleep(5)

#going through all pop-ups
location = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]')
location.click()

time.sleep(1)

notifications = driver.find_element(By.XPATH, '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[2]')
notifications.click()

time.sleep(1)

cookies = driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

time.sleep(5)

#counter because first like have div[4] other have div[5]
counter = 0
for n in range(100):
    time.sleep(1)

    #giving likes
    try:
        if counter == 0:
            driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span').click()
            counter += 1

        else:
            driver.find_element(By.XPATH, '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span').click()

    #closing the match pop-up
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, '//*[@id="q1359156289"]/div/div/div[1]/div/div[4]/button')
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
