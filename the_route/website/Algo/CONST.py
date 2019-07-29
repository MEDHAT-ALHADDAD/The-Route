apikey = "b87938c8dcmshce40b6d7556e1bap1afddfjsn495f23ba1e44"
THREADIT = True
cooldowntime = 2 # 2 seconds of cool down
TURBOMODE = False
debug = False
infinity = 90000000
APIheaders={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": apikey,
    "Content-Type": "application/x-www-form-urlencoded"
  }
def debugPrint(thing):
    if debug:
        print(thing)

citytoairport={"Atlanta":"ATL","Chicago":"ORD","Dubai":"DXB","Los Angeles":"LAX","London":"LHR", "Tokyo":"HND"}
airporttocity={v: k for k, v in citytoairport.items()}