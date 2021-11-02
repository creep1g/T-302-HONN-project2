from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from container import Container
from order_notifier import OrderNotifier
from models.order_model import OrderModel
from order_repository import OrderRepository
from fastapi.responses import JSONResponse
import requests

router = APIRouter()

@router.post('/orders', status_code=201)
@inject
async def create_order(order: OrderModel, OrderRepo: OrderRepository = Depends(
                                Provide[Container.order_repository_provider]),
                                order_notifier: OrderNotifier = Depends(
                                Provide[Container.order_notifier_provider])):

    if requests.get(f'''http://merchant_service:8001/merchants/{order.merchantId}''').json() == None:
        return JSONResponse(status_code=400, content={"message": "Merchant does not exist"})
    if requests.get(f'''http://buyer_service:8002/buyers/{order.buyerId}''').json() == None:
        return JSONResponse(status_code=400, content={"message": "Buyer does not exist"})
    if (requests.get(f'''http://merchant_service:8001/merchants/{order.merchantId}''').json()["allowsDiscount"] == False and order.discount > 0):
        return JSONResponse(status_code=400, content={"message": "Merchant does not allow discount"})
    #TODO Requests for INVENTORY and product does not exists and product is
    # sold out and product does not belong to merchant
        

    order_notifier.notify(order)
    
    return OrderRepo.create_order(order)[0][0]

@router.get('/orders/{id}', status_code=200)
@inject
async def get_order(id: int, OrderRepo: OrderRepository = Depends(Provide[Container.order_repository_provider])):
    order = OrderRepo.get_order(id)
    if order is None:
        return JSONResponse(status_code=404)
    return OrderRepo.get_order(id)
