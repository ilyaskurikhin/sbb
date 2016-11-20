import requests
import time
import sys
import csv

def get_station_location(station_name):
    response = requests.get("http://transport.opendata.ch/v1/locations?query={0}".format(station_name))
    if int(response.headers['X-Rate-Limit-Remaining']) < 1:
        time.sleep(1)
    try:
        station = (response.json()['stations'][0]['name'],
                float(response.json()['stations'][0]['coordinate']['x']),
                float(response.json()['stations'][0]['coordinate']['y']))
    except IndexError:
        station = ("not found",0,0)
    return station

def save_to_file(stations):
    with open('locations.csv','w',newline='') as file:
        writer = csv.writer(file, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for station in stations:
            row = [station[0], str(station[1]), str(station[2])]
            writer.writerow(row)

def read_from_file(filename):
    station_locations = []
    with open(filename,newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';',quotechar='|')
        for row in reader:
            station_locations.append(row[0],float(row[1]),float(row[2]))

def get_locations(station_names):
    station_locations = []
    index = 0 
    for station in station_names:
        pct = 100*index / len(station_names)
        print("\rWe are {0:.2f}% complete. Currect station : {1}".format(pct,station))
        index += 1
        station_locations.append(get_station_location(station))
    return station_locations

