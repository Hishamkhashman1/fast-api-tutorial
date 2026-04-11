
# import fastapi as fastapi
from fastapi import FastAPI, HTTPException

# Import Enum for creating Enums
from enum import Enum


# define the Enum class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



# define the app as a FastAPI object
app = FastAPI()


# simple HTTP GET endpoint for a FastAPI app

# Register this function as a route handler, it tells FastAPI that when a user makes a GET request to the root URL, the function below will be executed
@app.get("/") 

#An asynchronous function (often marked with async) allows a program to start a potentially long-running task—such as fetching data, accessing a database, or loading a file—without freezing the entire program. RUNS IN PARALLEL THAT IS.
async def root(): 
    # FastAPI automatically converts this python dictionary to JSON format and sends it as the HTTP response
    return {"hello":"from","fastapi":"world"}

#Path parameters with type example

@app.get("/charecters/{charecter_id}")
async def get_char(charecter_id: int):
    return {"charecter_id": charecter_id}

# path parameters with a type annotation using the enum class previously created
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



