from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from container import Container
from order_notifier import OrderNotifier
from models.order_model import OrderModel
from order_repository import OrderRepository


router = APIRouter()

@router.post('/orders', status_code=201)
@inject
async def create_order(order: OrderModel, OrderRepo: OrderRepository = Depends(
                                Provide[Container.order_repository_provider]),
                                order_notifier: OrderNotifier = Depends(
                                Provide[Container.order_notifier_provider])):
    order_notifier.notify(order)
    return OrderRepo.create_order(order)[0][0]

@router.get('/orders/{id}', status_code=200)
@inject
async def get_order(id: int, OrderRepo: OrderRepository = Depends(Provide[Container.order_repository_provider])):
    return OrderRepo.get_order(id)
