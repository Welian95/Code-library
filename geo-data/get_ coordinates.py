import geopy
from geopy.geocoders import Nominatim

def coordinates (adress):
    '''This is a function to get geocoordinates by a given adress
    param adress: string 
    output: l = latitude, b = longitude'''

    loc = Nominatim(user_agent="GetLoc")

    getLoc = loc.geocode(adress)

    b = getLoc.latitude
    l = getLoc.longitude
    return (b,l)

if __name__ == "__main__":
    b,l = coordinates('Münster')

    print (b,l)