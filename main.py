from fastapi import FastAPI , Request
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import cohere

load_dotenv()
app=FastAPI()

api_key=os.getenv('LLM_API_KEY')
client=cohere.Client(api_key=api_key)


class summraizeContent(BaseModel):
    content:str
    


@app.post('/summarize')
async def summraize_text(request:summraizeContent):
    content=request.content
    response=client.generate(
        prompt=f'summrize this content in 70 words:{content}',
        max_tokens=100
    )
    summary=response.generations[0].text.strip()
    
    if not summary:
        return ({'summary': content[:70]})
    else:
    
        return({"summary": summary})
    # summary=content[:70]
    # return({"summary": summary})


@app.get('/')
def loadPage():
    return {'message':"messege"}
    