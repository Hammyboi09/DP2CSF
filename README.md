# Decentralized Privacy-Preserving Credential Sharing Framework (DP2CSF)

## Overview
This framework provides a solution for privacy-preserving, decentralized credential sharing, using Zero-Knowledge Proofs (ZKPs). It enables:
- Credential issuance
- Credential sharing with privacy preservation
- Credential revocation

## Setup Instructions

### Prerequisites
- Python 3.8+ (tested with Python 3.13)
- Virtual Environment (venv)
- Dependencies listed in `requirements.txt`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd DP2CSF

2. Set up a virtual environment:
   python3 -m venv venv

3. Activate the virtual environment:
   For macOS/Linux: source venv/bin/activate
   For Windows: venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

### Running the Application

- To start the FastAPI server: uvicorn app.main:app --reload
The application will be running at http://127.0.0.1:8000.

### API Endpoints

1. Issue Credential
   Endpoint: /issue-credential/
   Method: POST
   Request Body:
  {  
  "holder": "Alice",
  "issuer": "IssuerA",
  "data": "Sample Credential Data"
  }

   Response:
  {  
  "credential_id": "some-uuid",
  "message": "Credential issued successfully!"
  }

2. Share Credential
   Endpoint: /share-credential/
   Method: POST
   Request Body:
  {  
  "credential_id": "some-uuid",
  "proof_request": "Sample Proof Request"
  }

   Response:
  {  
  "status": "success",
  "proof": "Mock proof for Sample Proof Request using credential some-uuid"
  }

3. Revoke Credential
   Endpoint: /revoke-credential/
   Method: POST
   Request Body:
  {  
  "credential_id": "some-uuid"
  }

   Response:
  {  
  "message": "Credential some-uuid has been revoked."
  }

### Security Enhancements

1. JWT Authentication
   - All API endpoints are secured using JWT. Include the following header in all requests:
     Authorization: Bearer <your-token>

2. Zero-Knowledge Proofs (ZKPs)
   - Basic ZKP simulation is implemented to enable privacy-preserving credential sharing.
   - Future iterations will integrate a sophisticated ZKP library for enhanced privacy.

### Testing

- Run the test suite with: pytest --cov=.