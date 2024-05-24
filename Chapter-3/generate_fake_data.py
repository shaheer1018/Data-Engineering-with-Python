from faker import Faker
import csv
import json
import pandas as pd
import pandas.io.json as pd_JSON

# # Create a new CSV file and open it in write mode
# output = open('data.CSV', 'w')

# # Instantiate the Faker object
# fake = Faker()

# # Define the header for the CSV file
# header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

# # Create a CSV writer object
# mywriter = csv.writer(output)

# # Write the header to the CSV file
# mywriter.writerow(header)

# # Write 1000 rows of fake data to the CSV file
# for r in range(1000):
#     mywriter.writerow([fake.name(), fake.random_int(min=18, max=80, step=1), fake.street_address(), 
#                        fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])

# # Close the CSV file
# output.close()



# # Create a new JSON file and open it in write mode
# output = open('data.JSON', 'w')

# # Instantiate the Faker object
# fake = Faker()

# # Create a dictionary to store data
# alldata = {}
# # Add a records key and initialize it with a blank array
# alldata['records'] = []

# for x in range(1000):
#     data = {"name": fake.name(), "age": fake.random_int(min=18, max=80, step=1),
#             "street": fake.street_address(), "city": fake.city(), "state": fake.state(),
#             "zip": fake.zipcode(), "lng": float(fake.longitude()), "lat": float(fake.latitude())}
#     alldata['records'].append(data)
    
# # write the JSON to a file
# json.dump(alldata, output)


# In the case of the data.JSON file, the records are nested in a records dictionary. 
# So, loading the JSON is not as straightforward. 
# You will need a few extra steps, which are as follows.
import pandas.io.json as pd_JSON

# # Open the file and load it with the pandas version of JSON.loads()

#===============================================
#                 NOTE
#===============================================
# This part of code was causing issues because I was not commenting the code above which is being used to
# generate the JSON file before loading it. 
f = open('data.JSON','r')
data = pd_JSON.loads(f.read())

df = pd_JSON.json_normalize(data, record_path = 'records')

print(df)

# # Load the JSON file using pd_JSON
# loaded_data = pd_JSON.read_json('data.JSON')

# # Now you can work with the loaded data
# print(loaded_data)

# # Convert the JSON data to a DataFrame
# df = pd.json_normalize(loaded_data)

# print(df)

# f=open('data.JSON','r')

# data=pd_JSON.loads(f.read())

# #     data = pd_JSON.loads(f.read())

# # # To create the DataFrame, we need to normalize the JSON. Normalizing is how you can flatten the
# # # JSON to fit in a table.
# # # In this case, you want to grab the individual JSON records held in the records dictionary. 
# # # Pass that path – records – to the record_path parameter of json_normalize()
# # df = pd_JSON.json_normalize(data, record_path = 'records')

# # print(df.head())
