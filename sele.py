from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
def Location():
    options = Options()
    options.add_argument(" random screen")
    #driver = webdriver.Chrome(executable_path = 'C:/Users/uvarna veeravalli/Downloads/chromedriver.exe',options=options) #Edit path of chromedriver accordingly
    driver= webdriver.Chrome()
    timeout =10
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    long = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
    long = [x.text for x in long]    
    long = str(long[0])    
    lat = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    lat = [x.text for x in lat]    
    lat = str(lat[0])    
    driver.quit()    
    return (lat,long)
print(Location())