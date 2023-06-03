""" 
make sure u have the necessary browser drivers installed and added to environment paths in your system
--------------------------------&---------------------------------
Make Sure to run these commands in CMD before running this program
pip install selenium
pip install pyautogui
pip install schedule
"""
from selenium import webdriver
import pyautogui as chirag
from time import sleep
import schedule
def join():
    chrome_options = webdriver.ChromeOptions()              #-----------changing the options in chrome browser that is going to get open
    prefs = {"profile.default_content_setting_values.notifications": 1,   #---------allowing the notifications (1 for allow and 2 for deny)
             "profile.default_content_setting_values.media_stream_mic": 1,#---------allowing the microphone (1 for allow and 2 for deny)
             "profile.default_content_setting_values.media_stream_camera": 1,#---------allowing the camera (1 for allow and 2 for deny)
             "profile.default_content_setting_values.geolocation": 2}#---------allowing the location using GPS (1 for allow and 2 for deny)
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://accounts.google.com/') # ------will direct the browser to get to site.
    sleep(10)#--------------used to delay execution of code for specific time
    driver.maximize_window() #----- will maximize the window
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('#')   #----enter the EMAIL ID
    chirag.press('enter')
    sleep(15)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("#") #----enter the EMAIL ID Password
    chirag.press('enter')
    sleep(15)
    driver.get("https://meet.google.com/yrf-feui-ykz") #------will direct the browser to get to site as mentioned
    sleep(20)
    chirag.hotkey('ctrl', 'd') #----- will switch off the mic on google meet
    sleep(3)
    chirag.hotkey('ctrl', 'e') #-----will switch off the camera on google meet
    sleep(3)
#adding the xpath of the join button to join the meet and using click to click on it.
#adding the xpath is easy , just inspect the button in chrome browser and copy the xpath
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
    sleep(900)
# leaving the meeting after 900sec. or 15 minutes
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button').click()
# using the schedule library to schedule the join() funtion to run at 06:59 everyday
schedule.every().day.at("06:59").do(join)
while True:
    schedule.run_pending()
    time.sleep(5)




