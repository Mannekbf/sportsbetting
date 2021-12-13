# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:08:03 2021

@author: brieuc.feneuil
"""

#%% Import modules and packages

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
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



#%% Scrape bookmaker's website

#sport_title = driver.find_elements_by_class_name("filters__content")
sport_title = driver.find_elements(By.CLASS_NAME, "filters__content")
print(sport_title)


for sport in sport_title:
    print(sport)

# driver.findElement(By.id("query")               
# sport_list = [x.replace('\n', '') for x in sport_title]
# football_title = driver.find_elements_by_class_name('Soccer active')
# tennis_title = driver.find_elements_by_class_name('Tennis active')
# basketball_title = driver.find_elements_by_class_name('Basketball active')
# icehockey_title = driver.find_elements_by_class_name('Icehockey active')



# for x in sport_title:
#     sport_list = x.text.split('\n')
#     print(sport_list)
        
#     for sport in sport_list:
#         if sport == 'Tennis':
#             print('yes')
#             parent = sport.find_elements_by_class_name('bet_event_main_list')
#             granny = sport.find_elements_by_class_name('bet_event_row')
#             print(granny.text)
#             grandparent = parent.find_elements_by_class_name('data-container 532a3c3c-0410-1a94-c747-fc3bc383a773')
    
#             single_row_events = grandparent.find_elements_by_class_name('Bet-event-list')
            
    
#             for match in single_row_events:
#                 odds_event = match.find_elements_by_class_name('bet-outcome-list cols-3')
#                 odds_events.append(odds_event)
                
#                 team1 = match.find_elements_by_class_name("bet-team-name bet-team1-name")
#                 team2 = match.find_elements_by_class_name("bet-team-name bet-team2-name")
#                 print(team1.text)
#                 print(team2.text)
                                                      
