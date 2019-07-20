import datetime
class node:
    def __init__(self, duration:datetime.timedelta, country, airport):
        self.airport = airport
        self.duration = duration
        self.country = country
    def __str__(self):
        return self.airport