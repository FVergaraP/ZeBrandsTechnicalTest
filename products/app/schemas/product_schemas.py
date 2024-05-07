from pydantic import BaseModel


class ProductBase(BaseModel):
    sku: str
    name: str
    price: float
    brand: str

    class Config:
        from_attribute = True
