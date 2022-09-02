
def compareItemsQuantity(listWeb, listJson):
    print("Comparing sizes of lists. ListWeb: %d - ListJSon: %d" % (len(listWeb), len(listJson)))

def compareItems(listWeb, listJson):
    # print("Compair lists")

    newItems = {}
    removedItems = {}

    for jsonItem in listJson:
        try:
            alreadyHas = listWeb[jsonItem]
        except:
            removedItems[jsonItem] = {"name": listJson[jsonItem]["name"], "price": listJson[jsonItem]["price"], "situation": listJson[jsonItem]["situation"], "link": listJson[jsonItem]["link"]}

    for webItem in listWeb:
        try:
            nowHas = listJson[webItem]
        except:
            newItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"]}

    return (newItems, removedItems)