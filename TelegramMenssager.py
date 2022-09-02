import telegram_send

def sendItemsChanged(addedItems, removedItems):

    if (len(addedItems) > 0):

        for item in addedItems:
            menssage = "✅❎✅ ITEM ADICIONADO ✅❎✅  \n\n🚗 %s \n💰 Preço: %s \n❗ Situação: %s \n🔗 Link: %s" % (addedItems[item]["name"], addedItems[item]["price"], addedItems[item]["situation"], addedItems[item]["link"])
            telegram_send.send(messages=[menssage])
    else:
        print("Zero New Items")

    if (len(removedItems) > 0):

        for item in removedItems:
            menssage = "❌⛔️❌ ITEM REMOVIDO ❌⛔️❌  \n\n🚗 %s \n💰 Preço: %s \n❗ Situação: %s \n🔗 Link: %s" % (removedItems[item]["name"], removedItems[item]["price"], removedItems[item]["situation"], removedItems[item]["link"])
            telegram_send.send(messages=[menssage])
    else:
        print("Zero Removed Items")

def sendManssage(messages):
    telegram_send.send(messages=[messages])