import pytest
from unittest.mock import patch

# Mock data for testing
MOCK_TEXT = """
Purchase Order
----------------
Date: 10/05/2023
----------------
Customer Name: CID-982305
Billing Address: 1234 Oak Street, Suite 400, Springfield, IL, 62704
Phone: (312) 555-7890 (555-876-5432)
Email: janedoe@company.com
"""

MOCK_SUMMARY = {
    "summary": " Customer Name: CID-982305. \xa0Purchase Order. Buyer Name: 1234 Oak Street, Suite 400, Springfield, IL, 62704 . Phone: (312 555-7890 (555-876-5432) Email: janedoe@company.com.com ."
}

MOCK_ENTITIES = {
    "date": [{"label": "date", "text": "10/05/2023", "start": 17, "end": 27}],
    "customer_id": [
        {"label": "customer_id", "text": "CID-982305", "start": 56, "end": 66}
    ],
    "address": [
        {
            "label": "address",
            "text": "1234 Oak Street, Suite 400, Springfield, IL, 62704",
            "start": 82,
            "end": 140,
        }
    ],
    "phone_number": [
        {"label": "phone_number", "text": "(312) 555-7890", "start": 149, "end": 162},
        {"label": "phone_number", "text": "555-876-5432", "start": 164, "end": 176},
    ],
    "email": [
        {"label": "email", "text": "janedoe@company.com", "start": 185, "end": 204}
    ],
}


# Mocking the GLiNER model
class MockGLiNER:
    @staticmethod
    def from_pretrained(model_name):
        return MockGLiNER()

    def predict_entities(self, text, labels, threshold):
        return [
            {"label": "date", "text": "10/05/2023", "start": 17, "end": 27},
            {"label": "customer_id", "text": "CID-982305", "start": 56, "end": 66},
            {
                "label": "address",
                "text": "1234 Oak Street, Suite 400, Springfield, IL, 62704",
                "start": 82,
                "end": 140,
            },
            {
                "label": "phone_number",
                "text": "(312) 555-7890",
                "start": 149,
                "end": 162,
            },
            {"label": "phone_number", "text": "555-876-5432", "start": 164, "end": 176},
            {"label": "email", "text": "janedoe@company.com", "start": 185, "end": 204},
        ]


# Test for summarizer
@patch("transformers.pipeline")
def test_summarizer(mock_pipeline):
    mock_pipe = mock_pipeline.return_value
    mock_pipe.side_effect = lambda text, max_length=142, **kwargs: [
        {"summary_text": MOCK_SUMMARY["summary"]}
    ]

    from src.engine import summarizer

    result = summarizer(MOCK_TEXT, max_length=142)
    assert result == MOCK_SUMMARY


# Test for entity_extractor
@patch("src.engine.GLiNER", new=MockGLiNER)
def test_entity_extractor():
    from src.engine import entity_extractor

    result = entity_extractor(MOCK_TEXT)
    assert result == MOCK_ENTITIES
