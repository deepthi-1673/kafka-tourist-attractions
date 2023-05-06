import csv

# Example data
data = [
    {'state': 'California', 'attraction': 'Disneyland'},
    {'state': 'California', 'attraction': 'Golden Gate Bridge'},
    {'state': 'New York', 'attraction': 'Statue of Liberty'},
    {'state': 'New York', 'attraction': 'Central Park'},
    {'state': 'Florida', 'attraction': 'Universal Studios'},
    {'state': 'Florida', 'attraction': 'Walt Disney World'},
]

# Open CSV file for writing
with open('tourist_attractions.csv', mode='w', newline='') as file:
    # Define the header row
    fieldnames = ['state', 'attraction']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for item in data:
        writer.writerow(item)
