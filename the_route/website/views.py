from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from .Algo import Algo, node, flight, CONST
import datetime



def home(request):
    return render(request,'home.html')

def afterReg(request):
    if request.method == "POST":
        return redirect('../home/')
    return render(request,'afterReg.html')

def contactus(request):
    return render(request,'contactus.html')

def rec(request):
    return render(request,'request_page/rec.html')

@csrf_exempt
def results(request):
    # page will not update data or rerender for now
    # data accepted by the result page sotred in list of dicts (res)

    res = []
    # res = [
    #     {"no":"1","From":"Cairo","To":"London","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"2","From":"London","To":"paris","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"3","From":"paris","To":"Rome","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"4","From":"Rome","To":"Moscow","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"5","From":"Moscow","To":"Cairo","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"6","From":"Cairo1","To":"London1","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"7","From":"Paris1","To":"Rome1","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"8","From":"Rome1","To":"LA","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
    #     {"no":"9","From":"LA","To":"Cairo","Flight_No":"@123","Date":"12/03/2020","Price":"500$"}
    #     ]
    city = ["atlanta","chicago","dubai","los angeles","london", "tokyo"]
    for result in res:
        city.append(result['From'])

    if request.method == "POST" and request.is_ajax():
        message = "Ajax"
        val = request.POST.get('Cities_Results', '')
        Cities_list = json.loads(val)
        # data returned from the result page >> sotred in list (Cities_list) ['london','cairo','paris','moscow']
        nodes = []
        for i in Cities_list:
            print(i)
            nodes.append(node.node(datetime.timedelta(3), i, CONST.citytoairport[i]))
        totalcost,res=Algo.maincalccost(nodes[0],nodes[1:-1],nodes[-1], datetime.datetime(2019,7,20) + datetime.timedelta(days=90))

        # assigned new values to res
        # res = [
        #     {"no":"1","From":"Cairo","To":"London","Flight_No":"@123","Date":"12/03/2020","Price":"500$"},
        #     {"no":"2","From":"London","To":"paris","Flight_No":"@123","Date":"12/03/2020","Price":"500$"}
        #     ]
        city = []
        for result,i in enumerate(res):
            result = result.getJSON(i)
            city.append(result.getJSON['From'])
        print(city)
        context = {
        "results": res,
        "shortcity": city
        }
        return JsonResponse(request,'request_page/Results.html',context)
    
    else:
        message = "Not Ajax"
        context = {
            "results": res,
            "shortcity": city
            }
        return render(request,'request_page/Results.html',context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../afterReg/')
    else:
        form =UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})
