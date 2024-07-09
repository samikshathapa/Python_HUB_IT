# We need json module to read and write JSON files
import json

# Sample data
data = {
    "name": "Ram",
    "age": 30,
    "city": "Bhaktapur"
}

# Writing JSON Object to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Reading JSON Object from a file
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)