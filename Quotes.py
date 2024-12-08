from fastapi import FastAPI
import random
import uvicorn
from pydantic import BaseModel

# Initialize the app
app = FastAPI()

# Sample quotes
quotes = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

# GET: Fetch a random quote
@app.get("/get-quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}

# POST: Add a new quote
class QuoteRequest(BaseModel):
    new_quote: str

@app.post("/create-quote")
def add_quote(quote_request: QuoteRequest):
    quotes.append(quote_request.new_quote)
    return {"message": "Quote added successfully!", "total_quotes": len(quotes)}

# Run this app using `uvicorn`
if __name__ == "__main__":
    uvicorn.run("Quotes:app", host="127.0.0.1", port=8000, reload=True)