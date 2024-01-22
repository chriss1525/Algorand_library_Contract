import beaker
import pyteal as pt
from pyteal import *
import random


app = beaker.Application("wordle")

# List of scrambled words
scrambled_words = ["lepapl", "nabana", "yrcneh", "etad", "yrebder"]
words = ["apple", "banana", "cherry", "date", "berry"]


@app.external
def generate_word(*, output: pt.abi.String) -> pt.Expr:
    # Select a random scrambled word from the list
    Sword = random.choice(scrambled_words)
    return output.set(Sword)


@app.external
def check_answer(guess: pt.abi.String, *, output: pt.abi.Bool) -> pt.Expr:
    # Check if the guess is in the list of scrambled words
    return output.set(guess in words)
