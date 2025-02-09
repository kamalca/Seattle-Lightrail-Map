def update_pixels(indexes):
    for i in range(len(pixels)):
            if i in indexes:
                    pixels[i] = (255,0,0)
            else:
                    pixels[i] = (0,0,255)


def get_stop_ids(line):
    trips = client.trips_for_route.list(line)
    ret = []
    for trip in trips.data.list:
            ret.append(trip.status.next_stop)
    return ret
