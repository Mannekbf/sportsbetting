# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:08:03 2021

@author: brieuc.feneuil
"""

#%% Import modules and packages

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#%% Set variables

teams = []
x12 = []
odds_events = []


#%% Set connection with bookmaker


# def get_page():
#     url = 'https://sport.circus.be/fr/sport/sport/844'
#     response = requests.get(url)
#     html = response.text
#     print(html)

# get_page()


# football_web = 'https://sport.circus.be/fr/sport/sport/844'
# tennis_web = 'https://sport.circus.be/fr/sport/sport/848'
# basketball_web = 'https://sport.circus.be/fr/sport/sport/850'
# icehockey_web = 'https://sport.circus.be/fr/sport/sport/846'

web = 'https://sport.circus.be/en/sport/'
path = r'C:\Users\brieuc.feneuil\Downloads\chromedriver'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(5)
xpath = '//*[@id="didomi-notice-agree-button"]'
accept = driver.find_element(By.XPATH,xpath)
accept.click()

wait = WebDriverWait(driver, 10)

#%% Scrape bookmaker's website

time.sleep(5)

sport_list = driver.find_elements(By.CSS_SELECTOR,'.filters__content li')
    
for x in range(0,len(sport_list)):

    if sport_list[x].text == 'Tennis':
        print('yes')
        print(sport_list[x].text)
            
        sport_list[x].click()
            
        # driver.set_window_size(1750,800)
        
        # click on button 'load all pre-matches'
        driver.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pageContent']/div/section/div/div/div/div[1]/div/div[2]/div/div[1]/section/div/div/div/div[2]/div/div/div[3]/a"))))
        
        break
        
        # parent = sport.find_element(By.XPATH,'./..')
        # grandparent = parent.find_element(By.XPATH,'./..')
        # # parent = sport.find_elements_by_class_name('bet_event_main_list')
        # # grandparent = parent.find_elements_by_class_name('data-container 532a3c3c-0410-1a94-c747-fc3bc383a773')
        # print(parent.text)
        # print(grandparent.text)
        
        # single_row_events = grandparent.find_elements_by_class_name('Bet-event-list')
            
    
        # for match in single_row_events:
        #     odds_event = match.find_elements_by_class_name('bet-outcome-list cols-3')
        #     odds_events.append(odds_event)
                
        #     team1 = match.find_elements_by_class_name("bet-team-name bet-team1-name")
        #     team2 = match.find_elements_by_class_name("bet-team-name bet-team2-name")
        #     print(team1.text)
        #     print(team2.text)                                              
