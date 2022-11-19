
def compareItemsQuantity(listWeb, listJson):
    print("Comparing sizes of lists. ListWeb: %d - ListJSon: %d" % (len(listWeb), len(listJson)))

def compareItems(listWeb, listJson):
    # print("Compair lists")

    newItems = {}
    removedItems = {}


    for webItem in listWeb:
        if listWeb[webItem]["situation"] == "Available":
            try:
                alreadyHas = listJson[webItem]
                if listJson[webItem]["situation"] == "Sold Out":
                    newItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"]}
  
            except:
                newItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"]}

        else:
            try:
                alreadyHas = listJson[webItem]
                if listJson[webItem]["situation"] == "Available":
                    removedItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"]}
  
            except:
                removedItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"]}


    return (newItems, removedItems)