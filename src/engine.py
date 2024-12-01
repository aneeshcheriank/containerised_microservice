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


def summarizer(text):
    pipe = pipeline(
        task="summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e"
    )
    summary = pipe(text)[0]["summary_text"]
    return {"summary": summary}


def entity_extractor(text, labels=ENT_LABELS):
    model = GLiNER.from_pretrained("gretelai/gretel-gliner-bi-small-v1.0")
    entities = model.predict_entities(text, labels, threshold=0.7)

    # Display the detected entities
    ents = {}
    for entity in entities:
        if entity["label"] not in ents:
            key = entity["label"]
            ents[key] = []
            ents[key].append(entity)
        else:
            ents[entity["label"]].append(entity)
    return ents


if __name__ == "__main__":
    text = """
Purchase Order
----------------
Date: 10/05/2023
----------------
Customer Name: CID-982305
Billing Address: 1234 Oak Street, Suite 400, Springfield, IL, 62704
Phone: (312) 555-7890 (555-876-5432)
Email: janedoe@company.com
"""
    print(entity_extractor(text))
