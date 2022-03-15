from fastapi import FastAPI
from scraper import Scraperates

app = FastAPI()

currencies = Scraperates()


@app.get("/spot")
async def read_item():
    return currencies.scrapedatarates()


