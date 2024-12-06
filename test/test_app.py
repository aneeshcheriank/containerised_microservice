import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app  # Import the FastAPI app

# Create a TestClient instance
client = TestClient(app)

# Test the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Test the summarize endpoint
@patch("app.summarizer")
def test_summary(mock_summarizer):
    # Mock the summarizer response
    mock_summarizer.return_value = {"summary": "This is a summary."}
    
    response = client.get("/summary/test_text")
    assert response.status_code == 200
    assert mock_summarizer.called
    assert response.json() == {"summary": "This is a summary."}

# Test the ner endpoint
@patch("app.entity_extractor")
def test_ner(mock_entity_extractor):
    # Mock the entity_extractor response
    mock_entity_extractor.return_value = {"entities": ["entity1", "entity2"]}
    
    response = client.get("/ner/test_text")
    assert response.status_code == 200
    assert mock_entity_extractor.called
    assert response.json() == {"entities": ["entity1", "entity2"]}
