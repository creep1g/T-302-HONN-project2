from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from container import Container
router = APIRouter()

@router.post('/buyers', status_code=201)
@inject
async def create_buyer(buyer: BuyerModel, BuyerRepo: BuyerRepository = Depends(
                                Provide[Container.buyer_repository_provider])):
    return BuyerRepo.create_buyer(buyer.name,
                                  buyer.email,
                                  buyer.ssn,
                                  buyer.phone)

@router.get('/buyers/{id}', status_code=200)
@inject
async def get_buyer(id: int, BuyerRepo: BuyerRepository = Depends(Provide[Container.buyer_repository_provider])):

    return BuyerRepo.get_buyer(id)
