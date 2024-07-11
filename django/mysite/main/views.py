from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# Create your views here.

def test(request):
    s = "<html><head><title>test 파일</title>"
    s += "<script src='//code.jquery.com/jquery.min.js'></script>"
    s += "</head>"
    s += "<body><h1>Hello World</h1>"
    s += "<nav><a href='https://naver.com' style='color: green'>네이버\
        <img width=200 src='https://postfiles.pstatic.net/MjAyMjExMDZfNDEg/MDAxNjY3NzM4NTgxMDQw.WxBKldkyGgW3DV9TCvbRioz_wA6ligR2Ua_AXyHeTG8g.G0YAUTe9x9q8i-5h2NUuFH1hady32rdkZLzKo_WQavgg.PNG.josephk1010/Naver-logo.png?type=w966'>\
        </a><input type='checkbox' name='platform' value='naver'></input></nav>"
    s += "<nav><a href='https://daum.net' style='color: blue'>다음\
        <img width=200 src='https://postfiles.pstatic.net/MjAyNDA2MTBfMTA3/MDAxNzE3OTk1NjA3MjEw.A0VGzbCk5tpj4JRpFBkUj8aMUuCOxABMAB4OHUv4FEMg.ycCi-7hr5CnLWtamJtmvKw4HgQfOAJS9VMaGgCv7sTIg.PNG/pngwing.com.png?type=w966'>\
        </a><input type='checkbox' name='platform' value='daum'></input></nav>"
    s += "<br><button id='check'>checkbox submit</button>"
    s += "<script type='text/javascript'>\
            $('#check').on('click', function() {\
                var check = '';\
                $('input[type=checkbox][name=platform]:checked').each(function(e){\
                    check += $(this).val();\
                });\
                alert(check + ' checked!');\
            })\
          </script>"
    s += "<br><button onclick='test()'>button</button><br>"
    s += "<script type='text/javascript'>function test() { alert('button clicked!') }</script>"
    
    # OpenWeather API
    api_key = "d8caa3fb6432f6cf43af2ea0c3e6f269"
    
    s += "<br><label>City </label>"
    s += "<input id='city'></input>"
    s += "<button id='weather'>현재 날씨 보러가기</button>"
    s += "<script type='text/javascript'>"
    s += "$(document).ready(function(){"
    s += "$('#weather').click(function() {"
    s += "var city = $('#city').val();"
    s += "var latitude;"
    s += "var longitude;"
    s += "var city_ko;"
    s += "var temperature;"
    s += "$.ajax({"
    s += "type: 'GET',"
    s += "async: false,"
    s += f"url: 'http://api.openweathermap.org/geo/1.0/direct?q='+city+'&limit=1&appid={api_key}',"
    s += "success: function (response) {"
    s += "latitude = response[0]['lat'];"
    s += "longitude = response[0]['lon'];"
    s += "city_ko = response[0]['local_names']['ko'];"
    s += "},"
    s += "error: function (response) {"
    s += "console.log('error');"
    s += "},"
    s += "});"
    s += "$.ajax({"
    s += "type: 'GET',"
    s += "async: false,"
    s += f"url: 'https://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&units=Metric&appid={api_key}',"
    s += "success: function (response) {"
    s += "temperature = response['main']['temp'];"
    s += "},"
    s += "error: function (response) {"
    s += "console.log('error');"
    s += "},"
    s += "});"
    s += "alert(city_ko + '의 기온은 ' + temperature + '°C 입니다.');"
    s += "})"
    s += "})"
    s += "</script>"
    
    # get latitude, longitude
    lat_lon_url = f"http://api.openweathermap.org/geo/1.0/direct?q=Seoul&limit=1&appid={api_key}"
    
    lat_lon = requests.get(lat_lon_url).text
    
    lat_lon = lat_lon.strip("[]")
    lat_lon_json = json.loads(lat_lon)
    latitude = lat_lon_json["lat"]
    longitude = lat_lon_json["lon"]
    city = lat_lon_json["local_names"]["ko"]
    
    # get current weather data
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=Metric&appid={api_key}"
    
    weather = requests.get(weather_url).text
    weather_json = json.loads(weather)
    temperature = round(weather_json["main"]["temp"], 1)
    
   
    s += "<div><button onclick='alert_weather()'>서울 날씨 보러가기</button></div>"
    s += "<script type='text/javascript'>function </script>"
    s += f"<script type='text/javascript'>function alert_weather() {{ alert('현재 {city}({latitude}, {longitude})의 기온은 {temperature}°C입니다') }}</script>"

    
    # r = requests.get('https://google.com')
    # s += r.text
    
    s += "</body></html>"
    
    return HttpResponse(s)

def index(request):
    # return HttpResponse("Hello, world. You're at the main index.")
    return render(request, 'templates/main/test.html')