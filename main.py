import os

def my_keys():
    id= os.environ.get('SECRET_ID')
    password= os.environ.get("SECRET_PASSWORD")

    print(id,password)

my_keys()