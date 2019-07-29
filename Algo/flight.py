class flight:
    def __init__(self, src, dst, price, date, carrier):
        self.src = src
        self.dst = dst
        self.price = price
        self.date = date
        self.carrier = carrier

    def __str__(self):
        return "take trip from {} airport to {} airport on {} at price of {} from {} company".format(self.src,self.dst,self.date, self.price, self.carrier)

    def getJSON(self, i):# i is the order of the flight in the list
        #{"no":"1","From":"Cairo","To":"London","Flight_No":"@123","Date":"12/03/2020","Price":"500$"}
        return {"no":i,"From":self.src,"To":self.dst,"Flight_No":"@123","Date":self.date,"Price":self.price}