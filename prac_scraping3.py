from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('.\chromedriver.exe')
url = "https://www.airbnb.co.id/s/Bandung--Indonesia/homes?adults=1&place_id=ChIJf0dSgjnmaC4RshXo05MfahQ&refinement_paths%5B%5D=%2Fhomes"
driver.get(url)
sleep(5)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(5)

req = driver.page_source

driver.quit()

soup = BeautifulSoup(req, 'html.parser')

images = soup.select('img')
for image in images:
    print(image['src'])