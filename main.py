#Query parameters
#Optional params can be given too
#Fastapi is smart enough to rectify the path params and query params
#Query type conversion

from fastapi import FastAPI

app = FastAPI()


fake_items_db= [{'item_name' : 'foo'}, {'item_name' : 'Bar'}, {'item_name' : 'pencil'}]

@app.get('/items/{item_id}')
async def read_items(item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id' : item_id}
    if q:
        item.update({'q' : q})
    if short: #An optional query
        item.update(

        {"description": "This is an amazing item that has a long description"}
        )
    return item
