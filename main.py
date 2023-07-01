import os , colorama , msvcrt , IP2Location , folium , time
from colorama import Fore , Style
from fade import fire

text = """

✷ 　 　　 　 ·
 　 ˚ * .
 　 　　 *　　 * ⋆ 　 .
 · 　　 ⋆ 　　　 ˚ ˚ 　　 ✦
 　 ⋆ · 　 *
 　　　　 ⋆ ✧　 　 · 　 ✧　✵
 　 · ✵
 _  ___  _         _ _   __  
| || . \| |   ___ | | | /. | 
| ||  _/| |_ |___|| ' |/_  .|
|_||_|  |___|     |__/   |_| 

"""

TextF = fire(text)
print(TextF)

inputuser = Fore.RED + "[" + Fore.WHITE + ">>>" + Fore.RED + "]"
colon = Fore.WHITE + ':'
colon2 =  Fore.WHITE + ': '
yellow = Fore.YELLOW
white = Fore.WHITE
equals = Fore.WHITE + " == "
red = Fore.RED
wall = white + " | "
t = time.sleep(0.3)

filename = input(inputuser + colon + red + 'Enter The Path To The IP2Location .BIN file' + wall + yellow)
database = IP2Location.IP2Location(os.path.join('data', filename))
rec = database.get_all(input(inputuser + colon + red + 'Enter IP ' + wall + yellow))
time.sleep(3)

programOutput = inputuser = Fore.RED + "[" + Fore.WHITE + ">" + Fore.RED + "]"


b1 = red + "["
b2 = red + "]"

print(white + "----------------------------------------------------------")
print(programOutput + colon2 + red + rec.country_short + equals + b1 + white + "COUNTRY_SHORT" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.country_long + equals + b1 + white + "COUNTRY_LONG" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.region + equals + b1 + white + "REGION" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.city + equals + b1 + white + "CITY" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.isp + equals + b1 + white + "ISP" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.latitude + equals + b1 + white + "LAT" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.longitude + equals + b1 + white + "LNG" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.domain + equals + b1 + white + "DOMAIN" + b2 )
time.sleep(0.3)
print(programOutput + colon2 + red + rec.zipcode + equals + b1 + white + "ZIPCODE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.timezone + equals + b1 + white + "TIMEZONE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.netspeed + equals + b1 + white + "NETSPEED" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.idd_code + equals + b1 + white + "IDD_CODE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.area_code + equals + b1 + white + "AREA_CODE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.weather_code + equals + b1 + white + "WEATHER_CODE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.weather_name + equals + b1 + white + "WEATHER_NAME" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.mcc + equals + b1 + white + "MCC" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.mnc + equals + b1 + white + "MNC" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.mobile_brand + equals +  b1 + white + "MOBILE_BRAND" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.elevation + equals + b1 + white + "ELEVATION" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.usage_type + equals + b1 + white + "USAGE_TYPE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.address_type + equals + b1 + white + "ADDRESS_TYPE" + b2)
time.sleep(0.3)
print(programOutput + colon2 + red + rec.category + equals + b1 + white + "CATEGORY" + b2)
print(white + "----------------------------------------------------------")

foliumOutput = Fore.RED + "[" + Fore.WHITE + "FOLIUM" + Fore.RED + "]"
warn = Fore.RED + "[" + Fore.WHITE + "WARNING" + Fore.RED + "]"

print(foliumOutput + colon + red + "GENERATING MAP")
time.sleep(1.5)
print(warn + colon + red + "IF ERROR UPGRADE TO LAT & LNG")
time.sleep(6)
filename = "map.html"

count = 1
while os.path.isfile(f"map{count}.html"):
    count += 1
    if count > 10000:
        raise Exception("🥚")

lat = rec.latitude
lng = rec.longitude
location = rec.country_long

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat,lng],popup = location).add_to(myMap)
myMap.save(f'map{count}.html')
print(foliumOutput + colon + red + 'GENERATED')
time.sleep(1.3)
filename = f'map{count}.html'
path = os.path.abspath(filename)
time.sleep(3)
print(foliumOutput + colon + red + ' MAP PATH' + wall + red + f"{path}")
print(white + "----------------------------------------------------------")
time.sleep(1.5)
print(programOutput + colon + red + "TYPE TO EXIT")
msvcrt.getch()
