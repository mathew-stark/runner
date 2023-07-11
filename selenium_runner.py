from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import random

class runner:
    def __init__(self):
        print("started")
    def run(self,url,text):
        initial_url = url
        options = Options()
        options.add_argument("--disable-gpu")
        driver = webdriver.Remote(command_executor="http://192.168.1.13:4444/wd/hub", options=options)
        driver.get(url)
        driver.implicitly_wait(5)
        final_url = driver.current_url
        element = driver.find_elements(By.CLASS_NAME, "languages")
        for i in element:
            if text in i.get_attribute("data-value").lower():
                print("found")
                return True
            # if initial_url != final_url:
            #     print("An automatic redirect occurred from", initial_url, "to", final_url)
            # else:
            #     print("No automatic redirect occurred.")
        driver.quit()



test = runner()
while(True):
    try:
        x = test.run("https://in.bookmyshow.com/buytickets/oppenheimer-chennai/movie-chen-ET00347867-MT/20230721","imax")
        if x:
            requests.get("https://tinyurl.com/2ovv4ttq/notify/?text=Imax bookings are open in luxe")
    except:
        time.sleep(120)
        requests.get("https://tinyurl.com/2ovv4ttq/notify/?text=exception")
    time.sleep(random.randint(300,360))


