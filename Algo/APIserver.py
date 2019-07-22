debug = False
def debugPrint(thing):
    if debug:
        print(thing)
infinity = 90000000

import requests
import flight
import json
import threading
import datetime
import node
# from node import node
apikey = "b87938c8dcmshce40b6d7556e1bap1afddfjsn495f23ba1e44"



class costThread(threading.Thread):
    def setinput(self, src:node, dst:node, date:datetime.datetime):
        self.src = src
        self.dst = dst
        self.date = date
    
    def run(self):
        self.flight = calccost(self.src, self.dst, self.date)

    def getresults(self):
        return self.flight







class replywrapper:
    def __init__(self, jsonreply):
        self.response = json.loads(jsonreply)
        if len(self.response["Quotes"]) == 0:
            self.valid=False
            return
        self.valid = True
        self.price = self.response["Quotes"][0]["MinPrice"]
        self.carrierID, self.carrierName = self.__getcarrier()
        self.currency = self.response["Currencies"][0]["Code"]


    def __str__(self):
        return "carrier {}:{} had the best price of {}{}".format(self.carrierName, self.carrierID, self.price, self.currency)
    def __getcarrier(self):
        index = self.response["Quotes"][0]["OutboundLeg"]["CarrierIds"][0]
        carriers =  self.response["Carriers"]
        for c in carriers:
            if c["CarrierId"] == index:
                return index, c["Name"]
        raise Exception('Error in API, no valid Carrier was returned')



headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": apikey,
    "Content-Type": "application/x-www-form-urlencoded"
  }


def calccost(src:node.node, dst:node.node, date:datetime.datetime) -> flight.flight:
    src = src.airport + "-sky"
    dst = dst.airport + "-sky"
    debugPrint("checking {} to {}".format(src, dst))
    url = """https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/{}""".format(src,dst,date.isoformat('-')[0:10])
    debugPrint(url)
    r = requests.get(url, headers=headers)
    # debugPrint(r.text)
    r = replywrapper(r.text)

    if(r.valid):
        debugPrint(str(r) + " from {} to {}".format(src, dst))
        # return r.price
        return flight.flight(src, dst, r.price, date,r.carrierName)
    return flight.flight(src,dst,infinity,date,"")
            