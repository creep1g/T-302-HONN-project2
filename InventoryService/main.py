import uvicorn
from fastapi import FastAPI
from container import Container
import inventoryAPI
import inventory_processing
from Settings import Settings


def create_service() -> FastAPI:
    print("EY MATE")
    container = Container()
    container.config.from_pydantic(Settings(_env_file='.env'))
    container.wire(modules=[inventoryAPI, inventory_processing])
    service = FastAPI()
    service.container = container
    service.include_router(inventoryAPI.router)
    return (service)


service = create_service()

if __name__ == '__main__':
    uvicorn.run('main:service', host='0.0.0.0', port=8003, reload=True)
