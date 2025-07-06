# models.py - Pydantic models for User API
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

# Google Models
class EmailMessage(BaseModel):
    """Gmail message model"""
    to: List[EmailStr] = Field(..., description="List of recipient email addresses")
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body (HTML or plain text)")
    cc: Optional[List[EmailStr]] = Field(None, description="CC recipients")
    bcc: Optional[List[EmailStr]] = Field(None, description="BCC recipients")
    attachments: Optional[List[str]] = Field(None, description="List of attachment file paths or URLs")

class EmailResponse(BaseModel):
    """Gmail response model"""
    message_id: str
    thread_id: Optional[str] = None
    status: str = "sent"

class CalendarEvent(BaseModel):
    """Google Calendar event model"""
    summary: str = Field(..., description="Event title")
    description: Optional[str] = Field(None, description="Event description")
    start_time: datetime = Field(..., description="Event start time")
    end_time: datetime = Field(..., description="Event end time")
    attendees: Optional[List[EmailStr]] = Field(None, description="List of attendee emails")
    location: Optional[str] = Field(None, description="Event location")
    recurrence: Optional[List[str]] = Field(None, description="Recurrence rules in RRULE format")

class DriveFile(BaseModel):
    """Google Drive file model"""
    name: str = Field(..., description="File name")
    mime_type: Optional[str] = Field(None, description="MIME type of the file")
    parent_id: Optional[str] = Field(None, description="Parent folder ID")
    description: Optional[str] = Field(None, description="File description")

class DriveFileResponse(BaseModel):
    """Drive file response"""
    file_id: str
    name: str
    web_view_link: str
    download_link: Optional[str] = None

class SpreadsheetData(BaseModel):
    """Google Sheets data model"""
    spreadsheet_id: str = Field(..., description="Spreadsheet ID")
    range: str = Field(..., description="A1 notation range (e.g., 'Sheet1!A1:C10')")
    values: List[List[Any]] = Field(..., description="2D array of values")

class SpreadsheetUpdate(BaseModel):
    """Spreadsheet update request"""
    spreadsheet_id: str
    range: str
    values: List[List[Any]]
    value_input_option: str = Field("USER_ENTERED", description="How to interpret values")

# Slack Models
class SlackMessage(BaseModel):
    """Slack message model"""
    channel: str = Field(..., description="Channel ID or name (e.g., '#general' or 'C1234567890')")
    text: str = Field(..., description="Message text")
    thread_ts: Optional[str] = Field(None, description="Thread timestamp for replies")
    attachments: Optional[List[Dict[str, Any]]] = Field(None, description="Message attachments")
    blocks: Optional[List[Dict[str, Any]]] = Field(None, description="Block Kit blocks")

class SlackMessageResponse(BaseModel):
    """Slack message response"""
    ok: bool
    channel: str
    ts: str
    message: Optional[Dict[str, Any]] = None

class SlackChannel(BaseModel):
    """Slack channel model"""
    id: str
    name: str
    is_private: bool
    is_member: bool
    topic: Optional[str] = None
    purpose: Optional[str] = None

class SlackUser(BaseModel):
    """Slack user model"""
    id: str
    name: str
    real_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_bot: bool = False
    is_admin: bool = False

# Common Response Models
class APIResponse(BaseModel):
    """Generic API response"""
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None

class ListResponse(BaseModel):
    """List response with pagination"""
    items: List[Any]
    total: int
    page: int = 1
    per_page: int = 50
    has_more: bool = False