from datetime import date
from typing import Optional
from domain.model import Reference, Sku, Quantity
from service_layer import services

from fastapi import FastAPI

app = FastAPI()

@app.post("/allocate")
def allocate_endpoint(orderid: Reference, sku: Sku, qty: Quantity):
    
    return

@app.post("/add_batch")
def allocate_endpoint(orderid: Reference, sku: Sku, qty: Quantity, eta: Optional[date]): #will this work for optinoal date that is iso8601?
    
    return