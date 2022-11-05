import openai
from api_key import api_key
from fastapi import FastAPI
import uvicorn

openai.api_key = api_key

app = FastAPI()

@app.get("/{name}")
async def get_name(name: str):
  return "Hello, Nice to meet you {}".format(name)

@app.post("/predict")
async def get_image(prompt: str):
  response = openai.Image.create(
    prompt = prompt,
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']
  return {"The Desired Image in Present here: ": image_url}

if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 8000)