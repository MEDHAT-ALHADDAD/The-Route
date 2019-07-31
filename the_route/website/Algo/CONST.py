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

citytoairport={"atlanta":"ATL","chicago":"ORD","dubai":"DXB","los angeles":"LAX","london":"LHR", "tokyo":"HND"}
airporttocity={v: k for k, v in citytoairport.items()}