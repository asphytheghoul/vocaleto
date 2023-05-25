from fastapi import FastAPI
import gpt4all
import time
app = FastAPI()
gptj = gpt4all.GPT4All("ggml-mpt-7b-chat")
@app.get("/query/{input}")
async def query(input: str):
    start = time.time()
    response = gptj.generate(input)
    end = time.time()
    return {"input": input,"content":response,"time taken":end-start}
    
