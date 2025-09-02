
from datetime import datetime, timezone, timedelta
import json

# NOTE: Minimal placeholder logic (no paid API). You can extend with Skyfield later.
TZ = timezone(timedelta(hours=7))  # Asia/Bangkok
today = datetime.now(TZ).date()

def tone_text(daykey):
    base = {
      'sun': "วันนี้เด่นเรื่องภาวะผู้นำและการตัดสินใจ อย่ากลัวไฟหน้าเวที",
      'mon': "โฟกัสบ้าน/อารมณ์ จัดสภาพแวดล้อมให้สบายก่อนคุยเรื่องใหญ่",
      'tue': "พลังงานเยอะ เดินหน้าโครงการที่ต้องลุย แต่ระวังคำพูดแรง",
      'wed': "การสื่อสาร/เอกสารมาเป็นชุด เคลียร์งานเป็นก้อนจะเร็ว",
      'thu': "โอกาส/เครือข่ายเปิด ขยับเรื่องเรียน-กฎหมาย-ต่างประเทศ",
      'fri': "เสน่ห์/การเงินเด่น ใช้ใจพาไปแต่คุมงบประมาณ",
      'sat': "งานหนักแต่วางรากฐานได้จริง อย่ากังวลกับจังหวะช้า"
    }
    return base[daykey]

payload = {
  "date": str(today),
  "tz": "Asia/Bangkok",
  "generated_at": datetime.now(TZ).isoformat(timespec='seconds'),
  "cards": {
    "sun": {"title": "คนเกิดอาทิตย์", "text": tone_text('sun')},
    "mon": {"title": "คนเกิดจันทร์",  "text": tone_text('mon')},
    "tue": {"title": "คนเกิดอังคาร",  "text": tone_text('tue')},
    "wed": {"title": "คนเกิดพุธ",     "text": tone_text('wed')},
    "thu": {"title": "คนเกิดพฤหัส",   "text": tone_text('thu')},
    "fri": {"title": "คนเกิดศุกร์",   "text": tone_text('fri')},
    "sat": {"title": "คนเกิดเสาร์",   "text": tone_text('sat')}
  }
}

with open('data/daily_transit.json', 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
print("Generated data/daily_transit.json")
