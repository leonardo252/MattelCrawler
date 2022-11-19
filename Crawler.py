from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from enum import Enum
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle


DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
DRIVER_PATH = '/Users/leonardo/Desktop/MattelCrawler/chromedriver'

mattelPath = {'HotWheels': 'https://creations.mattel.com/collections/hot-wheels-collectors', 'MattelCreations': 'https://creations.mattel.com/collections/mattel-creations' ,'AllMattel': 'https://creations.mattel.com/collections/all'}


class MattelPath(Enum):
    HotWheels = 'HotWheels'
    AllMattel = 'AllMattel'
    MattelCreations = 'MattelCreations'

def getListItemsWeb(path):
    print("Get List of Itens from Web Page")

    itensList = {}
    
    # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--user-data-dir=chrome-data")
    # chrome_options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # driver.implicitly_wait(1)
    driver.get(mattelPath[MattelPath(path).value])

    time.sleep(5)

    collection_itens = driver.find_element(By.CLASS_NAME, "collection-grid__container")
    all_itens = collection_itens.find_elements(By.CLASS_NAME, "collection-grid__product")

    for item in all_itens:
        productName = item.find_element(By.CLASS_NAME, "collection-grid__product-name").text
        productPrice = item.find_element(By.CLASS_NAME, "collection-grid__product-price").text
        productLink = item.find_element(By.CLASS_NAME, "pi__link").get_attribute("href")
        try: 
            productSituation = item.find_element(By.CLASS_NAME, "collection-grid__product-description-badge").text
        except:
            productSituation = "Available"
        
        itensList[productName] = {"name": productName, "price": productPrice, "situation": productSituation, "link": productLink}

    driver.quit()
    return itensList

def getCookies():

    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    chrome_options.add_argument("user-data-dir=chrome-data")
    driver.get(mattelPath[MattelPath('HotWheels').value])

    cookies = driver.get_cookies()

    time.sleep(60)

    driver.quit()

def loadCookies():

    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(mattelPath[MattelPath('HotWheels').value])

    time.sleep(60)
    driver.quit()