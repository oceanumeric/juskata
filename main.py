from juskata import Num2Words
from fastapi import FastAPI
from pydantic import BaseModel


class Num(BaseModel):
    lang: str = "FR"
    num: int


class NumList(BaseModel):
    lang: str = "FR"
    num: list[int]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Jus Mundi"}


# post request for convereting one number to words
@app.post("/convert_num/")
async def convert_num(num: Num):
    if num.lang in ["FR", "BE"]:
        return {"frenchWord": Num2Words(lang=num.lang).convert_num(num.num)}
    else:
        return {"message": "Language not supported"}


# post request for converting list of numbers to words
@app.post("/convert_num_list/")
async def convert_num_list(num: NumList):
    if num.lang in ["FR", "BE"]:
        return {"frendWrods": Num2Words(lang=num.lang).convert_num_list(num.num)}
    else:
        return {"message": "Language not supported"}
