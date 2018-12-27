from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('http://google.com/')  #go to google
print('done')
inputelement = browser.find_element_by_id ('lst-ib')
inputelement.send_keys('dyson') # input the dyson in the search bar
inputelement.submit()
print('search completed')#click search
time.sleep(2)
dysonelement =browser.find_element_by_id('vn1s0p1c0') #find the first match
dysonelement.click() #Click to enter
print('link clicked')
vacuumelement1 = browser.find_element_by_id ('ctl00_cphNavigation_topNavigation1_TopNavigationLinksRepeater_ctl01_TopNavigationLink')
vacuumelement1.click()
print('category selected')
#vacuumelement2 = browser.find_element_by_id ('ctl00_cphNavigation_topNavigation1_TopNavigationLinksRepeater_ctl01_TopNavigationDetailRepeater_ctl02_SubMenuLink')
#vacuumelement2.click()
