import urllib.request as request
import json 
with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5") as response:
    data=json.load(response)

file=open("place.txt","w",encoding="utf-8")

keyword=input("捷運站名稱:")

list=data["result"]["results"]
for place in list:
    if keyword == place["MRT"]:
        file.write(place["stitle"]+"\n")
        
file.close()