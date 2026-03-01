from fastapi import FastAPI, Depends
from pydantic import BaseModel
from agent.agent import agent
from fastapi.middleware.cors import CORSMiddleware
from .auth import verify_backend_token

app = FastAPI(title="Weather Clothing Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    message: str


@app.post("/recommend", dependencies=[Depends(verify_backend_token)])
async def recommend(query: Query):
    try:
        result = await agent.run(query.message)
        return {
            "success": True,
            "recommendation": result.output
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        } 


@app.get("/") 
async def root(): 
    return {"message": "Weather Clothing Agent is running."}