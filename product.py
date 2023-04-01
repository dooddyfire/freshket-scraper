import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






driver = webdriver.Chrome(ChromeDriverManager().install())

cat = "leafy"
product_lis = []

product_image_lis = []
product_name_lis = []
package_lis = []
product_url_lis = []
product_price_lis = []
product_detail_lis = []


for i in range(1,2):
    # Get Page Number  
    page = i 
    url = "https://www.freshket.co/en/market/vegetable/{}?page={}".format(cat,page)
   
    driver.get(url)
    #time.sleep(5)
    
    image_per_page_lis = [ c.find_element(By.CSS_SELECTOR,'img').get_attribute('src') for c in driver.find_elements(By.CSS_SELECTOR,"#product-image")]
    print(image_per_page_lis)

    for item in image_per_page_lis:
        product_image_lis.append(item)








    product_url = [ c.get_attribute('href') for c in driver.find_elements(By.CSS_SELECTOR,"a.MuiLink-root")]
    print(product_url)


    for i in product_url[3:]: 
        try:
            urlx = i
            driver.get(i)
            #time.sleep(5)

            product_name = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div/div/div[3]/div/h1').text 
            print(product_name)
            product_name_lis.append(product_name)

            price = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/h6').text 
            print(price)
            product_price_lis.append(price)

            packaging = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div/div/div[3]/div/p').text 
            print(packaging)
            package_lis.append(packaging)

            product_detail = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div/div/div[3]/div/div[3]/p').text 
            print(product_detail)
            product_detail_lis.append(product_detail)
        except: 
            continue
        product_url_lis.append(urlx)


print(product_image_lis)
print(len(product_image_lis))

print('----')

print(product_name_lis)
print(len(product_name_lis))
print('----')

print(package_lis)
print(len(package_lis))



print("----------")
print(product_price_lis)
print(len(product_price_lis))

print("--------")
print(product_detail_lis)
print(len(product_detail_lis))

df = pd.DataFrame()
df['brand'] = [ cat for i in range(len(product_name_lis))]
df['name'] = product_name_lis 
df['รูปภาพ'] = product_image_lis 
df['ml/g'] = package_lis 
df['Packaging'] = package_lis 
df['ราคาเต็มก่อนส่วนลด'] = product_price_lis
df['url'] = product_url_lis

df.to_excel("Vegx.xlsx")