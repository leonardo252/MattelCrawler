from email import message
import JsonParser
import Crawler
import CheckUtils
import threading
from threading import Thread
import TelegramMenssager
import datetime as dt
import schedule
import time

# pip install webdriver-manager

intervalHW = 60
intervalMC = 90
intervalSill = 1

def hotWheelsCollectors():
    print("\nSearching Hot Wheels Collectors")
    webItensList = Crawler.getListItemsWeb(Crawler.MattelPath.HotWheels)
    jsonItensList = JsonParser.getAllHotWheelsJson()
    onSales = JsonParser.getAllOnSales()

    CheckUtils.compareItemsQuantity(webItensList, jsonItensList)

    addedItems, removedItems, newOnSales = CheckUtils.compareItems(webItensList, jsonItensList, onSales)

    if (len(addedItems) > 0 or len(removedItems) > 0 or len(newOnSales) > 0):
        TelegramMenssager.sendItemsChanged(addedItems, removedItems, newOnSales)

        JsonParser.updateHotWheelsJson(webItensList)
        JsonParser.updateOnSales(newOnSales)
    else:
        print("Nothing new to Hot Wheels Collectors")


def mattelCreationsCollectors():
    print("\nSearching All Mattel Creations")
    webItensList = Crawler.getListItemsWeb(Crawler.MattelPath.AllMattel)
    jsonItensList = JsonParser.getAllMattelJson()

    CheckUtils.compareItemsQuantity(webItensList, jsonItensList)

    addedItems, removedItems = CheckUtils.compareItems(webItensList, jsonItensList)

    if (len(addedItems) > 0 or len(removedItems) > 0):
        TelegramMenssager.sendItemsChanged(addedItems, removedItems)

        JsonParser.updateAllMattelJson(webItensList)
    else:
        print("Nothing new to Mattel Creations")


def stillRunning():
    messages = "🤖 🛠️ ROBÔ TRABALHANDO  🛠️ 🤖"

    TelegramMenssager.sendManssage(messages)

def run_threaded(job_fn):
  job_thread = threading.Thread(target=job_fn)
  job_thread.start()

def main():

    schedule.every().hour.at(":27").do(run_threaded, stillRunning)
    schedule.every(intervalHW).seconds.do(run_threaded, hotWheelsCollectors)
    schedule.every(intervalMC).seconds.do(run_threaded, mattelCreationsCollectors)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    # main()

    # webItensList = Crawler.getListItemsWeb(Crawler.MattelPath.HotWheels)
    # print(webItensList)

    # JsonParser.read(webItensList)

    # print(JsonParser.getAllHotWheelsJson())
    
    hotWheelsCollectors()
    
    # Crawler.getCookies()

    # Crawler.loadCookies()

