from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {
        'item id' : item_id, #path parameter
        'needy' : needy, #Required query parameter
        'skip' : skip, #query parameter with default value 0
        'limit' : limit, #Option query parameter
    }
    return item

#Enum can also be used in this case!