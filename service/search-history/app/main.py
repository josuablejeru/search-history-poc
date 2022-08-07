from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/session/{org_id}/{user_id}")
async def session(org_id, user_id):
    return {"org_id": org_id, "user_id": user_id}


@app.get("/history/{org_id}/{user_id}")
async def get_history(org_id, user_id):
    """Returns the history of a user"""
    return {
        "org_id": org_id,
        "user_id": user_id,
        "history": [
            {
                "entityId": "entity1",
                "entityType": "contact",
                "entityName": "John Doe",
                "org_id": "234532",
            },
        ],
    }
