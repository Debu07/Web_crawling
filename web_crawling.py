import csv
from selenium import webdriver
MAX_PAGE_NUM=5
MAX_PAGE_DIG=3

with open('result.csv','w') as f:
    f.write('Buyers,Price\n')

driver=webdriver.Firefox()

for i in range(1,MAX_PAGE_NUM+1):
    page_num=(MAX_PAGE_DIG-len(str(i)))*'0'+str(i)  # 3- you are at page one so i = 1 ->3-1=2*0 ->00+str(i) -> "001"
    url='http://econpy.pythonanywhere.com/ex/'+page_num+'.html'
    driver.get(url)

    buyers=driver.find_element_by_xpath("//div[@title='buyer-name']")
    prices=driver.find_element_by_xpath("//span[@class='item-price']")

    with open('result.csv','a') as f:
        for i in range(len(buyers)):
            f.write(buyers[i].text+","+prices[i].text+"\n")
driver.close()

