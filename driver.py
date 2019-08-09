import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://bhaubhau.github.io')

def click_up():
    global driver
    print("Clicking up")
    up_button=driver.find_element_by_xpath("//i[@class='up']/parent::button")
    up_button.click()

def click_down():
    global driver
    print("Clicking down")
    down_button=driver.find_element_by_xpath("//i[@class='down']/parent::button")
    down_button.click()

def click_left():
    global driver
    print("Clicking left")
    left_button=driver.find_element_by_xpath("//i[@class='left']/parent::button")
    left_button.click()

def click_right():
    global driver
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
    time.sleep(5)

def get_current_state():
    global driver
    tiles=driver.find_elements_by_class_name("tile")
    result=[]
    for tile in tiles:
        tile_text=tile.text
        if tile_text=='':
            result.append('0')
        else:
            result.append(tile_text)
    print(str(result))
    return result

time.sleep(5)
get_current_state()
perform_action(0)
get_current_state()
perform_action(1)
get_current_state()
perform_action(2)
get_current_state()
perform_action(3)
get_current_state()
perform_action('Up')
get_current_state()
perform_action('right')
get_current_state()
perform_action('Down')
get_current_state()
perform_action('left')
get_current_state()

driver.quit()