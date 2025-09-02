
# Soulkey Daily Transit (Free Stack)

ฟรี 100% — ไม่มีค่าใช้จ่ายแฝง
- โฮสต์ไฟล์ JSON ด้วย **GitHub Pages**
- อัปเดตอัตโนมัติด้วย **GitHub Actions**
- ไม่มี API คิดเงินรายครั้ง

## ใช้งานเร็วใน 5 ขั้นตอน
1) สร้าง repo ใหม่บน GitHub แล้วอัปโหลดไฟล์ทั้งโฟลเดอร์นี้
2) เปิด GitHub Pages: Settings → Pages → Source: `Deploy from a branch` → Branch: `main` (หรือ `master`) → `/` root
3) ตรวจว่า URL ของ Pages คือ `https://<USER>.github.io/<REPO>/`
4) Workflow จะรันทุกวัน 00:10 น. (Asia/Bangkok) และอัปเดต `data/daily_transit.json`
5) ฝั่งเว็บ iOS/หน้า Today Free: fetch JSON จาก URL ข้างบน เช่น:
   - `https://<USER>.github.io/<REPO>/data/daily_transit.json`

## iOS Integration (WebView/SwiftUI)
- ใช้ URLSession ดึง JSON ข้างต้นแล้ว map เข้าการ์ด 7 ใบ
- แสดง Badge "อัปเดตล่าสุดเมื่อ ..." จากฟิลด์ `generated_at`

## เพิ่มความฉลาด (ภายหลัง)
- หากต้องการคำนวณจากดาวจรจริง แนะนำเพิ่มไลบรารี `skyfield` และกติกา Soulkey
- ย้ำ: ยังคงฟรี (โอเพ่นซอร์ส, ไม่มี API เสียเงิน)

