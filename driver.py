import time
import numpy as np
import os
import random
from selenium import webdriver

debug_mode=True

driver = webdriver.Chrome('./chromedriver')
#driver.get('https://bhaubhau.github.io')
file_path='file:///' + os.getcwd() + '/index.html'
if debug_mode:
    print(file_path)
driver.get(file_path)
time.sleep(10)

def click_up():
    global driver, debug_mode
    if debug_mode:
        print("Clicking up")
    up_button=driver.find_element_by_xpath("//i[@class='up']/parent::button")
    up_button.click()

def click_down():
    global driver, debug_mode
    if debug_mode:
        print("Clicking down")
    down_button=driver.find_element_by_xpath("//i[@class='down']/parent::button")
    down_button.click()

def click_left():
    global driver, debug_mode
    if debug_mode:
        print("Clicking left")
    left_button=driver.find_element_by_xpath("//i[@class='left']/parent::button")
    left_button.click()

def click_right():
    global driver, debug_mode
    if debug_mode:
        print("Clicking right")
    right_button=driver.find_element_by_xpath("//i[@class='right']/parent::button")
    right_button.click()

def perform_action(action_code):
    if(isinstance(action_code,int)):
        if action_code==0:
            click_up()        
        elif action_code==1:
            click_right()
        elif action_code==2:
            click_down()
        elif action_code==3:
            click_left()
    elif(isinstance(action_code,str)):
        if action_code.lower()=='up':
            click_up()        
        elif action_code.lower()=='right':
            click_right()
        elif action_code.lower()=='down':
            click_down()
        elif action_code.lower()=='left':
            click_left()
    time.sleep(200/1000)

def get_current_state():
    global driver
    tiles=driver.find_elements_by_class_name("tile")
    result=[]
    for tile in tiles:
        tile_text=tile.text
        if tile_text=='':
            result.append(0)
        else:
            result.append(int(tile_text))
    result=np.array(result)
    result=result.reshape((4, 4))
    return result

def perform_random_action():
    global debug_mode
    current_state=get_current_state()
    action_list=[0,1,2,3]
    action=random.choice(action_list)
    perform_action(action)
    next_state=get_current_state()
    if debug_mode:
        print(current_state)
        print(action)
        print(next_state)
    return current_state, action, next_state

while True:
    current_state, action, next_state = perform_random_action()
    if (0 in next_state.flatten())==False:
        print('Game Over')
        break
    
driver.quit()