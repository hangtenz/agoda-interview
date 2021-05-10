from pydantic import BaseModel

#Interface definition to comunicate with RESTAPI

class DecryptText(BaseModel):
    text:str

class EncryptText(BaseModel):
    encrypted:str

class EncryptionRequest(BaseModel):
    data: list[DecryptText]

class EncryptionResponse(BaseModel):
    data: list[EncryptText]

class DecryptionRequest(BaseModel):
    data: list[EncryptText]

class DecryptionResponse(BaseModel):
    data: list[DecryptText]