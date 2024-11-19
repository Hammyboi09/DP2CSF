from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
import uuid
from app.utils.auth import create_access_token, verify_token

app = FastAPI()

# Mock Database
credentials_db = {}
revoked_credentials = set()

# Models
class Credential(BaseModel):
    holder: str
    issuer: str
    data: str

class CredentialShareRequest(BaseModel):
    credential_id: str
    proof_request: str

class CredentialRevocationRequest(BaseModel):
    credential_id: str

# Dependency for validating the token
def get_current_user(authorization: str = Header(...)):
    token = authorization.split("Bearer ")[-1]
    # Verify and decode the token to extract user info
    payload = verify_token(token)  # If the token is invalid, it will raise an HTTPException
    return payload  # The payload can include user information (e.g., username or user id)

# Endpoints
@app.post("/issue-credential/")
def issue_credential(credential: Credential, current_user: str = Depends(get_current_user)):
    credential_id = str(uuid.uuid4())
    credentials_db[credential_id] = credential
    return {"credential_id": credential_id, "message": "Credential issued successfully!"}

@app.post("/share-credential/")
def share_credential(share_request: CredentialShareRequest, current_user: str = Depends(get_current_user)):
    credential_id = share_request.credential_id
    if credential_id not in credentials_db:
        raise HTTPException(status_code=404, detail="Credential not found.")
    if credential_id in revoked_credentials:
        raise HTTPException(status_code=400, detail="Credential has been revoked.")
    
    # You can also log the current user's info from the token if needed
    user_info = current_user  # This contains the decoded information from the token (e.g., username)
    return {
        "status": "success",
        "proof": f"Mock proof for {share_request.proof_request} using credential {credential_id}",
        "user_info": user_info,  # Optionally return user info for debugging
    }

@app.post("/revoke-credential/")
def revoke_credential(revocation_request: CredentialRevocationRequest, current_user: str = Depends(get_current_user)):
    credential_id = revocation_request.credential_id
    if credential_id not in credentials_db:
        raise HTTPException(status_code=404, detail="Credential not found.")
    revoked_credentials.add(credential_id)
    return {"message": f"Credential {credential_id} has been revoked."}
