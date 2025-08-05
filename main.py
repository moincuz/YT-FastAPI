from fastapi import FastAPI
from enum import Enum

fastic = FastAPI() ## FastAPI instance we can name it as we wish, usually this called the'app'

@fastic.get("/hello")
async def hello():
    return "Welcome to FastAPI World! This is a simple API"

@fastic.get("/hello/{name}") ## {name} is a path parameter, it is a variable that is part of the URL
##Provide a good URL explanation in swagger UI, and also provide a good description of the API
async def raspechatay_svoe_imya(name):
    return f"Welcome to FastAPI World! This is a simple API {name}"

########################################################

food_items = { ## This is a dictionary, it is a collection of key-value pairs

'indian':[ "Tandoori Chicken", "Naan", "Chana Masala"],
'american':[ "Burger", "Cola"],
'italian':[ "Pizza", "Pasta"],
'mexican':[ "Taco", "Burrito"],
'japanese':[ "Sushi", "Ramen"],
'russian':[ "Pelmeni", "Blini"],
'chinese':[ "Dim Sum", "Spring Rolls"],
'korean':[ "Kimchi", "Bibimbap"],
'thai':[ "Pad Thai", "Tom Yum Goong"],
'vietnamese':[ "Pho", "Banh Mi"],
}
valid_cuisines = food_items.keys()

@fastic.get("/get_items/{cousine_name}")
async def nazvanie_kuxni_po_vkusu(cousine_name):
    '''
    This is a function that returns the name of the cuisine by the name of the cuisine
    '''
    if cousine_name not in valid_cuisines:
        return {"error": "Invalid cuisine name. Please use our menu instead"}
    return f"Nazvanie kuxni po vkusu : {cousine_name}: {food_items.get(cousine_name)}"
    

########################################################
class AvailableCousine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


@fastic.get("/get_menu_items/{from_cousine_name}")
async def nazvanie_blud(from_cousine_name: AvailableCousine):
    return f"Names of dishes: {food_items.get(from_cousine_name)}"
########################################################

cupon_code = {
 1: "10%",
 2: "20%",
 3: "30%"
}

@fastic.get("/get_coupon/{code}")
async def get_coupon(code: int):
    return f"You discount is  {cupon_code.get(code)}"








