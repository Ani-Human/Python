from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def read_user_item(item_id: str, required_query: int ): #To make the required query optional add " | None = None"
    return {
        'item id' : item_id,
        'Required query' : required_query,
    }