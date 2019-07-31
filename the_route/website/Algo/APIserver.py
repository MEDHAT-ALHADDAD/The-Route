import requests
from . import flight
import json
import threading
import datetime
from . import node
import time
from . import CONST



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
        self.tripexist = False
        self.valid = False
        self.response = json.loads(jsonreply)
        if "Quotes" not in self.response:
            return
        self.valid = True
        self.parse()

    def parse(self):
        if len(self.response["Quotes"]) == 0:
            return
        self.tripexist = True
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




def calccost(src:node.node, dst:node.node, date:datetime.datetime) -> flight.flight:
    src = src.airport + "-sky"
    dst = dst.airport + "-sky"
    # debugPrint("checking {} to {}".format(src, dst))
    url = """https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/{}""".format(src,dst,date.isoformat('-')[0:10])
    # debugPrint(url)
    r = requests.get(url, headers=CONST.APIheaders)
    # debugPrint(r.text)
    rw = replywrapper(r.text)

    while(not rw.valid):
        CONST.debugPrint(rw.response)
        time.sleep(CONST.cooldowntime)
        r = requests.get(url, headers=CONST.APIheaders)
        rw = replywrapper(r.text)
    if(rw.tripexist):
        # debugPrint(str(r) + " from {} to {}".format(src, dst))
        # return r.price
        return flight.flight(src, dst, rw.price, date,rw.carrierName)
    else:
        return flight.flight(src,dst,CONST.infinity,date,"")
            