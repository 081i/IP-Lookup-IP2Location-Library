import os , colorama , msvcrt
import IP2Location , folium , time

from colorama import Fore , Style

text = """
  ___   ____    _              __     __  _____ 
 |_ _| |  _ \  | |             \ \   / / |___ / 
  | |  | |_) | | |      _____   \ \ / /    |_ \ 
  | |  |  __/  | |___  |_____|   \ V /    ___) |
 |___| |_|     |_____|            \_/    |____/ 
"""

# Using fade Lib 
def b(text):
    system(""); faded = ""
    red = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
        if not red > 200:
            red += 30
    return faded

TextF = b(text)
print(TextF)

filename = input(Fore.BLUE + '[INFO]' + Fore.WHITE + ':' + Fore.YELLOW + 'Enter The Path To The IP2Location .BIN file | ' + Fore.WHITE)
database = IP2Location.IP2Location(os.path.join('data', filename))
rec = database.get_all(input(Fore.BLUE + "[INFO]" + Fore.WHITE + ':' + Fore.YELLOW + 'Enter IP | ' + Fore.WHITE))
time.sleep(2)

print(Fore.GREEN + "-----")
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.country_short + Fore.BLUE + ' -- [COUNTRY_SHORT]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.country_long + Fore.BLUE + ' -- [COUNTRY_LONG]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.region + Fore.BLUE + ' -- [REGION]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.city + Fore.BLUE + ' -- [CITY]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.isp + Fore.BLUE + ' -- [ISP]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.latitude + Fore.BLUE + ' -- [LAT]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.longitude + Fore.BLUE + ' -- [LNG]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.domain + Fore.BLUE + ' -- [DOMAIN]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.zipcode + Fore.BLUE + ' -- [ZIPCODE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.timezone + Fore.BLUE + ' -- [TIMEZONE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.netspeed + Fore.BLUE + ' -- [NETSPEED]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.idd_code + Fore.BLUE + ' -- [IDD_CODE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.area_code + Fore.BLUE + ' -- [AREA_CDOE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.weather_code + Fore.BLUE + ' -- [WEATHER_CODE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.weather_name + Fore.BLUE + ' -- [WEATHER_NAME]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mcc + Fore.BLUE + ' -- [MCC]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mnc + Fore.BLUE + ' -- [MNC]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mobile_brand + Fore.BLUE + '[ -- MOBILE_BRAND]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.elevation + Fore.BLUE + ' -- [ELEVATION]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.usage_type + Fore.BLUE + ' -- [USAGE_TYPE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.address_type + Fore.BLUE + ' -- [ADDRESS_TYPE]')
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.category + Fore.BLUE + ' -- [CATEGORY]')
print(Fore.GREEN + "-----")

print(Fore.BLUE + '[SYSTEM]' + Fore.WHITE + ':' + Fore.LIGHTBLUE_EX + 'Generating IP Map File')
print(Fore.BLUE + '[INFO]' + Fore.WHITE + ':' + Fore.LIGHTYELLOW_EX + 'IF YOU HAVE ERROR UPGRADE DATA FILE')
time.sleep(3)
filename = "map.html"
count = 1

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
print(Fore.BLUE + '[SYSTEM]' + Fore.WHITE + ':' + Fore.GREEN + 'Generated!')
time.sleep(1.3)
filename = f'map{count}.html'
path = os.path.abspath(filename)
print(Fore.BLUE + '[INFO]' + Fore.WHITE + ':' + Fore.GREEN + 'Your Map File Is Saved At | ' + Fore.WHITE + f"{path}")
time.sleep(1.5)
print(Fore.WHITE + "Press Any Key To Exit...")
msvcrt.getch()
