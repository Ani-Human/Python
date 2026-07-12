from fastapi import FastAPI

app = FastAPI()

#path parameters
@app.get('/item_id/{item_id}')
async def item(item_id: int):
    return {'item_ID' : item_id}