import requests
import flight
import json
# from node import node
apikey = "b87938c8dcmshce40b6d7556e1bap1afddfjsn495f23ba1e44"


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


def calccost(date="2019-09-01" ,src="SFO-sky", dst="JFK-sky"):
    url = """https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/{}""".format(src,dst,date)
    print(url)
    r = requests.get(url, headers=headers)

    print(replywrapper(r.text))
    print(r.text)


    return flight.flight(0,0,0,0)
calccost(0)