from jose import jwt

def create_token(data:dict):
    encode_d = data.copy()
    return jwt.encode(encode_d,"3d26a8caae3504a5665a2c7ba980b46ee0b1d14b539990613b310e42c08f0e52")

def dec(token:str):
    return jwt.decode(token,"3d26a8caae3504a5665a2c7ba980b46ee0b1d14b539990613b310e42c08f0e52")