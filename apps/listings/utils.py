import math


def deg2rad(deg):
    return deg * (math.pi/180)


def get_distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    R = 6371
    latdiff = deg2rad(lat2-lat1)
    londiff = deg2rad(lon2-lon1)
    a = math.sin(latdiff/2) * math.sin(latdiff/2) +\
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.sin(londiff/2) * math.sin(londiff/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c  # distance in km #
    return d
