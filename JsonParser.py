import json

FILENAMEHW = 'HotWheelsHistory.json'
FILENAMEMC = 'AllMattelCreations.json'

    # Ele dá um dump direto, formatado pra strings no python
    # with open('json_data1.json', 'w') as outfile:
    #     json.dump(json_string, outfile)

    # json_string = json.dumps(data)


def updateJsonData(listItens):
    jsonString = json.dumps(listItens)
    __writeJSon(jsonString, FILENAMEHW)

def getListJson():
    print("Get List of Itens from Hot Wheels JSon")
    return __readJson(FILENAMEHW)

def updateAllMattelJson(listItens):
    jsonString = json.dumps(listItens)
    __writeJson(jsonString, FILENAMEMC)

def getAllMattelJson():
    print("Get List of Itens from Mattel Creations JSon")
    return __readJson(FILENAMEMC)

def __writeJSon(jsonString, fileName):

    try:
        with open(fileName, 'w') as outfile:
            outfile.write(jsonString)
    except:
        print("Problem to read JSON")

def __readJson(fileName):

    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
            return data

    except:
        return []
