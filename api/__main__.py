import uvicorn

from fastapi import FastAPI
from mongoengine import connect

from api.routers import product, healthcheck

app = FastAPI(
    title='Backend Challenge',
    description='Backend test for Nodis application job. More info at **https://github.com/nodis-com-br/backend-test**'
)

app.include_router(product.router, prefix='/product', tags=['Product'])
app.include_router(healthcheck.router, prefix='/healthcheck', tags=['HealthCheck'])

connect('backend-test', host='mongodb://localhost/backend-test')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)