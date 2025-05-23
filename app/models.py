from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    """
    Represents a product with its basic attributes.

    Attributes:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        description (Optional[str]): Optional description of the product.
    """
    id: int
    name: str
    price: float
    description: Optional[str] = None

class ProductUpdate(BaseModel):
    """
    Data model for updating product information.

    Attributes:
        name (Optional[str]): The updated name of the product. If not provided, the name will remain unchanged.
        price (Optional[float]): The updated price of the product. If not provided, the price will remain unchanged.
        description (Optional[str]): The updated description of the product. If not provided, the description will remain unchanged.
    """
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
