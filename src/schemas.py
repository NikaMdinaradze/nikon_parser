from pydantic import BaseModel
from typing import List


class NikonPreview(BaseModel):
    name: str
    price: str
    detailed_link: str
    category: str


class ImageURLS(BaseModel):
    images: List[str]
