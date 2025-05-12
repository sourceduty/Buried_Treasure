import folium

# Define 10 suggested treasure burial locations for 2025
locations = [
    {"name": "Snaefellsnes Peninsula, Iceland", "lat": 64.8333, "lon": -23.1167},
    {"name": "Torngat Mountains, Canada", "lat": 58.5000, "lon": -63.5000},
    {"name": "Drakensberg Mountains, South Africa", "lat": -29.3500, "lon": 29.6000},
    {"name": "Altai Mountains, Mongolia", "lat": 48.0000, "lon": 88.0000},
    {"name": "Khao Sok National Park, Thailand", "lat": 8.9180, "lon": 98.5268},
    {"name": "Valle de Cocora, Colombia", "lat": 4.6370, "lon": -75.5078},
    {"name": "Kamchatka Peninsula, Russia", "lat": 56.0000, "lon": 160.0000},
    {"name": "Trango Towers, Pakistan", "lat": 35.7422, "lon": 76.1544},
    {"name": "Fiordland National Park, New Zealand", "lat": -45.4170, "lon": 167.7180},
    {"name": "Namib Desert Canyons, Namibia", "lat": -24.7380, "lon": 15.2650},
]

# Initialize the map centered globally using OpenStreetMap
map_center = [10, 0]
treasure_map = folium.Map(location=map_center, zoom_start=2, tiles='OpenStreetMap')

# Add each location as a marker
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["name"],
        icon=folium.Icon(color='orange', icon='star')
    ).add_to(treasure_map)

# Save to an HTML file
treasure_map.save("treasure_locations_map.html")
print("Map saved as 'treasure_locations_map.html'")
