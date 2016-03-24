#TODO: Import the module that will allow you to use Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard

def play2048( times ):
    browser = webdriver.Firefox() #opens the firefox browser
    browser.get('https://gabrielecirulli.github.io/2048/')#opens url in firefox

    htmlElem = browser.find_element_by_tag_name('html')
    scoreElem = browser.find_element_by_class_name('score-container') #used inspect element to find out what the score box was labled on the website, determined it was called score-container. this finds the information that will show up in score container and assigns it to scoreElem 

    moves = 0
    for moves in range(times): #this section will press the up right down and left keys within the browser in order to control the game.  
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        moves += 1
        

    print('Your final score is: ' + scoreElem.text) #this will print the text that lies within the element score-container on the website. 
        
            
        
        
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 
    
