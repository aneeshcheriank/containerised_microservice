from transformers import pipeline
from gliner import GLiNER

ENT_LABELS = [
    "medical_record_number",
    "date_of_birth",
    "ssn",
    "date",
    "first_name",
    "email",
    "last_name",
    "customer_id",
    "employee_id",
    "name",
    "street_address",
    "phone_number",
    "ipv4",
    "credit_card_number",
    "license_plate",
    "address",
    "user_name",
    "device_identifier",
    "bank_routing_number",
    "date_time",
    "company_name",
    "unique_identifier",
    "biometric_identifier",
    "account_number",
    "city",
    "certificate_license_number",
    "time",
    "postcode",
    "vehicle_identifier",
    "coordinate",
    "country",
    "api_key",
    "ipv6",
    "password",
    "health_plan_beneficiary_number",
    "national_id",
    "tax_id",
    "url",
    "state",
    "swift_bic",
    "cvv",
    "pin",
]


def summarizer(text, max_length=142):
    """
    Summarizes the input text using the Transformers pipeline.
    Args:
        text (str): Input text to summarize.
        max_length (int): Maximum length of the summary.
    Returns:
        dict: Summary text as a dictionary.
    """
    pipe = pipeline(
        task="summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e"
    )
    summary = pipe(text, max_length=max_length)[0]["summary_text"]
    return {"summary": summary}


def entity_extractor(text, labels=ENT_LABELS):
    """
    Extracts entities from the input text using GLiNER.
    Args:
        text (str): Input text for entity extraction.
        labels (list): List of entity labels to detect.
    Returns:
        dict: Extracted entities grouped by their label.
    """
    model = GLiNER.from_pretrained("gretelai/gretel-gliner-bi-small-v1.0")
    entities = model.predict_entities(text, labels, threshold=0.7)

    ents = {}
    for entity in entities:
        label = entity["label"]
        if label not in ents:
            ents[label] = []
        ents[label].append(entity)
    return ents
