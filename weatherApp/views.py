from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        parsed_data = json.loads(res)
        data = {
            "country_code": str(parsed_data['sys']['country']),
            "coordinate": str(parsed_data['coord']['lon']) + ' ' +
            str(parsed_data['coord']['lat']),
            "temp": str(parsed_data['main']['temp'])+'k',
            "pressure": str(parsed_data['main']['pressure']),
            "humidity": str(parsed_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
