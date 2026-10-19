from app import extract
def test_extracts_invoice_fields():
 r=extract("Vendor: Acme Ltd\nInvoice Number: INV-123\nDate: 2026-10-01\nTotal: $125.50")
 assert r["fields"]["invoice_number"]=="INV-123"
 assert r["fields"]["total"]=="125.50"
 assert not r["review_required"]
def test_missing_fields_require_review():
 assert extract("Invoice Number: INV-1")["review_required"]
