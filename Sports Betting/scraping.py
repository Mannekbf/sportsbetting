# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:08:03 2021

@author: brieuc.feneuil
"""

#%% Import modules and packages

import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time


#%% Set variables

binary_odds_sport_list = ["Basketball", "Tennis", "American Football", "Volleyball", "Esports", "Boxing", "Darts", "MMA"]
threeway_odds_sport_list = ["Football", "Handball", "Ice Hockey", "Rugby", "Futsal"]

weekdays_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

column_names = ["Bookmaker", "Sport", "team1", "team2", "team1odd", "teamstieodd", "team2odd"]
df = pd.DataFrame(columns = column_names)

web = 'https://sport.circus.be/en/sport/'
path = Service(r'C:\Users\brieuc.feneuil\Downloads\chromedriver.exe')

see_more_button = True
event_presence = True
id_presence = True

#%% Set connection with bookmaker

driver = webdriver.Chrome(service=path)
driver.get(web)

time.sleep(5)
xpath = '//*[@id="didomi-notice-agree-button"]'
accept = driver.find_element(By.XPATH,xpath)
accept.click()

driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

wait = WebDriverWait(driver, 15)
wait2 = WebDriverWait(driver, 20)

#%% Scrape bookmaker's website

time.sleep(5)
# /div[1]/aside/div li
container = driver.find_element(By.XPATH, "//*[@class='betting-tops__container top-prematch__container']")
sport_list = container.find_elements(By.CSS_SELECTOR, ".filters__content li")

for x in range(0,len(sport_list)):
    
    #reinitialize sport_list (otherwise Stale problem)
    time.sleep(5)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='betting-tops__container top-prematch__container']")))
    container = driver.find_element(By.XPATH, "//*[@class='betting-tops__container top-prematch__container']")
    sport_list = container.find_elements(By.CSS_SELECTOR, ".filters__content li")    
    
    if len(sport_list) == 0 :
        time.sleep(5)
        sport_list = container.find_elements(By.CSS_SELECTOR, ".filters__content li")
    
    print("Sport ", x+1, " / ", len(sport_list))
        
    # if sport_list[x].text == "American Football":
            
    # print(sport_list[x].text)
    sport = sport_list[x].text
    # print(sport)
    
    sport_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='betting-tops__container top-prematch__container']//label[@title='%s']"  % sport)))
    driver.execute_script("arguments[0].click();", sport_button)
    
    sport_prematch_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='betting-tops__container top-prematch__container']//a[contains(text(),'prematches')]")))
    driver.execute_script("arguments[0].click();", sport_prematch_button)
    
    time.sleep(5)
    
    #finding all days for games of a same sport 
    days_list = driver.find_elements(By.XPATH, "//div[@class='filters__content']//label")
          
    #loop for clicking on all day buttons for future games of a same sport
    for y in range(0,len(days_list)) :
        
        days_list = driver.find_elements(By.XPATH, "//div[@class='filters__content']//label")
        
        day = days_list[y].text
        
        # either the text contains a space or no any
        try:    
            day_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@title='%s']"  % day)))
            driver.execute_script("arguments[0].click();", day_button)

        except: 
            day_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@title='%s ']"  % day)))
            driver.execute_script("arguments[0].click();", day_button)
    
        while see_more_button :
            
            try:
                see_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='See more']")))
                driver.execute_script("arguments[0].click();", see_more_button)
                
            except:
                break
            
        try:
            driver.find_element(By.XPATH, "//div[@class='notification-box info']/div")
            continue
        
        except:
            pass
        
        events = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='bet-event-list']/div")))
        print(len(events), "events planified")    
        
        for z in range(0,len(events)):
            
            time.sleep(0.25)
            
            print("Event ", z+1, " / ", len(events))
            
            while id_presence: 
                
                try:
                    events = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='bet-event-list']/div")))
                    event_id = events[z].get_attribute('id')               
                    event_teams = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='%s']//div[contains(@class,'bet-team-name')]"  % event_id)))
                    break
                
                except:
                    if z+1 > len(events):
                        continue
                            
                    else:
                        pass
            
            if len(event_teams) == 1:
                events = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='bet-event-list']/div")))
                continue
            
            else:
                pass
            
            print(event_teams[0].text)
            print(event_teams[1].text)
            
            while event_presence:
            
                try:
                    # print("STALE 5 ?")
                    event_teams = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='%s']//div[contains(@class,'bet-team-name')]"  % event_id)))
                    name_team1 = event_teams[0].text
                    name_team2 = event_teams[1].text
                    break
                
                except:
                    pass
                    
            try: 
                if sport in binary_odds_sport_list:
                    event_odds = wait.until(EC.presence_of_all_elements_located((By.XPATH,"(//div[@id='%s']//div[@class='bet-outcome-list cols-2'])[1]//div[@class='bet-outcome']"  % event_id)))
                else:
                    event_odds = wait.until(EC.presence_of_all_elements_located((By.XPATH,"(//div[@id='%s']//div[@class='bet-outcome-list cols-3'])[1]//div[@class='bet-outcome']"  % event_id)))
                
                print("Odd list length is" , len(event_odds))
                
                #try without this ?
                if event_odds[0].text == '' and event_odds[-1].text == '':
                    print("No odds for this event")
                    continue
                
                elif event_odds[0].text == '-' :
                    odd_team1 = 1
                    odd_team2 = float(event_odds[-1].text)
                    print(odd_team1)
                    print(odd_team2)
                
                elif event_odds[-1].text == '-' :
                    odd_team1 = float(event_odds[0].text)
                    odd_team2 = 1
                    print(odd_team1)
                    print(odd_team2)
                
                else:
                    odd_team1 = float(event_odds[0].text)
                    odd_team2 = float(event_odds[-1].text)
                    print(odd_team1)
                    print(odd_team2)
                
                if len(event_odds) == 3 :    
                    odd_tie = float(event_odds[1].text)
                    print(odd_tie)
                    
                else:     
                    odd_tie = 0     
                
                df = df.append({'Bookmaker' : "Circus",
                                'Sport': sport,
                                'team1': name_team1,
                                'team2': name_team2,
                                'team1odd': odd_team1,
                                'teamstieodd': odd_tie,
                                'team2odd': odd_team2,
                                'Expectancy' : (1/odd_team1) + (1/odd_tie) + (1/odd_team2),
                                }, 
                                ignore_index=True)
            
            except:       
                pass
                
            # #reinitialize events list (otherwise Stale problem)
            # events = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='bet-event-list']/div")))
    
        # #reinitialize day button list
        # days_list = driver.find_elements(By.XPATH, "//div[@class='filters__content']//label")
    
    #go back to previous page
    go_back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='go-back']")))
    driver.execute_script("arguments[0].click();", go_back_button)
    
    #reinitialize sport_list (otherwise Stale problem)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='betting-tops__container top-prematch__container']")))
    # container = driver.find_element(By.XPATH, "//*[@class='betting-tops__container top-prematch__container']")
    # sport_list = container.find_elements(By.CSS_SELECTOR, ".filters__content li")
