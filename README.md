# AI Document Intelligence & Extraction

A document-field extraction prototype with structured output, field-level rule-match signals, and a human-review indicator.

## Features
- Extract invoice number, date, vendor/supplier, and total from text
- JSON output with missing-field list
- Review-required flag for incomplete documents
- Input size limit, automated tests, and CI

## Run locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
API docs: http://127.0.0.1:8000/docs.

## Example payload
```json
{"text":"Vendor: Acme Ltd\nInvoice Number: INV-123\nDate: 2026-10-01\nTotal: $125.50"}
```

## Honest scope
This version processes extracted text only; it does not parse PDFs, perform OCR, or call a generative model. Confidence values mean a deterministic rule matched; they are not calibrated probabilities. Next steps: add PDF/OCR ingestion, schema validation, and a human-review UI.

## Stack
Python, FastAPI, Pydantic, pytest.
