#env variables
#External to python


import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("NAME")
print(f'Hola {name}')


#--------Only with os and export of env vars--------
#  source myenv/bin/activate
# (myenv) export MY_NAME="WADE_THE_GREAT"
# (myenv) python main.py
# Hola WADE_THE_GREAT
# (myenv) MY_NAME="Habibi" python3 main.py
# Hola Habibi
# (myenv) python main.py
# Hola WADE_THE_GREAT


#--------With load_dotenv and os--------

# (myenv) python main.py
# Hola IWONTTELLU