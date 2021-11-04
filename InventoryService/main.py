import uvicorn
from fastapi import FastAPI
from container import Container
import inventoryAPI
from inventory_processing import InventoryProcessing
from Settings import Settings


def create_service() -> FastAPI:
    print("EY MATE")
    container = Container()
    container.config.from_pydantic(Settings(_env_file='.env'))
    container.wire(modules=[inventoryAPI])
    p: InventoryProcessing = container.inventory_proccessing_provider()
    service = FastAPI()
    service.container = container
    service.include_router(inventoryAPI.router)
    return (service, p)


service,p= create_service()
p.payment_proccessing()

if __name__ == '__main__':

    uvicorn.run('main:service', host='0.0.0.0', port=8003)
