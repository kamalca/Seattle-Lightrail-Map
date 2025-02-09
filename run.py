from time import sleep
import os
from onebusaway import OnebusawaySDK
from tabulate import tabulate
import board
import neopixel
from stops import stops

client = OnebusawaySDK(api_key=os.environ['OBA_API_KEY'])
oneline="40_100479"
twoline = "40_2LINE"

pixels = neopixel.NeoPixel(board.D18, 100, pixel_order=neopixel.RGB)

def print_stops(line):
    trips = client.trips_for_route.list(line)
    ret = []
    for trip in trips.data.list:
            stop = client.stop.retrieve(trip.status.next_stop)
            trip_info = client.trip.retrieve(trip.trip_id).data.entry
            ret.append([stop.data.entry.name, trip_info.trip_headsign, trip.status.status, trip.status.next_stop_time_offset, trip.status.closest_stop_time_offset])
    return ret

def update_pixels(indexes, color):
    for i in range(len(pixels)):
            if i in indexes:
                    pixels[i] = color


def get_stop_ids(line):
    trips = client.trips_for_route.list(line)
    ret = []
    for trip in trips.data.list:
            ret.append(trip.status.next_stop)
    return ret


while 1:
    info = []
    info += print_stops(oneline)
    info += print_stops(twoline)
    print(tabulate(info, headers=["Next Stop", "Destination", "Status", "Time Next Stop", "Time Closest Stop"]))
    update_pixels(range(len(pixels)), (0, 0, 0))
    update_pixels([stops.index(x) + 2 for x in get_stop_ids(oneline)], (0, 150, 0))
    update_pixels([stops.index(x) + 2 for x in get_stop_ids(twoline)], (0, 0, 150))
    sleep(10)
    print("\n\n")
