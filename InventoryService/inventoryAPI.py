from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from container import Container
from models.inventory_model import InventoryModel
from inventory_repository import InventoryRepository

router = APIRouter()


@router.post('/products', status_code=201)
@inject
async def create_product(product: InventoryModel, InventoryRepo: InventoryRepository = Depends(Provide[Container.inventory_repository_provider])):
    print("HELOOOO")
    return InventoryRepo.create_product(product)


@router.get('/products/{id}', status_code=200)
@inject
async def get_product(id: int, InventoryRepo: InventoryRepository = Depends(
        Provide[Container.inventory_repository_provider])):
    product = InventoryRepo.get_product(id)
    if product is None:
        return JSONResponse(status_code=404)
    return InventoryRepo.get_product(id)
