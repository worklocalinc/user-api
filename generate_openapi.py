# generate_openapi.py - Generate OpenAPI specification
import json
import sys
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from main import app

def generate_openapi_spec():
    """Generate and save OpenAPI specification"""
    # Get the OpenAPI schema
    openapi_schema = app.openapi()
    
    # Add server information
    openapi_schema["servers"] = [
        {
            "url": "http://localhost:8000",
            "description": "Development server"
        },
        {
            "url": "https://user-api.worklocal.ca",
            "description": "Production server"
        }
    ]
    
    # Add security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer",
            "description": "API key authentication"
        }
    }
    
    # Save to file
    with open("openapi_spec.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)
    
    print("OpenAPI specification generated: openapi_spec.json")
    print(f"Total endpoints: {len(openapi_schema['paths'])}")
    
    # Print endpoint summary
    print("\nEndpoint Summary:")
    for path, methods in openapi_schema["paths"].items():
        for method, details in methods.items():
            if method in ["get", "post", "put", "delete"]:
                print(f"  {method.upper()} {path} - {details.get('summary', 'No summary')}")

if __name__ == "__main__":
    generate_openapi_spec()