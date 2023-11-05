from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DUMMY_DATA = [
    {
        "id": 1,
        "text": "This is the first item"
    },
    {
        "id": 2,
        "text": "This is the second item",
        "extraText": "This one has a little extra text"
    }
]


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/data", tags=["data"])
async def get_data() -> dict:
    return {"data": DUMMY_DATA}
