import csv
import requests
import json
import xlsxwriter

# Set the user agent to support Persian text characters
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Read the coordinates from the input CSV file
with open('coordinates.csv', 'r') as f:
    reader = csv.reader(f)
    coordinates = [(float(row[0]), float(row[1])) for row in reader]

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('addresses.xlsx')
worksheet = workbook.add_worksheet()

# Loop through the coordinates and geocode them
for row, coordinate in enumerate(coordinates):
    latitude, longitude = coordinate
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={latitude}&lon={longitude}"

    # Make the request and parse the response
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    # Extract the address from the response
    address = data['display_name']

    # Write the coordinate and address to the Excel worksheet
    worksheet.write(row, 0, str(coordinate))
    worksheet.write(row, 1, address)

# Save the Excel file
workbook.close()
