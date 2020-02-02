import requests
import time
from datetime import datetime
from geopy.distance import geodesic

locations = {}
def get_location(locs):
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    latitude = geo_data['latitude']
    longitude = geo_data['longitude']
    time_string = datetime.now().strftime("%H:%M:%S")
    pt = datetime.strptime(time_string,'%H:%M:%S')
    total_seconds = pt.second + pt.minute*60 + pt.hour*3600
    locs[total_seconds] = (latitude, longitude)    

def get_distance(coord1, coord2):
    distance = geodesic(coord1, coord2).miles
    return distance

if __name__ == "__main__":
    # 37.751, -97.822
    # a = 37.7510001
    # b = -97.8220000
    # c = 37.7510002
    # d = -97.8220000
    # a = 37.7510
    # b = -97.8220
    # c = 37.7511
    # d = -97.8220
    total_miles = 0.0
    get_location(locations)
    
    while True:
        # poll new location every 5 seconds
        time.sleep(5)
        get_location(locations)
        
        time1 = int(list(locations.keys())[-1])
        time2 = int(list(locations.keys())[-2])

        # distance = get_distance((a,b), (c,d))
        print((float(locations[time1][0]), float(locations[time1][1])))
        print((float(locations[time2][0]), float(locations[time2][1])))
        distance = get_distance((float(locations[time1][0]), float(locations[time1][1])), (float(locations[time2][0]), float(locations[time2][1])))
        print("DIST: " + str(distance))
        mph = distance / float(((time1-time2)/3600))
        print("MPH: " + str(mph))
        if (mph > 20.0):
            print("WHOA that's too fast! Make sure you're not driving to qualify for the discounts.")
        else:
            total_miles += distance
        print("TOTAL MILES: " + str(total_miles))


