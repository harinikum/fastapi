from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def github():
    return {"message":"correct"}