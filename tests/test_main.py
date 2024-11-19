from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth import create_access_token

# Initialize TestClient
client = TestClient(app)

def test_issue_credential_with_auth():
    # Create token for authorization
    token = create_access_token({"sub": "user1"})
    response = client.post(
        "/issue-credential/",
        json={"holder": "Alice", "issuer": "IssuerA", "data": "Sample Credential Data"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert "credential_id" in response.json()

def test_share_credential_with_invalid_token():
    # Share credential with invalid token
    response = client.post(
        "/share-credential/",
        json={"credential_id": "1234", "proof_request": "Sample Proof Request"},
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401  # Unauthorized

def test_issue_credential():
    # Issue credential without token
    response = client.post(
        "/issue-credential/",
        json={"holder": "Alice", "issuer": "IssuerA", "data": "Sample Credential Data"},
    )
    assert response.status_code == 422  # This should be 422 due to missing authorization

def test_share_credential():
    # Share credential with valid token
    token = create_access_token({"sub": "user1"})
    issue_response = client.post(
        "/issue-credential/",
        json={"holder": "Bob", "issuer": "IssuerB", "data": "Another Credential Data"},
        headers={"Authorization": f"Bearer {token}"}
    )
    credential_id = issue_response.json()["credential_id"]

    share_response = client.post(
        "/share-credential/",
        json={"credential_id": credential_id, "proof_request": "Sample Proof Request"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert share_response.status_code == 200
    assert "proof" in share_response.json()

def test_revoke_credential():
    # Revoke credential and check its effect
    token = create_access_token({"sub": "user1"})
    issue_response = client.post(
        "/issue-credential/",
        json={"holder": "Charlie", "issuer": "IssuerC", "data": "Revocable Credential"},
        headers={"Authorization": f"Bearer {token}"}
    )
    credential_id = issue_response.json()["credential_id"]

    revoke_response = client.post(
        "/revoke-credential/",
        json={"credential_id": credential_id},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert revoke_response.status_code == 200

    # Try sharing revoked credential
    share_response = client.post(
        "/share-credential/",
        json={"credential_id": credential_id, "proof_request": "Sample Proof Request"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert share_response.status_code == 400  # Credential has been revoked
