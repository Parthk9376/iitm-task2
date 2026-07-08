from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt

ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-gaogjv7o.apps.exam.local"

PUBLIC_KEY = """
PASTE THE COMPLETE PUBLIC KEY HERE
"""

app = FastAPI()

class TokenRequest(BaseModel):
    token: str

@app.post("/verify")
def verify(req: TokenRequest):
    try:
        payload = jwt.decode(
            req.token,
            PUBLIC_KEY,
            algorithms=["RS256"],
            audience=AUDIENCE,
            issuer=ISSUER,
        )

        return {
            "valid": True,
            "email": payload.get("email"),
            "sub": payload.get("sub"),
            "aud": payload.get("aud"),
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail={"valid": False}
        )
