import requests
import math
from math import sin, cos, sqrt, atan2, radians
import time
from datetime import datetime

locations = {}
def get_location(locs):
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    longitude = geo_data['longitude']
    latitude = geo_data['latitude']
    time_string = datetime.now().strftime("%H:%M:%S")
    pt = datetime.strptime(time_string,'%H:%M:%S')
    total_seconds = pt.second + pt.minute*60 + pt.hour*3600
    locs[total_seconds] = (latitude, longitude)
    

def get_distance(coord1, coord2):
    R = 6373.0
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
   
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2.0)**2.0 + cos(lat1) * cos(lat2) * sin(dlon / 2.0)**2.0
    c = 2.0 * atan2(sqrt(a), sqrt(1.0 - a))

    distance = R * c
    print("KM: " + str(distance))
    return float(distance*0.621371)



def main():
    # 37.751, -97.822
    a = 37.7510001
    b = -97.8220000
    c = 37.7510002
    d = -97.8220000
    total_miles = 0.0
    get_location(locations)
    time.sleep(5)

    
    while True:
       
        get_location(locations)
        time.sleep(5)
        
        time1 = int(list(locations.keys())[-1])
        time2 = int(list(locations.keys())[-2])

        distance = get_distance((a,b), (c,d))
        # print((float(locations[time1][0]), float(locations[time1][1])))
        # distance = get_distance((float(locations[time1][0]), float(locations[time1][1])), (float(locations[time2][0]), float(locations[time2][1])))
        print("DIST: " + str(distance))
        mph = distance/float(((time1-time2)/3600))
        print("MPH: " + str(mph))
        #print(time1)
        if (mph > 25.0):
            print("HEY pussy dont fuckig drive. you dont get those miles")
        else:
            total_miles += distance
        print("TOTAL MILES: " +str(total_miles))




main()
