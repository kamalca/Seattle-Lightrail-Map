from time import sleep
import os
from onebusaway import OnebusawaySDK
from tabulate import tabulate
client = OnebusawaySDK(api_key=os.environ['OBA_API_KEY'])
def print_stops(line):
    trips = client.trips_for_route.list(line)
    ret = []
    for trip in trips.data.list:
            stop = client.stop.retrieve(trip.status.next_stop)
            trip_info = client.trip.retrieve(trip.trip_id).data.entry
            ret.append([stop.data.entry.name, trip_info.trip_headsign, trip.status.status, trip.status.next_stop_time_offset, trip.status.closest_stop_time_offset])
    return ret

twoline = "40_2LINE"
oneline="40_100479"
monorail = "96_SCM"

while 1:
    info = []
    info += print_stops(oneline)
    info += print_stops(twoline)
    info += print_stops(monorail)
    print(tabulate(info, headers=["Next Stop", "Destination", "Status", "Time Next Stop", "Time Closest Stop"]))
    print("\n\n")
    sleep(10)
