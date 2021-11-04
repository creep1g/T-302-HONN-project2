from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from container import Container
from models.inventory_model import InventoryModel
from inventory_repository import InventoryRepository
from inventory_processing import InventoryProcessing
import threading

router = APIRouter()


@router.post('/products', status_code=201)
@inject
async def create_product(product: InventoryModel, InventoryRepo: InventoryRepository = Depends(Provide[Container.inventory_repository_provider])):
    return InventoryRepo.create_product(product)


@router.patch('/products/{id}', status_code=201)
@inject
async def reserve_product(id: int, InventoryRepo: InventoryRepository = Depends(Provide[Container.inventory_repository_provider])):
    return InventoryRepo.reserve_product(product_id=id)

@router.get('/products/{id}', status_code=200)
@inject
async def get_product(id: int, InventoryRepo: InventoryRepository = Depends(
        Provide[Container.inventory_repository_provider])):
    product = InventoryRepo.get_product(id)
    if product is None:
        return JSONResponse(status_code=404, content="Product does not exist")
    return InventoryRepo.get_product(id)


@router.on_event('startup')
@inject
async def get_message(message_receiver: InventoryProcessing = Provide[Container.inventory_proccessing_provider]):
    thread = threading.Thread(target=message_receiver.payment_proccessing)
    thread.start()
