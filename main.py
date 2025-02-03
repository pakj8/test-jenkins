from fastapi import FastAPI, Query
import requests # type: ignore
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape")
async def scrape(url: str = Query(..., description="URL to scrape")):
    """Scrapes the given URL and returns the page title."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        
        return {"url": url, "title": title}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
