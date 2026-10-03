# AI Log — K4 Level 3B: AI Evaluation & Benchmarking Pipeline

Nhật ký toàn diện ghi nhận các yêu cầu và tương tác với AI trợ lý (Antigravity IDE / Gemini) trong quá trình thực hiện bài lab Ngày 14 (Level 3B - AI Evaluation).

- **Học viên:** Ngô Anh Tú
- **MSSV:** 2A202602396
- **Email:** anhtu11102003@gmail.com
- **Repository:** `K4-L3B-Ngo-Anh-Tu-2A202602396-AI-Evaluation`
- **AI Log API Key:** `ai20k_-DFgDRWBJ-eBOdEZIOrDFvcSnw0omsq5`
- **AI Log Server:** `https://ai-logs.note.transformerlabs.ai/api/ingest`
- **Tổng số AI Log đã gửi:** 58 logs (Đã đồng bộ thành công lên server — HTTP 202 Accepted)

---

## Danh sách chi tiết các phiên tương tác AI (52 mục)

### Mục 01: Giải thích mục tiêu và cấu trúc bài lab AI Evaluation & Benchmarking Pipeline Ngày 14

- **Yêu cầu (Prompt):** Giải thích mục tiêu và cấu trúc bài lab AI Evaluation & Benchmarking Pipeline Ngày 14
- **Hành động & Kết quả:** Phân tích 6 mục tiêu cốt lõi: tự động hóa evaluation pipeline, triển khai RAGAS metrics, LLM-as-a-Judge rubric 1-5, stratified sampling golden dataset, failure analysis 5 Whys, và quality gate trong CI/CD.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 02: Khởi tạo môi trường ảo Python venv, cài đặt requirements.txt và giải thích lý do cần Python 3.11+

- **Yêu cầu (Prompt):** Khởi tạo môi trường ảo Python venv, cài đặt requirements.txt và giải thích lý do cần Python 3.11+
- **Hành động & Kết quả:** Thiết lập môi trường .venv, cài đặt các thư viện pytest, openai, python-dotenv; giải thích cú pháp type hinting hiện đại `str | None` và chuẩn dataclass yêu cầu Python 3.11 trở lên.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 03: Chạy bộ test baseline ban đầu và phân tích nguyên nhân 42 tests failed

- **Yêu cầu (Prompt):** Chạy bộ test baseline ban đầu và phân tích nguyên nhân 42 tests failed
- **Hành động & Kết quả:** Thực hiện lệnh `pytest tests/ -v`, ghi nhận 42 tests failed do starter template.py và solution/solution.py chưa hoàn thành các khối TODO của 5 task.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 04: Phân biệt vai trò của template.py (evaluation engine) và domain_assistant.py (system under evaluation)

- **Yêu cầu (Prompt):** Phân biệt vai trò của template.py (evaluation engine) và domain_assistant.py (system under evaluation)
- **Hành động & Kết quả:** Làm rõ nguyên tắc đánh giá độc lập: domain_assistant.py là hệ thống RAG sinh câu trả lời; template.py là công cụ chấm điểm độc lập. Domain assistant chỉ đọc question mà không đọc expected_answer để tránh data leakage.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 05: Thiết kế dataclass QAPair: các trường bắt buộc, typing và default_factory cho metadata và retrieved_contexts

- **Yêu cầu (Prompt):** Thiết kế dataclass QAPair: các trường bắt buộc, typing và default_factory cho metadata và retrieved_contexts
- **Hành động & Kết quả:** Định nghĩa QAPair gồm question, expected_answer, context, metadata (dict default_factory), retrieved_contexts (list default_factory) theo đúng interface của đề bài.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 06: Thiết kế dataclass EvalResult: phân định answer-side metrics vs retrieval-side metrics

- **Yêu cầu (Prompt):** Thiết kế dataclass EvalResult: phân định answer-side metrics vs retrieval-side metrics
- **Hành động & Kết quả:** Định nghĩa EvalResult gồm qa_pair, actual_answer, 3 answer metrics (faithfulness, relevance, completeness), passed, failure_type và 2 retrieval metrics tùy chọn (context_precision, context_recall).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 07: Cài đặt hàm EvalResult.overall_score() tính trung bình cộng 3 answer metrics

- **Yêu cầu (Prompt):** Cài đặt hàm EvalResult.overall_score() tính trung bình cộng 3 answer metrics
- **Hành động & Kết quả:** Triển khai overall_score() = (faithfulness + relevance + completeness) / 3.0; đảm bảo trả về giá trị float chuẩn hóa trong khoảng 0.0 đến 1.0.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 08: Tại sao retrieval metrics (context_recall, context_precision) không được tính vào overall_score()?

- **Yêu cầu (Prompt):** Tại sao retrieval metrics (context_recall, context_precision) không được tính vào overall_score()?
- **Hành động & Kết quả:** Giải thích: Retrieval metrics phản ánh hiệu năng của Retriever, trong khi overall_score đánh giá chất lượng đầu ra cuối cùng của câu trả lời gửi đến người dùng; giữ tách biệt giúp chẩn đoán chính xác nguyên nhân lỗi.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 09: Kiểm thử unit test cho Task 1 Data Models: pytest tests/test_solution.py::TestEvalResultOverallScore

- **Yêu cầu (Prompt):** Kiểm thử unit test cho Task 1 Data Models: pytest tests/test_solution.py::TestEvalResultOverallScore
- **Hành động & Kết quả:** Chạy test và đạt 3/3 passed cho các trường hợp điểm trung bình, all zeros (0.0) và all ones (1.0).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 10: Tìm hiểu khái niệm RAGAS: 4 nhóm metric và luồng Question -> Retriever -> Context -> Generator -> Answer

- **Yêu cầu (Prompt):** Tìm hiểu khái niệm RAGAS: 4 nhóm metric và luồng Question -> Retriever -> Context -> Generator -> Answer
- **Hành động & Kết quả:** Phân tích 4 nhóm metric: Task Completion, Answer Quality, RAG-Specific, Business; đối chiếu từng chặng trong RAG Triad với các chỉ số đánh giá tương ứng.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 11: Cài đặt hàm _tokenize(): chuyển chữ thường, regex tách từ và lọc stopwords tiếng Anh

- **Yêu cầu (Prompt):** Cài đặt hàm _tokenize(): chuyển chữ thường, regex tách từ và lọc stopwords tiếng Anh
- **Hành động & Kết quả:** Triển khai hàm tách từ với regex `\b\w+\b`, chuyển lower-case và loại bỏ các stopwords phổ biến để tránh làm sai lệch điểm số trùng lặp.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 12: Tại sao cần loại bỏ stopwords khi tính word overlap heuristic trong RAGAS?

- **Yêu cầu (Prompt):** Tại sao cần loại bỏ stopwords khi tính word overlap heuristic trong RAGAS?
- **Hành động & Kết quả:** Giải thích: Các từ đệm như 'is', 'the', 'a' xuất hiện liên tục trong mọi văn bản; nếu không loại bỏ, chúng sẽ thổi phồng điểm overlap của các câu trả lời sai lệch hoặc lạc đề.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 13: Cài đặt RAGASEvaluator.evaluate_faithfulness(): đo lường mức độ grounded của answer trong context

- **Yêu cầu (Prompt):** Cài đặt RAGASEvaluator.evaluate_faithfulness(): đo lường mức độ grounded của answer trong context
- **Hành động & Kết quả:** Tính tỷ lệ giao giữa token câu trả lời và context chia cho tổng số token câu trả lời: `|answer ∩ context| / |answer|`, clamp giá trị [0.0, 1.0].
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 14: Xử lý edge case trong evaluate_faithfulness khi answer hoặc context rỗng

- **Yêu cầu (Prompt):** Xử lý edge case trong evaluate_faithfulness khi answer hoặc context rỗng
- **Hành động & Kết quả:** Quy ước trả về 1.0 khi answer rỗng theo tài liệu đặc tả; trả về 0.0 nếu context rỗng nhưng answer có nội dung.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 15: Cài đặt RAGASEvaluator.evaluate_relevance(): đo lường độ liên quan giữa answer và question

- **Yêu cầu (Prompt):** Cài đặt RAGASEvaluator.evaluate_relevance(): đo lường độ liên quan giữa answer và question
- **Hành động & Kết quả:** Tính tỷ lệ trùng lặp token giữa câu trả lời và câu hỏi chia cho độ dài câu hỏi: `|answer ∩ question| / |question|`, clamp giá trị trong [0.0, 1.0].
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 16: Cài đặt RAGASEvaluator.evaluate_completeness(): đo lường mức độ bao phủ của answer so với expected_answer

- **Yêu cầu (Prompt):** Cài đặt RAGASEvaluator.evaluate_completeness(): đo lường mức độ bao phủ của answer so với expected_answer
- **Hành động & Kết quả:** Tính độ phủ của answer trên ground truth: `|answer ∩ expected| / |expected|`, phản ánh mức độ đáp ứng đầy đủ các ý chính của chuyên gia.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 17: Khái niệm Context Recall: tại sao đo lường độ bao phủ trên hợp (union) của các retrieved chunks?

- **Yêu cầu (Prompt):** Khái niệm Context Recall: tại sao đo lường độ bao phủ trên hợp (union) của các retrieved chunks?
- **Hành động & Kết quả:** Context Recall đo lường xem toàn bộ tập chunks được retriever kéo về có chứa đủ dữ kiện để trả lời câu hỏi hay không: `|expected ∩ ⋃chunks| / |expected|`.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 18: Cài đặt RAGASEvaluator.evaluate_context_recall() và xử lý trường hợp expected_answer rỗng

- **Yêu cầu (Prompt):** Cài đặt RAGASEvaluator.evaluate_context_recall() và xử lý trường hợp expected_answer rỗng
- **Hành động & Kết quả:** Gộp tập hợp token của tất cả chunks, tính tỷ lệ giao với expected tokens; trả về 1.0 nếu expected rỗng và 0.0 nếu không có chunks nào.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 19: Khái niệm Context Precision: tại sao cần rank-aware Average Precision@K thay vì precision thông thường?

- **Yêu cầu (Prompt):** Khái niệm Context Precision: tại sao cần rank-aware Average Precision@K thay vì precision thông thường?
- **Hành động & Kết quả:** Trong RAG, chunk xếp đầu tiên có ảnh hưởng mạnh nhất đến generator do hiện tượng Lost-in-the-Middle; Rank-aware AP@K thưởng điểm cao khi chunk liên quan đứng đầu danh sách.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 20: Cài đặt RAGASEvaluator.evaluate_context_precision() với ngưỡng relevance_threshold = 0.1

- **Yêu cầu (Prompt):** Cài đặt RAGASEvaluator.evaluate_context_precision() với ngưỡng relevance_threshold = 0.1
- **Hành động & Kết quả:** Xác định chunk liên quan nếu cover >= 10% token expected; tính Precision@k tại mỗi vị trí và lấy trung bình AP@K trên tổng số chunks liên quan.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 21: Giải thích công thức toán học AP@K trong RAGAS: rewards relevant chunks xếp trước noise chunks

- **Yêu cầu (Prompt):** Giải thích công thức toán học AP@K trong RAGAS: rewards relevant chunks xếp trước noise chunks
- **Hành động & Kết quả:** Chứng minh: nếu relevant chunk nằm ở rank 1, Precision@1 = 1.0; nếu bị đẩy xuống rank 2 sau noise chunk, Precision@2 = 0.5; AP@K giảm một nửa dù tập retrieved như nhau.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 22: Triển khai RAGASEvaluator.run_full_eval(): kết nối answer metrics và optional retrieval metrics

- **Yêu cầu (Prompt):** Triển khai RAGASEvaluator.run_full_eval(): kết nối answer metrics và optional retrieval metrics
- **Hành động & Kết quả:** Tích hợp tính toán đồng thời cả 3 answer metrics và 2 retrieval metrics (nếu có contexts); thiết lập trường passed khi cả 3 answer metrics >= 0.5.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 23: Phân loại lỗi theo thứ tự ưu tiên trong run_full_eval: hallucination (<0.3), irrelevant (<0.3), incomplete (<0.3), off_topic

- **Yêu cầu (Prompt):** Phân loại lỗi theo thứ tự ưu tiên trong run_full_eval: hallucination (<0.3), irrelevant (<0.3), incomplete (<0.3), off_topic
- **Hành động & Kết quả:** Cài đặt quy tắc first-match wins: ưu tiên phát hiện hallucination (faithfulness < 0.3), kế đến irrelevant (relevance < 0.3), incomplete (completeness < 0.3), và cuối cùng off_topic.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 24: Tại sao retrieval metrics chẩn đoán retriever nhưng không làm thay đổi rule pass (>=0.5) của answer?

- **Yêu cầu (Prompt):** Tại sao retrieval metrics chẩn đoán retriever nhưng không làm thay đổi rule pass (>=0.5) của answer?
- **Hành động & Kết quả:** Một retriever có thể bị noise nhưng generator vẫn trả lời đúng nhờ lọc nhiễu tốt; do đó quyết định Pass/Fail của phản hồi người dùng chỉ dựa trên chất lượng Answer.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 25: Kiểm thử unit test cho Task 2 RAGAS Evaluator và Retrieval Metrics (14 tests passed)

- **Yêu cầu (Prompt):** Kiểm thử unit test cho Task 2 RAGAS Evaluator và Retrieval Metrics (14 tests passed)
- **Hành động & Kết quả:** Chạy pytest trên TestRAGASEvaluator và TestContextMetrics, xác nhận pass toàn bộ các kịch bản fully grounded, unrelated, full coverage, rank-aware AP@K.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 26: Triển khai bonus helper rerank_by_overlap(): sắp xếp chunks theo lexical overlap với query

- **Yêu cầu (Prompt):** Triển khai bonus helper rerank_by_overlap(): sắp xếp chunks theo lexical overlap với query
- **Hành động & Kết quả:** Cài đặt hàm sắp xếp lại các chunks dựa trên số lượng token trùng khớp với query giảm dần, mô phỏng hoạt động của cross-encoder reranker.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 27: Giải thích tại sao Reranking có thể tăng Context Precision mà không làm thay đổi Context Recall

- **Yêu cầu (Prompt):** Giải thích tại sao Reranking có thể tăng Context Precision mà không làm thay đổi Context Recall
- **Hành động & Kết quả:** Reranking chỉ đảo thứ tự các phần tử trong tập hợp sẵn có mà không thêm/bớt phần tử; do đó hợp các token không đổi (Recall không đổi), nhưng đưa chunk đúng lên đầu làm tăng AP@K.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 28: Kiểm thử unit test cho bonus reranker: test_reranking_improves_or_keeps_precision

- **Yêu cầu (Prompt):** Kiểm thử unit test cho bonus reranker: test_reranking_improves_or_keeps_precision
- **Hành động & Kết quả:** Chạy test xác nhận rerank_by_overlap giúp nâng cao Context Precision từ 0.5 lên 1.0 đối với chuỗi [noise, relevant], pass thành công test bonus.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 29: Kiến trúc LLM-as-a-Judge: vai trò của prompt, reference answer và rubric thang điểm 1-5

- **Yêu cầu (Prompt):** Kiến trúc LLM-as-a-Judge: vai trò của prompt, reference answer và rubric thang điểm 1-5
- **Hành động & Kết quả:** Phân tích cấu trúc prompt cho LLM Judge: cung cấp ngữ cảnh, câu hỏi, câu trả lời, tiêu chuẩn rubric chi tiết từ 1 đến 5 và yêu cầu xuất điểm số kèm lập luận (CoT).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 30: Cài đặt LLMJudge.__init__() và phương thức score_response() với JSON parsing và regex fallback

- **Yêu cầu (Prompt):** Cài đặt LLMJudge.__init__() và phương thức score_response() với JSON parsing và regex fallback
- **Hành động & Kết quả:** Xây dựng prompt rubric, gọi judge_llm_fn, dùng regex bóc tách JSON và parse dict điểm số; tự động fallback về 0.5 cho tiêu chí không parse được.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 31: Cơ chế fallback trong LLMJudge: xử lý khi LLM trả về text không hợp lệ hoặc thiếu tiêu chí

- **Yêu cầu (Prompt):** Cơ chế fallback trong LLMJudge: xử lý khi LLM trả về text không hợp lệ hoặc thiếu tiêu chí
- **Hành động & Kết quả:** Bọc khối try-catch quanh json.loads; nếu lỗi cú pháp, tự động gán giá trị mặc định 0.5 cho tất cả tiêu chí có trong rubric để đảm bảo pipeline không bị crash.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 32: Phân tích 3 loại bias thường gặp ở LLM Judge: Positional bias, Verbosity bias, Self-preference

- **Yêu cầu (Prompt):** Phân tích 3 loại bias thường gặp ở LLM Judge: Positional bias, Verbosity bias, Self-preference
- **Hành động & Kết quả:** Phân tích hiện tượng ưu tiên câu trả lời đầu tiên, thiên vị câu trả lời dài và ưa chuộng văn phong của chính kiến trúc model đó; đề xuất các giải pháp kiểm soát.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 33: Cài đặt LLMJudge.detect_bias(): kiểm tra positional bias, leniency bias (>0.8) và severity bias (<0.3)

- **Yêu cầu (Prompt):** Cài đặt LLMJudge.detect_bias(): kiểm tra positional bias, leniency bias (>0.8) và severity bias (<0.3)
- **Hành động & Kết quả:** Tính điểm trung bình toàn batch; cảnh báo leniency nếu avg > 0.8, severity nếu avg < 0.3; kiểm tra vị trí đầu có điểm số vượt trội nhất quán để gắn cờ positional bias.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 34: Kiểm thử unit test cho Task 3 LLMJudge (4 tests passed)

- **Yêu cầu (Prompt):** Kiểm thử unit test cho Task 3 LLMJudge (4 tests passed)
- **Hành động & Kết quả:** Chạy pytest trên TestLLMJudge, xác nhận trả về đúng cấu trúc dict, có trường scores, reasoning và phát hiện chính xác các loại bias.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 35: Thiết kế BenchmarkRunner: điều phối đánh giá hàng loạt tập QA pairs qua agent_fn và evaluator

- **Yêu cầu (Prompt):** Thiết kế BenchmarkRunner: điều phối đánh giá hàng loạt tập QA pairs qua agent_fn và evaluator
- **Hành động & Kết quả:** Xây dựng lớp runner nhận danh sách QAPair, gọi agent sinh câu trả lời, truyền retrieved_contexts vào run_full_eval và lưu trữ kết quả EvalResult tương ứng.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 36: Cài đặt BenchmarkRunner.run(): chuyển tiếp pair.retrieved_contexts vào run_full_eval

- **Yêu cầu (Prompt):** Cài đặt BenchmarkRunner.run(): chuyển tiếp pair.retrieved_contexts vào run_full_eval
- **Hành động & Kết quả:** Đảm bảo đối số contexts nhận đúng pair.retrieved_contexts để kích hoạt việc tính toán 2 retrieval metrics trong EvalResult.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 37: Cài đặt BenchmarkRunner.generate_report(): tính pass rate, average answer metrics và average retrieval metrics

- **Yêu cầu (Prompt):** Cài đặt BenchmarkRunner.generate_report(): tính pass rate, average answer metrics và average retrieval metrics
- **Hành động & Kết quả:** Tổng hợp báo cáo thống kê: tổng số case, số case pass, tỷ lệ pass_rate, trung bình các answer metrics và trung bình các retrieval metrics (loại trừ None).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 38: Cài đặt BenchmarkRunner.run_regression(): phát hiện metric bị sụt giảm quá 0.05 so với baseline

- **Yêu cầu (Prompt):** Cài đặt BenchmarkRunner.run_regression(): phát hiện metric bị sụt giảm quá 0.05 so với baseline
- **Hành động & Kết quả:** So sánh trung bình 3 answer metrics giữa đợt chạy mới và baseline; nếu metric nào giảm > 0.05 thì đưa vào danh sách regressions và đặt passed = False.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 39: Tại sao kiểm thử hồi quy (regression testing) đóng vai trò Quality Gate quan trọng trong CI/CD pipeline?

- **Yêu cầu (Prompt):** Tại sao kiểm thử hồi quy (regression testing) đóng vai trò Quality Gate quan trọng trong CI/CD pipeline?
- **Hành động & Kết quả:** Khi tối ưu prompt hoặc thay đổi model, có thể tăng điểm câu hỏi này nhưng làm hỏng câu hỏi khác; regression gate tự động ngăn chặn deploy phiên bản bị thụt lùi chất lượng.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 40: Cài đặt BenchmarkRunner.identify_failures(): lọc danh sách các kết quả có điểm dưới ngưỡng threshold

- **Yêu cầu (Prompt):** Cài đặt BenchmarkRunner.identify_failures(): lọc danh sách các kết quả có điểm dưới ngưỡng threshold
- **Hành động & Kết quả:** Duyệt qua danh sách kết quả, lọc các EvalResult có bất kỳ chỉ số nào trong 3 answer metrics thấp hơn threshold (mặc định 0.5).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 41: Thiết kế FailureAnalyzer: nguyên lý Failure Clustering và Continuous Improvement Loop

- **Yêu cầu (Prompt):** Thiết kế FailureAnalyzer: nguyên lý Failure Clustering và Continuous Improvement Loop
- **Hành động & Kết quả:** Xây dựng quy trình gom cụm lỗi (cluster before fix): sửa 1 nguyên nhân gốc rễ có thể giải quyết nhiều ca thất bại cùng lúc theo vòng lặp Evaluate -> Analyze -> Improve -> Repeat.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 42: Cài đặt FailureAnalyzer.categorize_failures(): thống kê số lượng failure theo từng loại failure_type

- **Yêu cầu (Prompt):** Cài đặt FailureAnalyzer.categorize_failures(): thống kê số lượng failure theo từng loại failure_type
- **Hành động & Kết quả:** Đếm số lần xuất hiện của từng loại lỗi (hallucination, irrelevant, incomplete, off_topic) trong danh sách các ca thất bại.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 43: Cài đặt FailureAnalyzer.find_root_cause(): chẩn đoán nguyên nhân gốc rễ dựa trên metric thấp nhất

- **Yêu cầu (Prompt):** Cài đặt FailureAnalyzer.find_root_cause(): chẩn đoán nguyên nhân gốc rễ dựa trên metric thấp nhất
- **Hành động & Kết quả:** So sánh 3 chỉ số: nếu faithfulness thấp nhất -> lỗi retrieval; relevance thấp nhất -> prompt ambiguous; completeness thấp nhất -> thiếu context/window; nếu bằng nhau -> multiple issues.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 44: Cài đặt FailureAnalyzer.generate_improvement_suggestions(): đề xuất tối thiểu 3 hành động khắc phục cụ thể

- **Yêu cầu (Prompt):** Cài đặt FailureAnalyzer.generate_improvement_suggestions(): đề xuất tối thiểu 3 hành động khắc phục cụ thể
- **Hành động & Kết quả:** Dựa trên phân loại lỗi, sinh tối thiểu 3 khuyến nghị hành động cụ thể: bổ sung hallucination checker, tăng chunk size RAG, thêm few-shot prompt examples.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 45: Cài đặt FailureAnalyzer.generate_improvement_log(): xuất bảng Markdown ghi nhận lỗi và giải pháp tương ứng

- **Yêu cầu (Prompt):** Cài đặt FailureAnalyzer.generate_improvement_log(): xuất bảng Markdown ghi nhận lỗi và giải pháp tương ứng
- **Hành động & Kết quả:** Định dạng bảng Markdown chuẩn với các cột: Failure ID, Type, Root Cause, Suggested Fix, Status ('Open') phục vụ việc theo dõi khắc phục lỗi.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 46: Chạy full test suite và kiểm tra 42/42 tests passed: phân tích thứ tự ưu tiên giữa template.py và solution/solution.py

- **Yêu cầu (Prompt):** Chạy full test suite và kiểm tra 42/42 tests passed: phân tích thứ tự ưu tiên giữa template.py và solution/solution.py
- **Hành động & Kết quả:** Phát hiện test suite ưu tiên load solution/solution.py; đồng bộ toàn bộ code hoàn chỉnh từ template.py sang solution.py; chạy pytest đạt 42/42 PASSED tuyệt đối.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 47: Thiết kế Golden Dataset 20 QA bằng Stratified Sampling: 5 Easy, 7 Medium, 5 Hard, 3 Adversarial

- **Yêu cầu (Prompt):** Thiết kế Golden Dataset 20 QA bằng Stratified Sampling: 5 Easy, 7 Medium, 5 Hard, 3 Adversarial
- **Hành động & Kết quả:** Xây dựng 20 cặp QA phân tầng: 5 Easy tra cứu trực tiếp, 7 Medium kết hợp 2 điều kiện, 5 Hard đa chính sách/đa điều kiện, 3 Adversarial (out-of-scope, prompt injection, false premise).
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 48: Đảm bảo nguyên tắc Provenance và Verbatim Evidence: trích xuất chuỗi con chính xác 100% từ 10 docs OrbitTech

- **Yêu cầu (Prompt):** Đảm bảo nguyên tắc Provenance và Verbatim Evidence: trích xuất chuỗi con chính xác 100% từ 10 docs OrbitTech
- **Hành động & Kết quả:** Sử dụng script đối chiếu tự động, xác nhận tất cả context evidence trong golden_dataset.json đều là chuỗi con nguyên văn từ 10 tài liệu trong data/technology_store/.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 49: Kiểm tra Golden Dataset bằng validate_golden_dataset.py: giải thích kết quả PASS

- **Yêu cầu (Prompt):** Kiểm tra Golden Dataset bằng validate_golden_dataset.py: giải thích kết quả PASS
- **Hành động & Kết quả:** Chạy validator chính thức của bài lab, kết quả xác thực đạt PASS với 20/20 records, tỷ lệ bao phủ tài liệu 10/10, đúng cấu trúc hợp đồng dữ liệu.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 50: Chạy RAG Assistant sinh actual_answers.json và adapter evaluate_answers.py tạo benchmark_results.json

- **Yêu cầu (Prompt):** Chạy RAG Assistant sinh actual_answers.json và adapter evaluate_answers.py tạo benchmark_results.json
- **Hành động & Kết quả:** Chạy BM25 retriever và bộ sinh câu trả lời để tạo actual_answers.json; chạy evaluate_answers.py tính toán toàn bộ 5 metrics và xuất benchmark_results.json.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 51: Thực hiện kỹ thuật 5 Whys cho Top 3 Worst Failures (A01, H01, A03) và xây dựng Rubric OrbitTech trong exercises.md / reflection.md

- **Yêu cầu (Prompt):** Thực hiện kỹ thuật 5 Whys cho Top 3 Worst Failures (A01, H01, A03) và xây dựng Rubric OrbitTech trong exercises.md / reflection.md
- **Hành động & Kết quả:** Phân tích sâu nguyên nhân gốc rễ cho 3 ca lỗi tiêu biểu bằng 5 Whys, thiết kế Rubric domain OrbitTech 1-5, hoàn thành bài tập so sánh framework và reranking.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.

### Mục 52: Thiết lập Git pre-push hook tự động hóa quy trình ghi nhận và đồng bộ AI log lên server chấm điểm AI20K

- **Yêu cầu (Prompt):** Thiết lập Git pre-push hook tự động hóa quy trình ghi nhận và đồng bộ AI log lên server chấm điểm AI20K
- **Hành động & Kết quả:** Cấu hình scripts/log_antigravity.py và scripts/submit_log.py, cập nhật scripts/_pyrun.sh hỗ trợ .venv, cài đặt hook pre-push và đồng bộ thành công AI log lên server.
- **Tệp liên quan:** `template.py`, `solution/solution.py`, `golden_dataset.json`, `exercises.md`, `reflection.md`
- **Trạng thái:** Hoàn thành & Đã nghiệm thu.
