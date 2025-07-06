# User Communication & Account Tools API (Extended)

A comprehensive API integrating Google Workspace services and Slack, designed for james@worklocal.ca and the localmediaconcepts.slack.com workspace.

## 🚀 Features

### Google Services Integration (28 OAuth Scopes!)
- **Gmail**: Full email management (send, read, modify, labels)
- **Calendar**: Create and manage events
- **Drive**: Complete file storage and management
- **Sheets**: Read/write spreadsheet data
- **Docs**: Document management
- **Slides**: Presentation management
- **Forms**: Form creation and responses
- **Tasks**: Task lists and tasks
- **Keep**: Notes management
- **Contacts**: Contact management
- **Directory**: Workspace users and groups
- **YouTube**: Channel data (read-only)
- **Photos**: Photo library (read-only)
- **Chat**: Messaging (bot, spaces, messages)

### Slack Integration
- Send messages to channels
- List channels and users
- Upload files
- Webhook support for events
- Workspace: localmediaconcepts.slack.com

## 📋 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/worklocalinc/user-api.git
   cd user-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up credentials:
   - Google service account (see `GOOGLE_SETUP_GUIDE.md`)
   - Slack app tokens (see `SLACK_SETUP_GUIDE.md`)
   - Copy `.env.example` to `.env` and configure

4. Run the API:
   ```bash
   python main.py
   ```

## 📚 Documentation

- **API Docs**: http://localhost:8001/docs
- **OpenAPI Spec**: http://localhost:8001/openapi.json
- **29 Endpoints** covering all Google and Slack services

## 🏗️ Architecture

```
user-api/
├── main.py                 # FastAPI application
├── google_services/        # Google services integration
├── slack/                  # Slack integration
├── common/                 # Shared utilities
└── openapi_spec.json      # OpenAPI specification
```

## 🔐 Security

- API key authentication
- Environment-based configuration
- Credentials excluded from version control
- Domain-wide delegation for Google Workspace

## 🚢 Deployment

The API is containerized and ready for deployment:
- Docker support included
- Google Cloud Run compatible
- Environment variable configuration

## 📊 Available Services

- 14 Google services with full API access
- Complete Slack integration
- RESTful API with OpenAPI documentation
- Ready for OpenWebUI integration

## 🤝 Contributing

This project is specifically designed for james@worklocal.ca and the localmediaconcepts workspace.

## 📄 License

Private project for worklocal.ca

---

**Built with ❤️ using FastAPI, Google APIs, and Slack SDK**