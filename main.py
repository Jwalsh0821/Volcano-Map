import folium
import pandas

# pandas csv processing
vdata = pandas.read_csv('volcano.csv')
lat = list(vdata["Latitude"])
long = list(vdata["Longitude"])
vnames = list(vdata["V_Name"])
vrisk = list(vdata["risk"])

# feature creation
mp = folium.Map(location=[37, -80],  zoom_start=4)

fg = folium.FeatureGroup(name="My Map")
for la, lo, name, risk in zip(lat, long, vnames, vrisk):
    color = "green"
    try:
        r = float(risk)
        if r == 1:
            color = "orange"
        elif r == 2:
            color = "red"
        elif r >= 3:
            color = "darkred"
    except ValueError:
        color = "green"
    fg.add_child(folium.Marker(
        location=[la, lo], popup=name, icon=folium.Icon(color=color)))

mp.add_child(fg)
mp.save("Map1.html")
