from fastapi import APIRouter, HTTPException
from app.models import Product, ProductUpdate
from app.database import products_db

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product, status_code=201)
def create_product(product: Product):
    """
    Create a new product.

    Args:
        product (Product): The product to create.

    Returns:
        Product: The created product.
    """
    if product.id in products_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    products_db[product.id] = product
    return product
@router.get("/", response_model=list[Product])
def get_products():
    """
    Retrieve all products.

    Returns:
        list[Product]: A list of all products.
    """
    return list(products_db.values())

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    """
    Retrieve a product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        Product: The retrieved product.

    Raises:
        HTTPException: If the product is not found.
    """
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: ProductUpdate):
    """
    Update a product by its ID.

    Args:
        product_id (int): The ID of the product to update.
        product_update (ProductUpdate): The updated product information.

    Returns:
        Product: The updated product.

    Raises:
        HTTPException: If the product is not found.
    """
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product_update.name is not None:
        product.name = product_update.name
    if product_update.price is not None:
        product.price = product_update.price
    if product_update.description is not None:
        product.description = product_update.description
    
    products_db[product_id] = product
    return product

@router.patch("/{product_id}", response_model=ProductUpdate)
def partial_update_product(product_id: int, product_update: ProductUpdate):
    """
    Partially update a product by its ID.

    Args:
        product_id (int): The ID of the product to update.
        product_update (ProductUpdate): The updated product information.

    Returns:
        Product: The updated product.

    Raises:
        HTTPException: If the product is not found.
    """
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product_update.name is not None:
        product.name = product_update.name
    if product_update.price is not None:
        product.price = product_update.price
    if product_update.description is not None:
        product.description = product_update.description
    
    products_db[product_id] = product
    return product
