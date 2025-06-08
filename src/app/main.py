import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title='EasyProject',
    version='0.0.1',
)


if __name__ == '__main__':
    uvicorn.run(app=app)
