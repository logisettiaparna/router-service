import sys

from service.config.app_config import loadConfig

def isCityExist(kvMapState,city):
    if kvMapState.get(city):
        print(kvMapState.get(city))
    elif kvMapState.get("*"):
        print(kvMapState.get("*"))
    else:
        anyCustomer()

def isStateExists(kvMapCountry,state,city):
    if kvMapCountry.get(state):
        kvMapState = kvMapCountry.get(state)
        isCityExist(kvMapState, city)
    elif kvMapCountry.get("*"):
        #print("here in no state")
        kvMapState = kvMapCountry.get("*")
        isCityExist(kvMapState, city)
    else:
        anyCustomer()

def isCountryExists(kvMapCustomer,country,state,city):
    if kvMapCustomer.get(country):
        kvMapCountry = kvMapCustomer.get(country)
        isStateExists(kvMapCountry, state, city)
    elif kvMapCustomer.get("*"):
        #print("here in no country")
        kvMapCountry = kvMapCustomer.get("*")
        isStateExists(kvMapCountry, state, city)
    else:
        anyCustomer()

def anyCustomer():
    print(kvMap.get("*").get("*").get("*").get("*"))

def findRoute(inputStr,kvMap):
    inputSplit=inputStr.split(".")
    customer_id = inputSplit[0]
    country = inputSplit[1]
    state = inputSplit[2]
    city = inputSplit[3]

    #Check if Customer exists....if no customer found, then execute "any" case("*") - Same with other keys
    if kvMap.get(customer_id):
        kvMapCustomer = kvMap.get(customer_id)
        isCountryExists(kvMapCustomer, country, state, city)
    else:
        anyCustomer()



if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise Exception('One Input String expected with pattern "<customer_id>.<country>.<state>.<city>" ')

    inputStr = args[1]
    kvMap=loadConfig.loadConfig_map()
    findRoute(inputStr,kvMap)