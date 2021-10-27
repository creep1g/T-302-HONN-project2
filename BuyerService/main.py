import uvicorn
from fastapi import FastAPI
from container import Container
import buyersAPI
from Settings import Settings

def create_service() -> FastAPI:
    container = Container()
    container.config.from_pydantic(Settings(_env_file='.env'))
    container.wire(modules=[buyersAPI])


    service = FastAPI()
    service.container = container
    service.include_router(buyersAPI.router)
    return service

service = create_service()

if __name__ == '__main__':
    uvicorn.run('main:service', host='0.0.0.0', port=8002)
