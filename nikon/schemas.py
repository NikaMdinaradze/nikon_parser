from pydantic import BaseModel


class NikonPreview(BaseModel):
    name: str
    price: str
    detailed_link: str
    category: str

