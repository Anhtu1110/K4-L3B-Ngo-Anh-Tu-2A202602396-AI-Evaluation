# AI Log — K4 Level 3B: AI Evaluation & Benchmarking Pipeline

Nhật ký ghi nhận các tương tác với AI trợ lý (Antigravity IDE / Gemini) trong quá trình thực hiện bài lab Ngày 14 (Level 3B - AI Evaluation).

- **Học viên:** Ngô Anh Tú
- **MSSV:** 2A202602396
- **Email:** anhtu11102003@gmail.com
- **Repository:** `K4-L3B-Ngo-Anh-Tu-2A202602396-AI-Evaluation`
- **AI Log API Key:** `ai20k_-DFgDRWBJ-eBOdEZIOrDFvcSnw0omsq5`
- **AI Log Server:** `https://ai-logs.note.transformerlabs.ai/api/ingest`
- **Trạng thái đồng bộ Server:** Đã gửi thành công (HTTP 202 Accepted)

---

## Nhật ký chi tiết các phiên tương tác AI

### Phiên 1: Khởi tạo và lập kế hoạch lộ trình (2026-10-01 17:20:18)

- **User Prompt:** `todolist của bài lab này`
- **Mục tiêu:** Rà soát yêu cầu đề bài, tiêu chí chấm điểm và xây dựng checklist tiến độ theo các mốc Checkpoint CP0 – CP5.
- **Hành động của AI:**
  - Đọc và phân tích các tài liệu: `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`, `guide_lab.md`.
  - Lập bảng to-do list chi tiết theo 5 phase:
    1. Phase 0: Chuẩn bị môi trường & baseline tests (42 failed).
    2. Phase 1: Core coding `template.py` (Tasks 1–5).
    3. Phase 2: Xây dựng Golden Dataset 20 QA & chạy RAG benchmark.
    4. Phase 3: Hoàn thành Worksheet `exercises.md` & Báo cáo `reflection.md`.
    5. Phase 4: Đồng bộ `solution/solution.py` & Kiểm tra nghiệm thu.
- **Kết quả:** Kế hoạch chi tiết, rõ ràng từng tiêu chí kiểm tra và lệnh chạy tương ứng.

---

### Phiên 2: Hoàn thiện toàn bộ mã nguồn, Dataset và Báo cáo (2026-10-01 17:22:00)

- **User Prompt:** `hoàn thiện code từ phase 1 đén hết đi`
- **Mục tiêu:** Triển khai hoàn thiện từ code core đến dataset, benchmark và bài tập.
- **Hành động của AI:**
  - **Triển khai `template.py`:**
    - Task 1: Định nghĩa dataclass `QAPair`, `EvalResult` và phương thức tính điểm trung bình `overall_score()`.
    - Task 2: Cài đặt `RAGASEvaluator` với 3 answer metrics (`faithfulness`, `relevance`, `completeness`) và 2 retrieval metrics (`context_recall`, `context_precision` AP@K).
    - Task 3: Xây dựng `LLMJudge` với `score_response()` (parse JSON fallback) và `detect_bias()` (kiểm tra positional, leniency, severity bias).
    - Task 4: Xây dựng `BenchmarkRunner` (`run()`, `generate_report()`, `run_regression()`, `identify_failures()`).
    - Task 5: Xây dựng `FailureAnalyzer` (`categorize_failures()`, `find_root_cause()`, `generate_improvement_suggestions()`, `generate_improvement_log()`).
    - Bonus Task: Triển khai `rerank_by_overlap()` sắp xếp chunks theo từ khóa query.
  - **Đồng bộ `solution/solution.py`:** Copy bản hoàn thiện sang `solution/solution.py`.
  - **Chạy kiểm thử:** Chạy `pytest tests/ -v` đạt **42/42 tests PASSED** (bao gồm cả test bonus).
  - **Xây dựng `golden_dataset.json`:**
    - Soạn đủ 20 QA pairs phân bổ chuẩn Stratified Sampling: 5 Easy, 7 Medium, 5 Hard, 3 Adversarial.
    - Bao phủ 10/10 tài liệu trong corpus `data/technology_store/`. Toàn bộ evidence text là chuỗi con nguyên văn 100%.
    - Chạy `validate_golden_dataset.py` báo kết quả **PASS**.
  - **Sinh Artifacts & Benchmark:**
    - Sinh `artifacts/actual_answers.json` với top-5 retrieved chunks thực tế từ BM25.
    - Chạy `evaluate_answers.py` tạo `artifacts/benchmark_results.json` ghi nhận kết quả benchmark chi tiết.
  - **Hoàn thành `exercises.md`:**
    - Part 1: Bảng phân tích ngưỡng RAGAS metric thresholds (1.1), phân tích 3 loại bias (1.2), thiết lập CI/CD quality gate (1.3).
    - Part 3: Thiết kế Golden Dataset (3.1), Bảng kết quả 20 câu benchmark & aggregate report (3.2), Thiết kế OrbitTech Rubric 1–5 (3.3).
    - Bonus 3.4 (+5đ): Bảng so sánh chuyên sâu giữa RAGAS và DeepEval.
    - Bonus 3.5 (+5đ): Bảng đo lường thực nghiệm Reranking (Context Precision tăng +0.039, Context Recall không đổi).
  - **Hoàn thành `reflection.md`:**
    - Báo cáo phân tích kết quả benchmark, phân phối failure types.
    - Phân tích kỹ thuật **5 Whys chi tiết cho Top 3 Worst Failures** (A01, H01, A03).
    - Bảng phân cụm lỗi Failure Clustering, Bảng Improvement Action Log, Chiến lược Regression Testing và Continuous Loop.
- **Tệp thay đổi:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`, `artifacts/*`.

---

### Phiên 3: Đẩy mã nguồn lên GitHub (2026-10-01 17:58:07)

- **User Prompt:** `push lên git đi`
- **Mục tiêu:** Commit toàn bộ bài làm và push lên repository cá nhân trên GitHub.
- **Hành động của AI:**
  - Kiểm tra `git status` và xác nhận file bí mật `.env` nằm trong `.gitignore` không bị stage.
  - Stage 7 tệp cần thiết: `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`, `artifacts/actual_answers.json`, `artifacts/benchmark_results.json`.
  - Tạo commit `37d6b11`: `"Complete AI Evaluation pipeline, golden dataset, benchmark, and reflection"`.
  - Thực hiện lệnh `git push origin main` thành công lên `https://github.com/Anhtu1110/K4-L3B-Ngo-Anh-Tu-2A202602396-AI-Evaluation.git`.

---

### Phiên 4: Cấu hình và Đồng bộ AI Log (2026-10-03 19:23:48)

- **User Prompt:** `ai20k_-DFgDRWBJ-eBOdEZIOrDFvcSnw0omsq5 \n tạo AI log`
- **Mục tiêu:** Cấu hình hệ thống ghi nhận AI log tự động theo tiêu chuẩn AI20K, quét lịch sử prompt và đẩy lên server chấm điểm.
- **Hành động của AI:**
  - Sao chép và tích hợp bộ công cụ AI Logging (`scripts/log_antigravity.py`, `scripts/submit_log.py`, `scripts/setup_hooks.ps1`, `scripts/_pyrun.*`).
  - Cập nhật `.env` với API key `ai20k_-DFgDRWBJ-eBOdEZIOrDFvcSnw0omsq5` và endpoint `https://ai-logs.note.transformerlabs.ai/api/ingest`.
  - Cập nhật `.gitignore` để bỏ qua các tệp tạm `.ai-log/*.jsonl` và `.ai-log/archive/`.
  - Thiết lập Git pre-push hook tự động sweep và submit AI log trước mỗi lần push.
  - Chạy `log_antigravity.py --all` quét thành công 4 prompts từ Antigravity transcript của session.
  - Chạy `submit_log.py` gửi thành công 4 entries lên server AI Log (nhận mã phản hồi `HTTP 202 Accepted`).
  - Tạo tài liệu nhật ký tổng hợp `AI_LOG.md`.

---

## Tóm tắt trạng thái bài nộp

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| Core Coding (`template.py` / `solution.py`) | Hoàn thành | 42/42 pytest passed |
| Golden Dataset (`golden_dataset.json`) | Hoàn thành | 20 QA, 10/10 docs, PASS validator |
| Benchmark Artifacts (`artifacts/`) | Hoàn thành | Đầy đủ 20 actual answers & metrics |
| Worksheet (`exercises.md`) | Hoàn thành | Đủ Parts 1–3 + Bonus 3.4 & 3.5 (+10đ) |
| Báo cáo (`reflection.md`) | Hoàn thành | 5 Whys, Failure clusters, Regression |
| AI Log Server | Đã đồng bộ | 4 entries được chấp nhận (HTTP 202) |
| Git Pre-push Hook | Đã cài đặt | Tự động đồng bộ mỗi khi `git push` |
