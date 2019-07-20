class flight:
    def __init__(self, src, dst, price, date, carrier):
        self.src = src
        self.dst = dst
        self.price = price
        self.date = date
        self.carrier = carrier

    def __str__(self):
        return "take trip from {} airport to {} airport on {} at price of {} from {} company".format(self.src,self.dst,self.date, self.price, self.carrier)