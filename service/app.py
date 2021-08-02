import sys

from service.config.app_config import loadConfig

def isCityExist(kvMapState,city):
    if kvMapState.get(city):
        print(kvMapState.get(city))
    else:
        print(kvMapState.get("*"))

def isStateExists(kvMapCountry,state,city):
    if kvMapCountry.get(state):
        kvMapState = kvMapCountry.get(state)
        isCityExist(kvMapState, city)
    elif kvMapCountry.get("*"):
        #print("here in no state")
        kvMapState = kvMapCountry.get("*")
        isCityExist(kvMapState, city)

def isCountryExists(kvMapCustomer,country,state,city):
    if kvMapCustomer.get(country):
        kvMapCountry = kvMapCustomer.get(country)
        isStateExists(kvMapCountry, state, city)
    elif kvMapCustomer.get("*"):
        #print("here in no country")
        kvMapCountry = kvMapCustomer.get("*")
        isStateExists(kvMapCountry, state, city)

def findRoute(inputStr,kvMap):
    inputSplit=inputStr.split(".")
    customer_id = inputSplit[0]
    country = inputSplit[1]
    state = inputSplit[2]
    city = inputSplit[3]

    #Check if Customer exists....if no customer found, then execute "any" case("*")
    if kvMap.get(customer_id):
        kvMapCustomer = kvMap.get(customer_id)
        isCountryExists(kvMapCustomer, country, state, city)
    else:
        print(kvMap.get("*").get("*").get("*").get("*"))



if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise Exception('One Input String expected with pattern "<customer_id>.<country>.<state>.<city>" ')

    inputStr = args[1]
    kvMap=loadConfig.loadConfig_map()
    findRoute(inputStr,kvMap)