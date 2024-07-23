# import package
from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd

df = pd.DataFrame()

df['Uername'] = ['Ronaldo', 'Messi', 'Mbappe']
df['Location'] = ['Portugal', 'Argentina', 'France']

# Password Api_key
API_KEY = "testingapitokenkey1234"

# buat object
app = FastAPI()

# membuat Function + URL (endpoint)
# endpoint untuk ambil all data atau retrieve all data
# http://www.domain.com/
@app.get("/")
def handlerData(request: Request):
    # get request headers
    headers = request.headers

    return {
        "message": "this is fastapi data",
       "headers": headers
    }

# endpoint get all data from dataframe
@app.get("/data/{loc}")
def handlerDf(loc): 
    # filter dataframe
    result = df.query(f"Location == '{loc}'")       
    return result.to_dict(orient="records")

# endpoint secret
@app.get('/secret')
def handlerSecret(api_key: str = Header(None)):
    # cek api_key
    if api_key != API_KEY or api_key == None:
        raise HTTPException(detail="Password Salah!", status_code=401)
        
    return{
        "secret": "hanya saya dan tuhan yang tahu"
    }