from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
import pandas as pd
import pickle

web = 'https://www.betway.co.ke/'
path="C:\\pythonScripts\\geckodriver.exe"
options=Options()
options.add_argument('--headless')
driver=webdriver.Firefox(executable_path=path,service_log_path='nul')
driver.get(web)

teams=[]
x12=[]
btts=[]
odds_events=[]

sleep(20)
seq=driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(seq[2])
p=driver.find_element_by_tag_name('button').click()
driver.switch_to.default_content()
sleep(5)
box=driver.find_element_by_id('bettingtabs')
'''row_events=box.find_elements_by_id('01aab7a6-0000-0000-0000-000000000000')
print(len(row_events))'''
box=driver.find_element_by_class_name('tab-content')

rows=box.find_elements_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]')
for i in range (2,22,1):
    rows.append(box.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]'))


for event in rows:
    for i in range (2,22,1):
        home_team=event.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div[1]')
        home_win_odd=event.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div[2]')
        draw_odd=event.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[2]/div/div[2]')
        away_team=event.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[3]/div/div[1]')
        away_team_odd=event.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[3]/div/div[2]')

        game_teams=str(home_team.text)+f'\\n'+ str(away_team.text)
        three_way= str(home_win_odd.text)+'\\n'+str(draw_odd.text)+'\\n'+str(away_team_odd.text)                    
        teams.append(game_teams)
        x12.append(three_way)
more_=driver.find_element_by_class_name('filter-market-label')
more_.click()
btts_button=driver.find_element_by_id('a2667d0c-e70f-e811-80d9-00155d4cf18a')
btts_=btts_button.find_element_by_class_name('anchor-market-type')
btts_.click()
sleep(2)
'''highlights=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/span[1]')
highlights.click()'''

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)



dict_gambling={'Teams':teams,'3-Way':x12}
df_betway=pd.DataFrame.from_dict(dict_gambling)
df_betway=df_betway.applymap(lambda x:x.strip() if isinstance(x,str) else x)

'''SAVE DATA'''
output=open('df_betway','wb')
pickle.dump(df_betway,output)
output.close()
print(df_betway)


    #print(event.text)
#/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]
#/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]
#/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[20]/div[2]
#/html/body/div[2]/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[21]/div[2]