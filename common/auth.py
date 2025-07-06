# auth.py - Authentication utilities for User API
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
import os
from typing import Optional
import requests
import time
import hmac
import hashlib

security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

def get_api_keys():
    """Get API keys from environment"""
    api_keys_str = os.getenv("API_KEYS", "")
    return [key.strip() for key in api_keys_str.split(",") if key.strip()]

def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verify API key from Authorization header"""
    api_keys = get_api_keys()
    
    if not api_keys:
        raise HTTPException(
            status_code=500,
            detail="API keys not configured on server"
        )
    
    if credentials.credentials not in api_keys:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )
    
    return credentials.credentials

def verify_google_token(token: Optional[str] = Depends(oauth2_scheme)):
    """Verify Google OAuth token"""
    if not token:
        return None
    
    # Verify token with Google
    response = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token}"
    )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Invalid Google OAuth token"
        )
    
    token_info = response.json()
    
    # Verify it's for the correct user
    expected_email = os.getenv("GOOGLE_USER_EMAIL", "james@worklocal.ca")
    if token_info.get("email") != expected_email:
        raise HTTPException(
            status_code=403,
            detail="Token not authorized for this user"
        )
    
    return token_info

def get_slack_token():
    """Get Slack bot token from environment"""
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        raise HTTPException(
            status_code=500,
            detail="Slack bot token not configured"
        )
    return token

def verify_slack_request(headers: dict, body: bytes = None):
    """Verify Slack request signature"""
    slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")
    if not slack_signing_secret:
        return True  # Skip verification if not configured
    
    # Get headers
    timestamp = headers.get("X-Slack-Request-Timestamp", "")
    slack_signature = headers.get("X-Slack-Signature", "")
    
    if not timestamp or not slack_signature:
        return False
    
    # Check timestamp to prevent replay attacks (5 minutes)
    if abs(time.time() - float(timestamp)) > 60 * 5:
        return False
    
    # Create signature base string
    if body:
        sig_basestring = f"v0:{timestamp}:{body.decode('utf-8')}"
        
        # Create HMAC SHA256 signature
        my_signature = 'v0=' + hmac.new(
            slack_signing_secret.encode(),
            sig_basestring.encode(),
            hashlib.sha256
        ).hexdigest()
        
        # Compare signatures
        return hmac.compare_digest(my_signature, slack_signature)
    
    return True