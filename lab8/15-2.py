from geopy.geocoders import Nominatim
from xml.dom import minidom
geolocator = Nominatim(user_agent="yar")
f = open("15 -2.osm", encoding="utf8")
doc = minidom.parseString(f.read())
root = doc.documentElement
k=0
police_stations = []
for node in root.getElementsByTagName("node")+root.getElementsByTagName("way"):
    for tag in node.getElementsByTagName("tag"):
        if tag.getAttribute('k') == "amenity" and tag.getAttribute('v')== "police":
            k+=1
            address = []
            info = tuple()
            for tag in node.getElementsByTagName("tag"):
                if "addr" in tag.getAttribute('k'):
                    address.append(tag.getAttribute('v'))
            if not address:
                address = "No address in OSM file"
                if tag.parentNode.nodeName == "node":
                    parent = tag.parentNode
                    coords = (parent.getAttribute('lat'), parent.getAttribute('lon'))
                    location = geolocator.reverse(coords, exactly_one=True)
                    address = location.address
            else:
                address = ", ".join(address[::-1])
            police_stations.append((address,) + info)
police_stations.sort(key = lambda police_station: police_station[0])
for police_station in police_stations:
    print(police_station)
print(k)