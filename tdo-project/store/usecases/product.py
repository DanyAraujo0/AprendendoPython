from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.schemas.product import ProductIn     

class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.databse: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.collection.get_collection("products")

    async def create(self, body:ProductIn):
        await self.collection.insert_one(body.model_dump())

product_usecase = ProductUsecase()