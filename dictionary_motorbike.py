bike = {"make": "Honda", "model": "250 dream", "colour": "Red", "engine_size": 250}
# make, model, colour and engine_size are keys and the related info is the value
print(bike['engine_size'])
print(bike['colour'])

bike_keys = bike.keys()
print(bike_keys)

bike["year"] = 2015
print(bike_keys)

print(bike)
print(bike.items())