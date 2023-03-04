from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            city_res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=dd7754a6860e94c1b2e91ebf32b894cf').read()
        except:
            return render(request, 'index.html')
        json_data = json.loads(city_res)
        city_data = {
            "country_code": str(json_data['sys']['country']),
            "coordinates": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])       
        }
    else:
        city_data = {}
    return render(request, 'index.html', {'city': city_data})