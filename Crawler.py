from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from enum import Enum

# DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
DRIVER_PATH = '/Users/leonardo/Desktop/MattelCrawler/chromedriver'

mattelPath = {'HotWheels': 'https://creations.mattel.com/collections/hot-wheels-collectors', 'MattelCreations': 'https://creations.mattel.com/collections/mattel-creations' ,'AllMattel': 'https://creations.mattel.com/collections/all'}

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")



class MattelPath(Enum):
    HotWheels = 'HotWheels'
    AllMattel = 'AllMattel'
    MattelCreations = 'MattelCreations'

def getListItemsWeb(path):
    print("Get List of Itens from Web Page")

    itensList = {}
    
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(mattelPath[MattelPath(path).value])

    collection_itens = driver.find_element(By.CLASS_NAME, "collection_main")
    all_itens = collection_itens.find_elements(By.CLASS_NAME, "product-item")

    for item in all_itens:

        productName = item.find_element(By.ID, "productTitle").get_attribute("value")
        productSkul = item.find_element(By.ID, "prodSku").get_attribute("value")
        productPrice = item.find_element(By.ID, "product-price").get_attribute("value")
        productSituation = item.find_element(By.ID, "product-availability").get_attribute("value")
        productLink = item.find_element(By.CLASS_NAME, "product-item__link").get_attribute("href")
        itensList[productSkul] = {"name": productName, "price": productPrice, "situation": productSituation, "link": productLink}

    driver.quit()

    return itensList

