import os
from dotenv import load_dotenv

# used for method 2
load_dotenv()

def my_keys():
    # method 1
    # id= os.environ.get('SECRET_ID')
    # password= os.environ.get("SECRET_PASSWORD")

    # method 2
    id = os.getenv('SECRET_ID')
    password = os.getenv('SECRET_PASSWORD')

    print(id,password)

my_keys()