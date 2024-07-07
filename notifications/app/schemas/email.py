from pydantic import BaseModel


class Email(BaseModel):
    receipts: list[str]
    message: str
    subject: str

    class Config:
        from_attribute = True
