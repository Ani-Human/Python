from fastapi import FastAPI

app = FastAPI()

#The order matters alot.abs
#path operations are evaluated in order. 


@app.get('/users/me')
async def read_user_me():
    return {'user' : 'me'} #This was using the read_user function and bugged. 

@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return {'user' : user_id}



'''
The order matters becuz if the position of the functions are reversed,
the user_id parameter will have the result 'me' always.
[Paths are evaluated in order]

path for /users/{user_id} would match also for /users/me, 
"thinking" that it's receiving a parameter user_id with a value of "me"
'''