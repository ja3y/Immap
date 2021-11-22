
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#GMAIL LOGIN
driver = webdriver.Chrome("/home/whoami/Documents/chrome_webdriver/chromedriver")
driver.get("https://www.google.com/maps/d/u/0/edit?hl=en&hl=en&mid=1d6JASAI4fKC3j_Zf8I7duT7w6ctvY4cn&ll=9.014779480121868%2C8.675276999999937&z=6")
time.sleep(5)
driver.find_element_by_id("identifierId").send_keys("dpublic91")
driver.find_element_by_xpath("//*[@id='identifierNext']").send_keys(Keys.RETURN)
time.sleep(3)
passwo= driver.find_element_by_xpath("//input[@name = 'password']")
passwo.send_keys("ikehchukwu")
driver.find_element_by_xpath("//span[@class = 'RveJvd snByac']").click()
time.sleep(5)




    #opens coordinates txt file
coordinates = open("coor.txt" , "r")
asa = ([])
for co in coordinates:
        #copy coordinates into the list([asa])
    asa.append(co)
print (asa)

print("** Starting Loop **")

for cor in asa:

         searchbox = driver.find_element_by_xpath("//input[@id='mapsprosearch-field']")
         searchbox.send_keys(cor)
         searchbox.send_keys(Keys.RETURN)
         time.sleep(2)

         search2= driver.find_element_by_xpath("//*[@class ='un1lmc-pbTTYe-ibnC6b-r4nke']").click()
         time.sleep(2)
         atmbutton= driver.find_element_by_xpath("//*[@class ='un1lmc-pbTTYe-ibnC6b-htvI8d']").click()
