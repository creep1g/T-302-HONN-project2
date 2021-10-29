from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from container import Container
from models.buyer_model import BuyerModel
from buyer_repository import BuyerRepository
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post('/buyers', status_code=201)
@inject
async def create_buyer(buyer: BuyerModel, BuyerRepo: BuyerRepository = Depends(
                                Provide[Container.buyer_repository_provider])):
    return BuyerRepo.create_buyer(buyer)


@router.get('/buyers/{id}', status_code=200)
@inject
async def get_buyer(id: int,
                    BuyerRepo: BuyerRepository = Depends(
                        Provide[Container.buyer_repository_provider])):
    buyer = BuyerRepo.get_buyer(id)
    if buyer is None:
        return JSONResponse(status_code=404)
    return BuyerRepo.get_buyer(id)
