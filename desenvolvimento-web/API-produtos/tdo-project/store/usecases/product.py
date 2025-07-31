from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut   
from store.core.exceptions import NotFoundException

class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body:ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(product.model_dump())

        return product
    
    async def get(self, id:UUID) -> ProductOut:
        result = await self.collection.find_one({"id":id})

        if not result:
            raise NotFoundException(message= f"Product not found with filter {id}")
        
        return ProductOut(**result)

    async def query(
        self,
        min_price: Optional[float] = None, 
        max_price: Optional[float] = None
    ) -> List[ProductOut]:
        
        db_filter = {}
        price_filter = {}

        if min_price is not None:
            price_filter["$gt"] = min_price 

        if max_price is not None:
            price_filter["$lt"] = max_price
        
        if price_filter:
            db_filter["price"] = price_filter

        return [ProductOut(**item) async for item in self.collection.find(db_filter)]
    
    async def update(self, id:UUID, body: ProductUpdate) -> ProductUpdateOut:
        product = await self.get(id=id)

        if body.updated_at is None:
            body.updated_at = datetime.now(timezone.utc)

        update_data = body.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product, key, value)

        return ProductUpdateOut.model_validate(product)
    
        # result = await self.collection.find_one_and_update(
        #     filter={"id":id},
        #     update={"$set": body.model_dump(exclude_none=True)},
        #     return_document=pymongo.ReturnDocument.AFTER
        # )
        # return ProductUpdateOut(**result)
    
    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False

product_usecase = ProductUsecase()