import datetime
import strawberry
from bson import ObjectId

from config.database import connection
from models.Buoy import CO2, Buoy, CO2Input, Data, DataInput, Tide, TideInput
from schemas.BuoySchema import BuoySchema

# connect to database
db = connection['BuoysNetwork']

# connect to collection
buoys = db['buoys']




@strawberry.type
class Query:
     # get all buoys from database as an array
 
    def getAllTheBuoys(self) -> list[Buoy]:

        allbuoys = []
        for buoy in buoys.find():
            allbuoys.append(
                BuoySchema(buoy)
            )
        return allbuoys


    def getABuoy(self) -> Buoy:
        # get the first buoy from database
        buoy = buoys.find_one()
        return BuoySchema(buoy)
        # {"_id": ObjectId(id)}
        # for learing purpose
        # return Buoy(
        #     id=result['_id'],
        #     name=result['name'],
        #     # alternative of data list of lambda function (valid)
        #     # data=[Data(id=data['id'], name=data['name'], value=data['value']) for data in result['data']],
        #     # alternative of above data list of lambda function (valid)
        #     # data=list(map(lambda data: Data(id=data['id'], name=data['name'], value=data['value']), result['data'])),
        #     # another alternative of above data list of lambda function (valid)
        #     data=list(map(lambda x: Data(**x), result['data'])),
        #     #co2 a dictornary with two keys data and categories will be converted to a CO2 object
        #     CO2=CO2(**result['CO2']),
        #     Tide=Tide(**result['Tide']),
        #     wind=result['wind'],
        #     date=result['date'],
        #     time=result['time'],
        #     lat=result['lat'],
        #     lng=result['lng']
        # )

    AllBuoys: bool = strawberry.field(resolver=getAllTheBuoys)
    Buoy: Buoy = strawberry.field(resolver=getABuoy)


@strawberry.type
class Mutation:
    # add a new buoy to database
    @strawberry.mutation
    def addBuoy(self,id:int, name: str, data: list[DataInput], CO2: CO2Input, Tide: TideInput, wind: int, date: datetime.date, time: datetime.time, lat: float, lng: float) -> bool:
        try:
            newBuoy = {
                "id": id,
                "name": name,
                "data": list(map(lambda x: x.__dict__, data)),
                "CO2": CO2.__dict__,
                "Tide": Tide.__dict__,
                "wind": wind,
                "date": date.isoformat(),
                "time": time.isoformat(),
                "lat": lat,
                "lng": lng
            }
            buoys.insert_one(newBuoy)
            return True
        except:
            return False