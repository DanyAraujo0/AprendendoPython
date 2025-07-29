from store.usecases.product import ProductUsecase
from tests.factories import product_data

async def test_usecases_should_return_sucess():
    result = await ProductUsecase.create(body=product_data())

    assert isinstance(result, ProductOut)