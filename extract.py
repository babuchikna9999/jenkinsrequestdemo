import requests
import pandas as pd
import os

TOKEN = os.getenv("API_TOKEN")

if TOKEN == "1234":
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    data=response.json()
    df=pd.DataFrame(data)
    df=df[["id","name"]]
    print(df)
else:
    print("invalid")