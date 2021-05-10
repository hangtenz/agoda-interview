from fastapi import FastAPI
import uvicorn
from interface.encryption import EncryptionRequest,EncryptionResponse
from interface.encryption import DecryptionRequest,DecryptionResponse
from usecase.encryption import EncryptionUsecase



#TODO: read config file private key should not hard code



app = FastAPI()
private_key = "private_key"
encryption_usecase = EncryptionUsecase(private_key)


#set endpoint
@app.post('/encrypt',response_model=EncryptionResponse,status_code=200)
def encrypt(request:EncryptionRequest):
    flat_request = []
    for d in request.data:
        flat_request.append(d.text)
    encrypt_data = encryption_usecase.encrypt(flat_request)
    res = []
    for d in encrypt_data:
        res.append({"encrypted":d})
    return {"data":res}


@app.post('/decrypt',response_model=DecryptionResponse,status_code=200)
def decrypt(request:DecryptionRequest) -> DecryptionResponse:
    flat_request = []
    for d in request.data:
        print("d = ",d)
        flat_request.append(d.encrypted)
    decrypt_data = encryption_usecase.decrypt(flat_request)
    res = []
    for d in decrypt_data:
        res.append({"text": d})
    return {"data":res}


if __name__ == "__main__":
    uvicorn.run("endpoint:app", host="0.0.0.0", port=5000,log_level="info",reload=True)