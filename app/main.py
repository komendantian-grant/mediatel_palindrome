"""
Main module, runs fastapi and handles palindrome requests.
"""

from fastapi import FastAPI, Request
from make_palindrome.make_palindrome import make_palindrome

app = FastAPI()

@app.post("/")
async def process_word(request: Request):
    """
    Provides a method which listens for a possible scrambled palindrome
    and returns the resulting lexicographically smallest palindrome
    produced with the least number of swaps
    or null if producing a palindrome is impossible.
    :param request: Request, containing the json with input string.
    :return: Json with the resulting palindrome or null.
    """
    body = await request.json()
    word : str = body["word"]
    palindrome : str | None = make_palindrome(word)
    return {"palindrome": palindrome}
