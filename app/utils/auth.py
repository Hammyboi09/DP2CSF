import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from app.utils.crypto import SECRET_KEY

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_token(token: str):
    try:
        print(f"Verifying token: {token}")  # Debugging line to check the token
        # Ensure the token is decoded with the correct SECRET_KEY and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        # Debugging line to see the decoded payload
        print(f"Decoded payload: {payload}")
        
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired")  # Debugging line for expired token
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError as e:
        print(f"Invalid token error: {e}")  # Debugging line for invalid token
        raise HTTPException(status_code=401, detail="Invalid token")
