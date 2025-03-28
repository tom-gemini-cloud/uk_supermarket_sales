import pandas as pd
import folium
from folium.plugins import HeatMap
import numpy as np

# Read the Excel file
df = pd.read_excel('input_data/Week_3_data.xlsx')

# Group by city and calculate total sales
city_sales = df.groupby('City')['Sales'].sum().reset_index()

# Create a base map centered on the UK
uk_map = folium.Map(location=[54.5, -2], zoom_start=6)

# Add markers for each city with sales data
for idx, row in city_sales.iterrows():
    # Note: In a real application, you would need to geocode the cities
    # For this example, we'll use approximate coordinates
    # You might want to use a geocoding service to get accurate coordinates
    folium.CircleMarker(
        location=[54.5, -2],  # Replace with actual coordinates
        radius=row['Sales']/1000,  # Scale the radius based on sales
        popup=f"{row['City']}: £{row['Sales']:,.2f}",
        color='red',
        fill=True,
    ).add_to(uk_map)

# Save the map
uk_map.save('sales_map.html')

print("Map has been created and saved as 'sales_map.html'") 