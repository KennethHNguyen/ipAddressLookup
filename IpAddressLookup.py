import re, requests, sys

#Function to get the ip input and return table markdown
def ipRequest(ip):
    ipInfo = requests.get('http://ipinfo.io/' + str(ip)).json()     #Pull ip info into a dictionary
    #Spilt the longitude & latitude seperately into a tuple with a comma seperator then back into the dictionary
    ipInfo['longitude'] = ipInfo.get('loc', 'N/A,N/A').partition(',')[0]
    ipInfo['latitude'] = ipInfo.get('loc', 'N/A,N/A').partition(',')[2]

    #Extracting relevant singular values (Val) from the ipinfo lookup into variables
    countryVal = ipInfo.get('country', 'N/A')
    regionVal = ipInfo.get('region', 'N/A')
    cityVal = ipInfo.get('city', 'N/A')
    longVal = ipInfo.get('longitude', 'N/A')
    latVal = ipInfo.get('latitude', 'N/A')

    #Return info
    infoOutput = """Country: %s\nRegion: %s\nCity: %s\n\nLongitude: %s\nLatitude: %s""" % (countryVal, regionVal, cityVal, longVal, latVal)
    return infoOutput

ip = input('Please enter an IPv4 address: ')

#Input validation for scope of IPv4
ipRegex = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')   #Quick regex for IPv4
mo = ipRegex.search(ip)                                                 #Match object for regex

if mo == None:                                                          #If ip doesn't meet regex
    print('Not a valid IPv4 address.')
    sys.exit()
else:
    for i in mo.groups():
        if int(i) > 255 or (i !='0' and i < '1'):                    #If octet is greater than 255
            print('Not a valid IPv4 address.')
            sys.exit()

print(ipRequest(ip))
