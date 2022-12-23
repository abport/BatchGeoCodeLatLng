# BatchGeoCodeLatLng

# Batch Geocoding Coordinates to addresses in Python using the OpenStreetMap Nominatim API

Do you know what geocoding is? It’s a way of turning a location (like a street address or a set of GPS coordinates) into information about that location (like the name of the city or country). This can be really helpful if you want to know where something is or if you want to find out more about a place.

In this tutorial, we’re going to learn how to use Python, a programming language, to geocode a list of GPS coordinates. We’ll be using a tool called the OpenStreetMap Nominatim API, which is a website that can turn coordinates into addresses for us.

First, let’s start by setting up our Python script. We’ll need to import a few libraries to help us make web requests and parse the response we get back from the API. Here’s what that looks like:

```python 
import csv
import requests
import json
```



```python
# Set the user agent to support Persian text characters
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
```

Next, we need to read in the list of coordinates that we want to geocode. We’ll be using a CSV file for this, which is a type of spreadsheet that stores data in rows and columns. Here’s how we can read the coordinates from the CSV file:


```python
# Read the coordinates from the input CSV file
with open('coordinates.csv', 'r') as f:
    reader = csv.reader(f)
    coordinates = [(float(row[0]), float(row[1])) for row in reader]
```
Now that we have our list of coordinates, we can start geocoding them one by one. To do this, we’ll use a loop to go through each coordinate in the list and make a request to the API with the coordinate. The API will then return a response with the address for that coordinate, which we can extract and print out. Here’s what the loop looks like:

```python
# Loop through the coordinates and geocode them
for coordinate in coordinates:
    latitude, longitude = coordinate
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={latitude}&lon={longitude}"

    # Make the request and parse the response
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    # Extract the address from the response
    address = data['display_name']
    print(f"Coordinate: {coordinate} => Address: {address}")
```

And that’s it! We’ve written a Python script that can geocode a list of GPS coordinates using the OpenStreetMap.

To use the script that I provided in the previous response, you’ll need to create a CSV file called  `coordinates.csv`  that contains the coordinates that you want to geocode. The CSV file should be formatted like this:

    latitude1,longitude1
    latitude2,longitude2
    latitude3,longitude3
    ...

Each line in the file should contain a single coordinate in the format  `latitude,longitude`, where  `latitude`  is the number of degrees north or south of the equator and  `longitude`  is the number of degrees east or west of the Prime Meridian. The coordinates should be separated by a comma, and there should be no spaces between the numbers and the commas.

Here’s an example of what the  `coordinates.csv`  file might look like for a list of three coordinates:

    38.0863,46.2918
    35.6892,51.3890
    48.8566,2.3522
    40.7128,-74.0060

These coordinates correspond to the following locations:

-   Tabriz, Iran
-   Tehran, Iran
-   Paris, France
-   New York, USA

You can add as many coordinates as you like to the list, just make sure to follow the format  `latitude,longitude`  and separate each coordinate with a newline.

Once you’ve created the  `coordinates.csv`  file and added your coordinates to it, you can run the Python script to geocode the coordinates and print the results to the console. The script will loop through each coordinate in the list, make a request to the API with the coordinate, and extract and print the address from the API response.

