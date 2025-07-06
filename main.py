# main.py - User Communication & Account Tools API Server
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Add current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Add subdirectories to Python path
current_dir = Path(__file__).parent
sys.path.extend([
    str(current_dir / "google_services"),
    str(current_dir / "slack"),
    str(current_dir / "common"),
])

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

# Import routers from each service
try:
    from google_services.google_services_router import router as google_router
    from slack.slack_router import router as slack_router
except ImportError as e:
    print(f"Import error: {e}")
    raise

# For Cloud Run with secrets
if os.path.exists("/secrets/api-env"):
    load_dotenv("/secrets/api-env")

# Create FastAPI app
app = FastAPI(
    title="User Communication & Account Tools API (Extended)",
    description="""Comprehensive API for Google Workspace and Slack integration.
    
    Google Services: Gmail, Calendar, Drive, Sheets, Docs, Slides, Forms, Tasks, Keep, 
    Contacts, Directory, YouTube, Photos, Chat
    
    Slack: Messages, Channels, Users, Files
    
    Configured for: james@worklocal.ca""",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with prefixes
app.include_router(google_router, prefix="/google", tags=["Google Services"])
app.include_router(slack_router, prefix="/slack", tags=["Slack"])

# Root endpoint
@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint"""
    return {
        "status": "active",
        "service": "User Communication & Account Tools API",
        "version": "1.0.0",
        "endpoints": {
            "google": "/google",
            "slack": "/slack",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "user-api",
        "version": "2.0.0",
        "google_services": [
            "gmail", "calendar", "drive", "sheets", "docs", 
            "slides", "forms", "tasks", "keep", "contacts",
            "directory", "youtube", "photos", "chat"
        ],
        "google_oauth_scopes": 28,
        "slack_configured": bool(os.getenv("SLACK_BOT_TOKEN"))
    }

# API info endpoint
@app.get("/info", tags=["Info"])
def api_info():
    """Get API information and available endpoints"""
    return {
        "title": "User Communication & Account Tools API (Extended)",
        "version": "2.0.0",
        "user": "james@worklocal.ca",
        "slack_workspace": "localmediaconcepts.slack.com",
        "available_services": {
            "google": {
                "gmail": "Email management (full access: send, read, modify, labels)",
                "calendar": "Calendar events and scheduling",
                "drive": "File storage and management (full access)",
                "sheets": "Spreadsheet operations",
                "docs": "Document management",
                "slides": "Presentation management",
                "forms": "Form creation and responses",
                "tasks": "Task lists and task management",
                "keep": "Notes management",
                "contacts": "Contact management",
                "directory": "Workspace user and group directory",
                "youtube": "YouTube channel and video data",
                "photos": "Photo library access",
                "chat": "Google Chat messaging (bot, spaces, messages)"
            },
            "slack": {
                "messages": "Send and receive messages",
                "channels": "Channel management",
                "users": "User information",
                "files": "File sharing"
            }
        },
        "oauth_scopes": {
            "count": 28,
            "categories": [
                "Gmail (5 scopes)",
                "Calendar (2 scopes)",
                "Drive (4 scopes)",
                "Productivity (4 scopes)",
                "Communication (3 scopes)",
                "Directory & Contacts (4 scopes)",
                "Additional Services (6 scopes)"
            ]
        }
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)