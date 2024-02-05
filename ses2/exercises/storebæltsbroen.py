# https://python-elective-kea.github.io/spring2024/ses2.html#ex-6-storebaelt


#cars dicts med key value pairs
cars = {
    '0001': {
        'color': 'red',
        'passenger_amount': 2,
        'car_length': 180
    },
    '0002': {
        'color': 'black',
        'passenger_amount': 3,
        'car_length': 170
    }
}

print(cars['0001'])
print(cars.get('0001'))

for regnr,values in cars.items():
    print(f"""
        {regnr}: color: {values["color"]}, 
        passengers: {values["passenger_amount"]}, 
        length: {values["car_length"]}
    """)


# eller: cars dicts med tuples indeni
cars_2 = {
    '0001': ('red', 2, 180),
    '0002': ('black', 3, 170)
}

