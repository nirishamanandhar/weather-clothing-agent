from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import agent

app = FastAPI(title="Weather Clothing Agent API")


class Query(BaseModel):
    message: str


@app.post("/recommend")
async def recommend(query: Query):
    try:
        import os 
        print("ENV:", os.environ)
        result = await agent.run(query.message)
        return {
            "success": True,
            "recommendation": result.output()
            }
    except Exception as e:
        import traceback 
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e)
        } 


@app.get("/") 
async def root(): 
    return {"message": "Weather Clothing Agent is running."}