# User API Setup Guide

## Prerequisites

- Python 3.8+
- Google Cloud account with APIs enabled
- Slack workspace with app creation permissions
- Git (for cloning the repository)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/worklocalinc/user-api.git
cd user-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your credentials
```

### 4. Set Up Google Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a service account with domain-wide delegation
3. Download the JSON key file as `service-account.json`
4. Enable required APIs (see GOOGLE_SETUP_GUIDE.md)

### 5. Configure Slack App

1. Create app at [api.slack.com](https://api.slack.com)
2. Add bot scopes (see SLACK_SETUP_GUIDE.md)
3. Install to workspace and get bot token

### 6. Run the API

```bash
python main.py
```

Access the API documentation at http://localhost:8001/docs

## Docker Deployment

```bash
docker-compose up -d
```

## Testing

```bash
# Test Google services
curl http://localhost:8001/google/test/all -H "Authorization: Bearer your-api-key"

# Test Slack
curl http://localhost:8001/slack/test -H "Authorization: Bearer your-api-key"
```

## Support

For detailed setup instructions, see:
- GOOGLE_SETUP_GUIDE.md
- SLACK_SETUP_GUIDE.md
- API Documentation: /docs endpoint