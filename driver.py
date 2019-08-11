import time
import numpy as np
import os
import random
from selenium import webdriver

debug_mode=False

driver = webdriver.Chrome('./chromedriver')
file_path='file:///' + os.getcwd() + '/index.html'
if debug_mode:
    print(file_path)
driver.get(file_path)
time.sleep(10)

action_code_dictionary={0:'up',1:'right',2:'down',3:'left'}
for action_code in range(len(action_code_dictionary)):
    action_code_dictionary[action_code_dictionary[action_code]]=action_code

def print_action_code_string(action_code):
    global action_code_dictionary
    if action_code in range(4):
        print('Clicking ' + action_code_dictionary[action_code])    
    elif action_code==-1:
        print('Game Over')

def click_up():
    global driver, debug_mode, action_code_dictionary
    if debug_mode:
        print_action_code_string(action_code_dictionary['up'])
    up_button=driver.find_element_by_xpath("//i[@class='up']/parent::button")
    up_button.click()

def click_down():
    global driver, debug_mode, action_code_dictionary
    if debug_mode:
        print_action_code_string(action_code_dictionary['down'])
    down_button=driver.find_element_by_xpath("//i[@class='down']/parent::button")
    down_button.click()

def click_left():
    global driver, debug_mode, action_code_dictionary
    if debug_mode:
        print_action_code_string(action_code_dictionary['left'])
    left_button=driver.find_element_by_xpath("//i[@class='left']/parent::button")
    left_button.click()

def click_right():
    global driver, debug_mode, action_code_dictionary
    if debug_mode:
        print_action_code_string(action_code_dictionary['right'])
    right_button=driver.find_element_by_xpath("//i[@class='right']/parent::button")
    right_button.click()

def perform_action(action_code):
    global action_code_dictionary
    if(isinstance(action_code,int)):
        if action_code==action_code_dictionary['up']:
            click_up()        
        elif action_code==action_code_dictionary['right']:
            click_right()
        elif action_code==action_code_dictionary['down']:
            click_down()
        elif action_code==action_code_dictionary['left']:
            click_left()
    elif(isinstance(action_code,str)):
        perform_action(action_code_dictionary[action_code.lower()])
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

def play_game_randomly():
    global driver, debug_mode
    states, actions=[], []
    final_attempt_done=0
    action_number=0
    while final_attempt_done<4:
        current_state=get_current_state()
        action_list=[0,1,2,3]
        action_list=random.sample(action_list, len(action_list))
        if debug_mode:
            print('Next action_list: ' + str(action_list))
        action=action_list[0]
        perform_action(action)    
        next_state=get_current_state()  
        states.append(current_state)
        actions.append(action)   
        if debug_mode:
            print('action_number: ' + str(action_number))
            print('final_attempt_done: ' + str(final_attempt_done))
            print('current_state:')
            print(current_state)
            print('action:')
            print(action)
            print('next_state:')
            print(next_state)
        action_number=action_number+1  
        final_attempt_done=final_attempt_done+1
        for action in action_list[1:]:             
            if np.array_equal(current_state,next_state):
                perform_action(action) 
                next_state=get_current_state()
                states.append(current_state)
                final_attempt_done=final_attempt_done+1                
                actions.append(action)
                if debug_mode:
                    print('action_number: ' + str(action_number))
                    print('final_attempt_done: ' + str(final_attempt_done))
                    print('current_state:')
                    print(current_state)
                    print('action:')
                    print(action)
                    print('next_state:')
                    print(next_state)
                action_number=action_number+1  
            else:
                final_attempt_done=0                  
                break      
    states.append(current_state)
    action=-1
    actions.append(action)
    if debug_mode:
        print('action_number: ' + str(action_number))
        print('final_attempt_done: ' + str(final_attempt_done))
        print('current_state:')
        print(current_state)
        print('action:')
        print(action)
    driver.quit() 
    return states, actions      
  
states, actions=play_game_randomly()

print('Transition List:')

previous_state=np.zeros((4, 4), dtype=int)
action_number=0
for state, action in zip(states, actions):
    print('action_number: ' + str(action_number))
    if debug_mode and (np.array_equal(previous_state,state)):
        print('Unchanged')
    print('current_state:')
    print(state)
    print('action:')
    print(action)
    print_action_code_string(action)
    action_number=action_number+1
    previous_state=state