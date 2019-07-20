debug = False
def debugPrint(thing):
    if debug:
        print(thing)


import requests
import flight
import json
import threading
# from node import node
apikey = "b87938c8dcmshce40b6d7556e1bap1afddfjsn495f23ba1e44"



class costThread(threading.Thread):
    def setinput(self, src="SFO", dst="JFK", date="2019-09-01", tmpcost = 0):
        self.src = src
        self.dst = dst
        self.date = date
        self.tmpcost = tmpcost
        self.totalcost = -1
    
    def run(self):
        self.totalcost = self.tmpcost + calccost(self.src, self.dst, self.date)

    def getTotalCost(self):
        return self.totalcost







class replywrapper:
    def __init__(self, jsonreply):
        self.response = json.loads(jsonreply)
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


def calccost(src="SFO", dst="JFK", date="2019-09-01"):
    src = src + "-sky"
    dst = dst + "-sky"
    debugPrint("checking {} to {}".format(src, dst))
    url = """https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/{}""".format(src,dst,date)
    # debugPrint(url)
    r = requests.get(url, headers=headers)
    # debugPrint(r.text)
    r = replywrapper(r.text)
    debugPrint(str(r) + " from {} to {}".format(src, dst))

    return r.price
    # return flight.flight(0,0,0,0)
            