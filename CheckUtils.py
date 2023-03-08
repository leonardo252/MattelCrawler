
def compareItemsQuantity(listWeb, listJson):
    print("Comparing sizes of lists. ListWeb: %d - ListJSon: %d" % (len(listWeb), len(listJson)))

def compareItems(listWeb, listJson):
    # print("Compair lists")

    newItems = {}
    removedItems = {}
    onSales = {}

    for webItem in listWeb:
        if listWeb[webItem]["situation"] == "Available":
            if listWeb[webItem]["onSale"] == True:
                try:
                    hasOnSale = []
                except:
                    onSales[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"], "onSale": listWeb[webItem]["onSale"]}
            else:
                try:
                    alreadyHas = listJson[webItem]
                    if listJson[webItem]["situation"] == "Sold Out":
                        newItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"], "onSale": listWeb[webItem]["onSale"]}
    
                except:
                    newItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"], "onSale": listWeb[webItem]["onSale"]}

            
        else:
            try:
                alreadyHas = listJson[webItem]
                if listJson[webItem]["situation"] == "Available":
                    removedItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"], "onSale": listWeb[webItem]["onSale"]}
  
            except:
                removedItems[webItem] = {"name": listWeb[webItem]["name"], "price": listWeb[webItem]["price"], "situation": listWeb[webItem]["situation"], "link": listWeb[webItem]["link"], "onSale": listWeb[webItem]["onSale"]}


    return (newItems, removedItems, onSales)