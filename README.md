# Decentralized Privacy-Preserving Credential Sharing Framework (DP2CSF)

## Overview
This framework provides a solution for privacy-preserving, decentralized credential sharing using Zero-Knowledge Proofs (ZKPs). It enables:
- Credential issuance
- Credential sharing with privacy preservation
- Credential revocation

---

## Setup Instructions

### Prerequisites
- Python 3.8+ (tested with Python 3.13)
- Virtual Environment (venv)
- Dependencies listed in `requirements.txt`

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd DP2CSF
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

- Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
   The application will be running at `http://127.0.0.1:8000`.

---

## API Endpoints

### 1. **Issue Credential**
   - **Endpoint:** `/issue-credential/`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "holder": "Alice",
       "issuer": "IssuerA",
       "data": "Sample Credential Data"
     }
     ```
   - **Response:**
     ```json
     {
       "credential_id": "some-uuid",
       "message": "Credential issued successfully!"
     }
     ```

### 2. **Share Credential**
   - **Endpoint:** `/share-credential/`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "credential_id": "some-uuid",
       "proof_request": "Sample Proof Request"
     }
     ```
   - **Response:**
     ```json
     {
       "status": "success",
       "proof": "Mock proof for Sample Proof Request using credential some-uuid"
     }
     ```

### 3. **Revoke Credential**
   - **Endpoint:** `/revoke-credential/`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "credential_id": "some-uuid"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Credential some-uuid has been revoked."
     }
     ```

---

## Security Enhancements

1. **JWT Authentication**
   - All API endpoints are secured using JWT. Include the following header in all requests:
     ```text
     Authorization: Bearer <your-token>
     ```

2. **Zero-Knowledge Proofs (ZKPs)**
   - Basic ZKP simulation is implemented to enable privacy-preserving credential sharing.
   - Future iterations will integrate a sophisticated ZKP library for enhanced privacy.

---

## Testing

### Unit Tests
- Run the test suite with:
   ```bash
   pytest --cov=.
   ```

### API Tests (Postman)
1. **Setup:**
   - Import the provided Postman collection into your Postman application.
   - Create a new environment named `DP2CSF Environment` and set the variable `access_token`.

2. **Tests Include:**
   - Login: Verifies token generation.
   - Fetch User Profile: Tests retrieval of user details.
   - Fetch All Users: Ensures user list retrieval works.
   - Create, Update, and Delete User: Validates CRUD operations on users.

3. **Expected Outputs:**
   - Refer to the detailed Postman tests documentation in `postman-tests.md`.

---

## Future Enhancements
- Integration with advanced ZKP libraries (e.g., zkSNARKs).
- Support for multi-factor authentication.
- UI dashboard for credential management.
