from fastapi import FastAPI
from pydantic import BaseModel, Field
import re
app=FastAPI(title="AI Document Intelligence & Extraction",version="0.1.0")
PATTERNS={"invoice_number":r"(?:invoice(?: number| #| no\.?)?)\s*[:#-]?\s*([A-Z0-9-]+)","date":r"date\s*[:#-]?\s*(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})","total":r"(?:total|amount due)\s*[:$ ]*\$?\s*([0-9,]+\.\d{2})","vendor":r"(?:vendor|supplier)\s*[:#-]?\s*([^\n]+)"}
class Request(BaseModel):
 text:str=Field(min_length=1,max_length=50000)
def extract(text):
 fields={k:(m.group(1).strip() if (m:=re.search(p,text,re.I)) else None) for k,p in PATTERNS.items()}
 missing=[k for k,v in fields.items() if v is None]
 return {"fields":fields,"confidence":{k:(0.95 if v is not None else 0.0) for k,v in fields.items()},"missing_fields":missing,"review_required":bool(missing),"method":"regex baseline; confidence is a rule-match signal, not calibrated probability"}
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/extract")
def endpoint(r:Request): return extract(r.text)
