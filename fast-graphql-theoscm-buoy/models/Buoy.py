from typing import Optional
import strawberry




@strawberry.type
class CO2 :
    data: list[int]
    categories: list[str]
@strawberry.type
class Tide :
    data: list[float]
    categories: list[str]
 

@strawberry.type
class Data:
    id: str
    name: str
    value: float
    
@strawberry.type
class Buoy:
      id: str
      name: str
      data: list[Data]
      CO2: CO2
      Tide: Tide
      wind: int
      date: str
      time: str
      lat: float
      lng: float



# need strawberry.input to make it work
@strawberry.input
# data input
class DataInput:
    id: str
    name: str
    value: float

@strawberry.input
# CO2 input
class CO2Input:
    data: list[int]
    categories: list[str]  


@strawberry.input
# Tide input
class TideInput:
    data: list[float]
    categories: list[str]