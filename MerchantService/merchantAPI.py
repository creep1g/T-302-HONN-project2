from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from container import Container
from models.merchant_model import MerchantModel
from merchant_repository import MerchantRepository

router = APIRouter()


@router.post('/merchants', status_code=201)
@inject
async def create_merchant(merchant: MerchantModel,
                          MerchantRepo: MerchantRepository = Depends(
                           Provide[Container.merchant_repository_provider])):
    return MerchantRepo.create_merchant(merchant)


@router.get('/merchants/{id}', status_code=200)
@inject
async def get_merchant(id: int, MerchantRepo: MerchantRepository = Depends(
                       Provide[Container.merchant_repository_provider])):
    merchant = MerchantRepo.get_merchant(id)
    if merchant is None:
        return JSONResponse(status_code=404)

    return MerchantRepo.get_merchant(id)
