from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
while True:
    try:
        driver.get("https://fan.at/news/6390ebd417bfe44ec5da4f81")
        sleep(2)

        driver.find_element("xpath", '//*[@id="cookiescript_accept"]').click()

        sleep(2)

        driver.find_element("xpath", '//*[@id="6390ebd117bfe44ec5da4f7a"]/div/app-tab-group/app-tab/div/app-voting-section/div/app-voting-item[3]/div/div').click()

        sleep(2)

        driver.find_element("xpath", '//*[@id="6390ebd117bfe44ec5da4f7a"]/app-voting-navigation/div/div/button/span[1]').click()

        print("done")
    except:
        print("error")
        continue
