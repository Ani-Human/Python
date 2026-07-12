from fastapi import FastAPI  #Importing the fastapi module

app = FastAPI()  #Creating a fastapi instance [app variable will be an instance of Fastapi]

@app.get('/')  #Path operation (home) | @something syntax is called a 'decorator', it takes a function below and does something with it.
async def root():  #The async function. Can be normal too.
    return {'message' : 'Hello'}  #Returning the content. A dict, list, str or int can be returned too. 

#-----FastAPI operations----------
'''
(normal)
-Post: to create data.
-Get: to read data.
-Put: to update data.
-Delete: to delete data.

(Exotic)
-Options
-Head
-Patch
-Trace
'''

# Recap¶
# Import FastAPI.
# Create an app instance.
# Write a path operation decorator using decorators like @app.get("/").
# Define a path operation function; for example, def root(): ....
# Run the development server using the command fastapi dev.
# Optionally deploy your app with fastapi deploy.