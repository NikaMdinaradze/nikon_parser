from pydantic import BaseModel
import json


class NikonPreview(BaseModel):
    name: str
    price: str
    detailed_link: str
    category: str

