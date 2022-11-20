from models.Buoy import CO2, Buoy, Data, Tide


def BuoySchema(buoy):
    return Buoy(
        id=buoy['_id'],
        name=buoy['name'],
        data=list(map(lambda x: Data(**x), buoy['data'])),
        CO2=CO2(**buoy['CO2']),
        Tide=Tide(**buoy['Tide']),
        wind=buoy['wind'],
        date=buoy['date'],
        time=buoy['time'],
        lat=buoy['lat'],
        lng=buoy['lng']
    )
