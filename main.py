from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get("/api/v1/time")
async def get_timezone_details(timezone: str, api_key: str):
    if api_key != os.getenv("TIME_API_KEY"):
        raise HTTPException(status_code=403, detail="sorry but i cant recognize your api key..")

    try:
        timezone_now = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        raise HTTPException(400, detail="sorry but the timezone you inserted isnt right.. pls check it again!")


    now = datetime.now(timezone_now)
    which_day_of_year = now.timetuple().tm_yday

    hour = now.hour
    minute = now.minute

    return {"hour": hour, "minute": minute, "day_of_the_year": which_day_of_year}

@app.get("/api/v1/date")
async def get_timezone_date(timezone: str, api_key: str):
    if api_key != os.getenv("TIME_API_KEY"):
        raise HTTPException(status_code=403, detail="sorry but i cant recognize your api key..")

    try:
        timezone_now = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        raise HTTPException(400, detail="sorry but the timezone you inserted isnt right.. pls check it again!")

    now = datetime.now(timezone_now)
    month = now.month
    day = now.day
    year_all = now.year
    year = str(year_all)[2:5]
    return {"month": str(month), "day": str(day), "year": year}


if __name__ == "__main__":
    uvicorn.run(app)