import JsonParser
import Crawler
import CheckUtils
import threading
from threading import Thread
import TelegramMenssager
import datetime as dt
import sched
import time

interval = 60
otherInterval = 80

def hotWheelsCollectors(sched):

    print("Searching Hot Wheels")
    webItensList = Crawler.getListItemsWeb(Crawler.MattelPath.HotWheels)
    jsonItensList = JsonParser.getListJson()

    CheckUtils.compareItemsQuantity(webItensList, jsonItensList)

    addedItems, removedItems = CheckUtils.compareItems(webItensList, jsonItensList)

    if (len(addedItems) > 0 or len(removedItems) > 0):
        TelegramMenssager.sendMenssage(addedItems, removedItems)

        JsonParser.updateJsonData(webItensList)
    else:
        print("Noting Changed")

    sched.enter(interval, 1, hotWheelsCollectors, (sched,))

def mattelCreationsCollectors(sched):

    print("Searching All Mattel Creations")
    webItensList = Crawler.getListItemsWeb(Crawler.MattelPath.AllMattel)
    jsonItensList = JsonParser.getAllMattelJson()

    CheckUtils.compareItemsQuantity(webItensList, jsonItensList)

    addedItems, removedItems = CheckUtils.compareItems(webItensList, jsonItensList)

    if (len(addedItems) > 0 or len(removedItems) > 0):
        TelegramMenssager.sendMenssage(addedItems, removedItems)

        JsonParser.updateAllMattelJson(webItensList)
    else:
        print("Noting Changed")

    sched.enter(interval, 1, mattelCreationsCollectors, (sched,))

class ThrHW(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.interval = interval

    def run(self):
        hw = sched.scheduler(time.time, time.sleep)
        hw.enter(60, 1, hotWheelsCollectors, (hw,))
        hw.run()

class ThrMC(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.interval = interval

    def run(self):
        mc = sched.scheduler(time.time, time.sleep)
        mc.enter(80, 1, mattelCreationsCollectors, (mc,))
        mc.run()



def main():
    hw = sched.scheduler(time.time, time.sleep)
    hw.enter(interval, 1, hotWheelsCollectors, (hw,))
    hw.run()

    #mc = sched.scheduler(time.time, time.sleep)
    #mc.enter(otherInterval, 1, mattelCreationsCollectors, (mc,))
    #mc.run()

    #hw_c = ThrHW(interval)
    #mc = ThrMC(otherInterval)
    #hw_c.start()
    #mc.start()
    #hw.run()

if __name__ == "__main__":
    main()
