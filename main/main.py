from config import OPEN_AI_API_KEY;
import os 
import openai

openai.api_key = OPEN_AI_API_KEY


input = "Tell me a joke"
res = openai.Completion.create (
    model = "text-davinci-003",
    prompt = input,
    temperature = 150,
    max_tokens = 150,
    top_p = 1.0,
    frequency_penalty = 0.0,
    presence_penalty = 0.0
)

print(res)