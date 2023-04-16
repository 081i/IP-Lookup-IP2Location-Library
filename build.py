import os , colorama , msvcrt
import IP2Location , folium , time

from colorama import Fore , Style

filename = input(Fore.BLUE + '[INFO]' + Fore.WHITE + ':' + Fore.YELLOW + 'Enter The Path To The IP2Location .BIN file | ' + Fore.WHITE)
database = IP2Location.IP2Location(os.path.join('data', filename))
rec = database.get_all(input(Fore.BLUE + "[INFO]" + Fore.WHITE + ':' + Fore.YELLOW + 'Enter IP | ' + Fore.WHITE))
time.sleep(2)

print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.country_short)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.country_long)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.region)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.city)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.isp)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.latitude)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.longitude)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.domain)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.zipcode)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.timezone)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.netspeed)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.idd_code)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.area_code)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.weather_code)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.weather_name)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mcc)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mnc)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.mobile_brand)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.elevation)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.usage_type)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.address_type)
print(Fore.BLUE + '[GAINED]' + Fore.WHITE + ':' + Fore.GREEN + rec.category)

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