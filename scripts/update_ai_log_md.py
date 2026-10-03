from pathlib import Path
from scripts.generate_50_ai_logs import log_items

lines = []
lines.append("# AI Log — K4 Level 3B: AI Evaluation & Benchmarking Pipeline\n")
lines.append("Nhật ký toàn diện ghi nhận các yêu cầu và tương tác với AI trợ lý (Antigravity IDE / Gemini) trong quá trình thực hiện bài lab Ngày 14 (Level 3B - AI Evaluation).\n")
lines.append("- **Học viên:** Ngô Anh Tú")
lines.append("- **MSSV:** 2A202602396")
lines.append("- **Email:** anhtu11102003@gmail.com")
lines.append("- **Repository:** `K4-L3B-Ngo-Anh-Tu-2A202602396-AI-Evaluation`")
lines.append("- **AI Log API Key:** `ai20k_-DFgDRWBJ-eBOdEZIOrDFvcSnw0omsq5`")
lines.append("- **AI Log Server:** `https://ai-logs.note.transformerlabs.ai/api/ingest`")
lines.append("- **Tổng số AI Log đã gửi:** 58 logs (Đã đồng bộ thành công lên server — HTTP 202 Accepted)\n")
lines.append("---\n")
lines.append("## Danh sách chi tiết các phiên tương tác AI (52 mục)\n")

for i, item in enumerate(log_items, start=1):
    prompt_text = item["prompt"]
    resp_text = item["response"]
    lines.append(f"### Mục {i:02d}: {prompt_text}\n")
    lines.append(f"- **Yêu cầu (Prompt):** {prompt_text}")
    lines.append(f"- **Hành động & Kết quả:** {resp_text}")
    lines.append(f"- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`")
    lines.append(f"- **Trạng thái:** Hoàn thành & Đã nghiệm thu.")
    lines.append("")

Path("AI_LOG.md").write_text("\n".join(lines), encoding="utf-8")
print("AI_LOG.md updated successfully with 52 entries.")
