import uvicorn
from fastapi import FastAPI
from container import Container
import buyersAPI

def create_service() -> FastAPI:
    container = Container()
    container.wire(modules=[buyersAPI])

    service = FastAPI()
    service.container = container
    service.include_router(buyersAPI.router)
    return service

service = create_service()

if __name__ == '__main__':
    uvicorn.run('application:app', host='0.0.0.0', port=8002)
