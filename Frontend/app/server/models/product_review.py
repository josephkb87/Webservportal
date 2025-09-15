from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review"
    
    
        class Config:
        schema_extra = {
            "example": {
                "name": "Biyita Ngon",
                "product": "Developer Basics Course",
                "rating": 4.9,
                "review": "Excellent course!",
                "date": datetime.now()
            }
        }
        
    class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]
    
    
        class Config:
            schema_extra = {
                "example": {
                    "name": "Micheal Ngon",
                    "product": "DevOps Developer Basics Course",
                    "rating": 5.0,
                    "review": "Basics course!",
                    "date": datetime.now()
            }
        }