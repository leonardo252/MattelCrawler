import telegram_send

def sendItemsChanged(addedItems, removedItems, onSales):

    if (len(onSales) > 0):
        for item in onSales:
            menssage = "💰〽️ %s 〽️💰 \n\n🚗 %s \n💰 Preço: %s \n❗ Situação: %s \n🔗 Link: %s \n\n〽️💰〽️ ITEM EM PROMOÇÃO 〽️💰〽️" % (onSales[item]["name"], onSales[item]["name"], onSales[item]["price"], onSales[item]["situation"], onSales[item]["link"])
            telegram_send.send(messages=[menssage])
        

    if (len(addedItems) > 0):

        for item in addedItems:
            menssage = "✅❎ %s ❎✅ \n\n🚗 %s \n💰 Preço: %s \n❗ Situação: %s \n🔗 Link: %s \n\n✅❎✅ ITEM DISPONÍVEL ✅❎✅" % (addedItems[item]["name"], addedItems[item]["name"], addedItems[item]["price"], addedItems[item]["situation"], addedItems[item]["link"])
            telegram_send.send(messages=[menssage])
    # else:
    #     print("Zero New Items")

    if (len(removedItems) > 0):

        for item in removedItems:
            menssage = "❌⛔️ %s ❌⛔️ \n\n🚗 %s \n💰 Preço: %s \n❗ Situação: %s \n🔗 Link: %s \n\n❌⛔️❌ ITEM REMOVIDO ❌⛔️❌" % (removedItems[item]["name"],removedItems[item]["name"], removedItems[item]["price"], removedItems[item]["situation"], removedItems[item]["link"])
            telegram_send.send(messages=[menssage])
    # else:
    #     print("Zero Removed Items")

def sendManssage(messages):
    telegram_send.send(messages=[messages])