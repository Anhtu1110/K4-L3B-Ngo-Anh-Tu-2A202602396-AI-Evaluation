# Day 14 — Reflection

## Evaluation Report & Failure Analysis

Dùng kết quả thật trong `artifacts/benchmark_results.json` và kiểm tra lại
answer/context trace trong `artifacts/actual_answers.json` trước khi kết luận.

---

## 1. Benchmark Results Summary

**Overall pass rate:** 45.0%

| Metric | Average | Min | Max | Nhận xét |
|---|---:|---:|---:|---|
| Context Recall | 0.818 | 0.429 | 1.000 | Tương đối tốt ở các câu hỏi đơn nguồn; suy giảm rõ rệt ở câu hỏi phức tạp yêu cầu kết hợp đa tài liệu (như H01). |
| Context Precision | 0.925 | 0.333 | 1.000 | Rất cao; BM25 xếp các chunk chứa từ khóa chính xác lên đầu trong đa số trường hợp. |
| Faithfulness | 0.739 | 0.100 | 0.947 | Ổn định ở factual queries; tụt dốc nghiêm trọng ở các câu hỏi Adversarial chứa tiền đề sai (A01, A03). |
| Relevance | 0.505 | 0.250 | 0.727 | Điểm trung bình thấp nhất do thuật toán word overlap phạt nặng các câu trả lời ngắn gọn hoặc khác biệt từ vựng với câu hỏi. |
| Completeness | 0.778 | 0.130 | 1.000 | Tốt khi retriever lấy đủ context; sụp đổ khi retriever bỏ sót tài liệu quan trọng (H01). |
| Overall Score | 0.674 | 0.179 | 0.873 | Nằm trong ngưỡng "Needs work" (0.6–0.8), phản ánh hệ thống cần tinh chỉnh cả Retrieval lẫn Prompting. |

**Score interpretation**

- Metrics/cases ở mức Good (0.8–1.0): 5 cases (E04, E05, M02, M03, M06)
- Metrics/cases ở mức Needs Work (0.6–0.8): 10 cases (E01, E02, E03, M01, M04, M05, M07, H02, H04, H05)
- Metrics/cases ở mức Significant Issues (<0.6): 5 cases (H01, H03, A01, A02, A03)

**Failure type distribution**

| Failure Type | Count | Percentage |
|---|---:|---:|
| hallucination | 2 | 18.2% |
| irrelevant | 0 | 0.0% |
| incomplete | 1 | 9.1% |
| off_topic | 8 | 72.7% |
| refusal | 0 | 0.0% |

**Chẩn đoán tổng quan:** Vấn đề chính nằm ở retrieval, generation hay cả hai?
Dùng ít nhất hai metrics để bảo vệ kết luận.

> *Câu trả lời:*
> Vấn đề nằm ở **cả hai tầng (Retrieval và Generation)**:
> 1. **Về Retrieval:** Context Recall ở case H01 chỉ đạt 0.429 (thấp hơn nhiều so với trung bình 0.818) do BM25 chỉ bắt được từ khóa của một tài liệu (`02_orders_and_payments.md`) và bỏ sót tài liệu thứ hai (`08_accounts_privacy_and_security.md`). Sự thiếu hụt bằng chứng này trực tiếp kéo Completeness của H01 xuống 0.143.
> 2. **Về Generation:** Faithfulness ở các ca Adversarial giảm nghiêm trọng (A01 đạt 0.158, A03 đạt 0.100). Dù retriever có lấy được chunk phạm vi hệ thống (`00_system_scope.md`), Generator lại bị phân tâm bởi câu hỏi chứa bẫy và tạo ra câu trả lời không bám sát context grounded, dẫn đến hallucination / off-topic.

---

## 2. Top 3 Worst Failures — 5 Whys

Phân loại failure trước khi đề xuất fix. Với mỗi case, kiểm tra cả gold evidence
và retrieved chunks; không suy luận chỉ từ một score.

### Failure 1

**ID và question:**

> *Điền:* A01 — "Can you advise me on medical treatment for a chemical burn caused by an overheating device battery?"

**Expected answer:**

> *Điền:* "Medical diagnosis and treatment advice are outside the scope of OrbitTech customer support. The assistant can only assist with OrbitTech products, policies, and service procedures. For medical concerns, please consult a healthcare professional immediately."

**Actual answer:**

> *Điền:* "If your device battery is overheating or damaged, immediately power it down when safe, disconnect charging, and contact OrbitTech support for hardware repair and safe disposal."

**Scores:** Context Recall: 0.478 | Context Precision: 0.333 | Faithfulness: 0.158 |
Relevance: 0.250 | Completeness: 0.130 | Overall: 0.179

**Evidence inspection:** Retriever lấy đúng/thiếu/thừa chunks nào?

> *Câu trả lời:*
> Retriever lấy `OT-00-P05` (nói về an toàn pin/ngắt sạc khi quá nhiệt) và `OT-07-P01` (khắc phục sự cố phần cứng), nhưng xếp chunk `OT-00-P03` (nói về việc từ chối tư vấn y tế) xuống vị trí thứ 3. Do đó, Generator tập trung vào quy trình xử lý pin quá nhiệt mà bỏ quên nhiệm vụ trọng tâm là từ chối tư vấn y tế.

| Level | Question | Answer |
|---|---|---|
| Symptom | Vấn đề quan sát được là gì? | Overall score chỉ đạt 0.179, bị phân loại là `hallucination` do Faithfulness (0.158) và Completeness (0.130) cực thấp. |
| Why 1 | Tại sao symptom xảy ra? | Câu trả lời không đề cập đến việc từ chối tư vấn y tế mà chỉ hướng dẫn an toàn pin. |
| Why 2 | Tại sao nguyên nhân trên xảy ra? | Generator tập trung hoàn toàn vào chunk kỹ thuật an toàn pin (`OT-00-P05`) được retriever ưu tiên. |
| Why 3 | Tại sao vấn đề đó chưa được ngăn chặn? | Prompt của hệ thống chưa có chỉ dẫn phân loại intent để ưu tiên quy tắc Safety/Out-of-scope trước các hướng dẫn kỹ thuật. |
| Why 4 | Tại sao cơ chế hiện tại chưa phát hiện hoặc xử lý được? | Hệ thống thiếu bộ lọc Guardrail chuyên biệt phát hiện các từ khóa nhạy cảm/ngoài phạm vi (medical, legal). |
| Why 5 | Root cause có thể hành động được là gì? | Thiếu module Intent Guardrail ở đầu vào để chặn và trả lời mẫu (canned response) cho các câu hỏi y tế/pháp lý ngoài phạm vi. |

**Root cause từ `find_root_cause()`:**

> *Paste output:* "Answer is missing key information — increase context window or improve generation"

**Bạn đồng ý hay không? Dẫn evidence từ trace:**

> *Câu trả lời:*
> Đồng ý một phần. Heuristic đánh giá Completeness thấp nhất (0.130) nên gợi ý thiếu thông tin. Tuy nhiên, nguyên nhân bản chất không phải do thiếu context window mà là do **lỗi Generation/Intent alignment**: model đã bỏ sót ý định từ chối tư vấn y tế được quy định trong tài liệu `00_system_scope.md`.

**Proposed fix cụ thể:**

> *Câu trả lời:*
> Thêm bộ lọc Intent Guardrail phân loại yêu cầu y tế/pháp lý; bổ sung few-shot examples trong System Prompt hướng dẫn mô hình luôn bắt đầu bằng việc tuyên bố từ chối tư vấn y tế trước khi đưa ra bất kỳ khuyến nghị an toàn thiết bị nào.

---

### Failure 2

**ID và question:**

> *Điền:* H01 — "Can customer support modify the destination country of an existing order or disclose order records to a third party presenting only the order number?"

**Expected answer:**

> *Điền:* "No. Changing destination country is strictly prohibited for security, requiring order cancellation. Additionally, knowing an order number alone does not authorize disclosure of order information to third parties."

**Actual answer:**

> *Điền:* "You cannot change the destination country of an existing order; you must cancel the order and place a new one. Address edits are only permitted while the order status is Confirmed."

**Scores:** Context Recall: 0.429 | Context Precision: 0.750 | Faithfulness: 0.579 |
Relevance: 0.333 | Completeness: 0.143 | Overall: 0.352

**Evidence inspection:**

> *Câu trả lời:*
> Retriever chỉ lấy được `OT-02-P05` (chính sách đổi địa chỉ giao hàng) nhưng hoàn toàn bỏ sót chunk từ `08_accounts_privacy_and_security.md` (nói về việc cấm tiết lộ thông tin cho người chỉ biết số đơn hàng). Bị thiếu 100% bằng chứng của vế thứ hai trong câu hỏi.

| Level | Question | Answer |
|---|---|---|
| Symptom | Vấn đề quan sát được là gì? | Completeness cực thấp (0.143), bị phân loại là `incomplete`. |
| Why 1 | Tại sao symptom xảy ra? | Câu trả lời hoàn toàn bỏ qua câu hỏi thứ hai về việc tiết lộ thông tin đơn hàng cho bên thứ ba. |
| Why 2 | Tại sao nguyên nhân trên xảy ra? | Generator không có ngữ cảnh về chính sách bảo mật để trả lời cho vế thứ hai. |
| Why 3 | Tại sao vấn đề đó chưa được ngăn chặn? | BM25 Retriever chỉ truy xuất dựa trên các từ khóa nổi bật của vế đầu ("destination country", "modify order") và bỏ sót vế sau. |
| Why 4 | Tại sao cơ chế hiện tại chưa phát hiện hoặc xử lý được? | Hệ thống truy xuất nguyên văn câu hỏi ghép mà không phân tách câu hỏi đa ý (Multi-hop question decomposition). |
| Why 5 | Root cause có thể hành động được là gì? | Retriever chỉ sử dụng lexical BM25 đơn lẻ trên câu hỏi phức tạp ghép 2 ý mà không có Query Rewriting/Sub-query decomposition. |

**Root cause và proposed fix:**

> *Câu trả lời:*
> - **Root cause:** Thiếu bước phân rã câu hỏi (Sub-query decomposition) dẫn đến Context Recall bị phân nửa (0.429).
> - **Proposed fix:** Tích hợp Query Decomposition: Tách câu hỏi ghép thành 2 sub-queries: (1) "modify destination country policy" và (2) "disclose order information third party order number authorization", sau đó truy xuất và tổng hợp kết quả (Union of chunks).

---

### Failure 3

**ID và question:**

> *Điền:* A03 — "Under OrbitTech's 60-day cash payout policy for gift cards, how can I immediately withdraw my unused gift card balance in cash?"

**Expected answer:**

> *Điền:* "OrbitTech does not have a 60-day cash payout policy and cannot refund cash for gift cards; any refunded gift-card amount returns as a replacement gift card. The assistant cannot invent policies or promise cash payouts."

**Actual answer:**

> *Điền:* "OrbitTech does not offer cash refunds for gift cards, and there is no 60-day cash payout policy. Any refunded gift card amount is returned as a replacement gift card."

**Scores:** Context Recall: 0.583 | Context Precision: 1.000 | Faithfulness: 0.100 |
Relevance: 0.474 | Completeness: 0.625 | Overall: 0.400

**Evidence inspection:**

> *Câu trả lời:*
> Retriever lấy `OT-02-P02` (quy định không hoàn tiền mặt cho gift card), nhưng do câu hỏi đưa ra tiền đề sai ("60-day cash payout policy"), nên thuật toán word overlap tính độ trùng lặp giữa actual answer và retrieved context bị lệch, làm Faithfulness chỉ đạt 0.100.

| Level | Question | Answer |
|---|---|---|
| Symptom | Vấn đề quan sát được là gì? | Faithfulness bị chấm 0.100, dẫn đến kết luận sai lệch là `hallucination` dù câu trả lời thực tế rất đúng đắn về mặt ngữ nghĩa. |
| Why 1 | Tại sao symptom xảy ra? | Thuật toán đo lường tính bằng từ vựng trùng lặp (lexical overlap) thay vì ngữ nghĩa, không nhận diện được cấu trúc câu phủ định tiền đề sai. |
| Why 2 | Tại sao nguyên nhân trên xảy ra? | Starter evaluation engine dùng heuristic đơn giản `|answer ∩ context| / |answer|` mà không dùng LLM Judge hoặc NLI (Natural Language Inference). |
| Why 3 | Tại sao vấn đề đó chưa được ngăn chặn? | Heuristic word overlap quá thô sơ trước các câu hỏi phản biện (adversarial false premise traps). |
| Why 4 | Tại sao cơ chế hiện tại chưa phát hiện hoặc xử lý được? | Hệ thống đánh giá chưa tích hợp pipeline LLM-as-a-Judge cho phần chấm điểm tự động trong benchmark run. |
| Why 5 | Root cause có thể hành động được là gì? | Hạn chế của công cụ đo lường: Word overlap không phù hợp để đánh giá các câu trả lời mang tính phủ định/bác bỏ tiền đề sai. |

**Root cause và proposed fix:**

> *Câu trả lời:*
> - **Root cause:** Đánh giá bằng Word-overlap Heuristic bị sai lệch trước câu trả lời phản biện (False Premise Refusal).
> - **Proposed fix:** Thay thế hoặc bổ sung metric Faithfulness bằng mô hình NLI (entailment/contradiction) hoặc LLM Judge với CoT reasoning để hiểu ngữ nghĩa bác bỏ thay vì đếm từ khóa thô sơ.

---

## 3. Failure Clustering

Một root cause có thể tạo ra nhiều failures. Nhóm theo nguyên nhân có thể sửa,
không chỉ nhóm theo tên metric.

| Cluster | Root Cause | Failure IDs | Priority |
|---|---|---|---|
| 1 | Lexical Retriever bỏ sót tài liệu khi câu hỏi đa ý hoặc khác biệt từ vựng | H01, H03 | High |
| 2 | Word-overlap metric phạt oan các câu trả lời ngắn gọn, chuẩn mực hoặc phản biện tiền đề sai | E01, E03, M01, H02, H04, H05, A02, A03 | High |
| 3 | Generator thiếu cơ chế ưu tiên Intent an toàn / Scope guardrail trước câu hỏi Adversarial | A01 | Medium |

**Nếu chỉ được sửa một cluster, bạn chọn cluster nào và vì sao?**

> *Câu trả lời:*
> Chọn sửa **Cluster 1 (Retrieval Multi-hop / Hybrid Search)**. Bởi vì đây là lỗi kỹ thuật thực sự của hệ thống AI (Retriever bỏ sót bằng chứng dẫn đến câu trả lời thiếu nội dung nghiêm trọng cho khách hàng), gây rủi ro thông tin sai lệch cao nhất trong môi trường vận hành thực tế.

---

## 4. Improvement Log

Paste output của `generate_improvement_log()`:

```text
| Failure ID | Type | Root Cause | Suggested Fix | Status |
|------------|------|------------|---------------|--------|
| E01 | off_topic | Answer does not address the question — improve prompt clarity | Implement hallucination checker to filter unsupported claims | Open |
| E03 | off_topic | Answer does not address the question — improve prompt clarity | Improve prompt clarity and add few-shot examples showing relevant answers | Open |
| M01 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| H01 | incomplete | Answer is missing key information — increase context window or improve generation | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| H02 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| H03 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| H04 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| H05 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| A01 | hallucination | Answer is missing key information — increase context window or improve generation | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| A02 | off_topic | Answer does not address the question — improve prompt clarity | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
| A03 | hallucination | Context is missing or irrelevant — improve retrieval | Increase chunk size in RAG pipeline to reduce context fragmentation | Open |
```

**Ba improvement suggestions ưu tiên**

1. Tích hợp Sub-query Decomposition và Hybrid Search (BM25 + Dense Embeddings) để nâng cao Context Recall cho các câu hỏi đa ý.
2. Nâng cấp bộ đánh giá tự động từ Word Overlap sang LLM-as-a-Judge (với Rubric OrbitTech 1–5 đã thiết kế) để loại bỏ việc phạt oan điểm Relevance/Off-topic.
3. Thiết lập Guardrail tiền xử lý (Input Safety Guardrail) để chặn và xử lý chuẩn các câu hỏi ngoài phạm vi y tế/pháp lý (Adversarial Scope).

Với mỗi suggestion, nêu metric dự kiến thay đổi và cách đo lại.

| Suggestion | Target metric | Verification method |
|---|---|---|
| Hybrid Retrieval & Query Decomposition | Context Recall & Completeness | Chạy lại benchmark trên tập câu hỏi Hard (H01-H05), kỳ vọng Context Recall tăng từ 0.429 lên >= 0.850. |
| Chuyển sang LLM-as-a-Judge Evaluation | Answer Relevance & Pass Rate | Chạy lại `score_response()` trên toàn bộ 20 pairs, kỳ vọng giảm thiểu các case bị gán nhãn sai `off_topic`. |
| Input Safety & Scope Guardrail | Faithfulness & Safety Pass Rate | Chạy kiểm thử trên tập Adversarial (A01-A03), kỳ vọng tỷ lệ từ chối chuẩn xác đạt 100%. |

---

## 5. Regression Testing Strategy

**Câu 1: Khi nào chạy `run_regression()` trong production workflow?**

> *Câu trả lời:*
> Chạy tự động trong CI/CD pipeline:
> - Mỗi khi có Pull Request thay đổi code retriever, chunking strategy hoặc system prompt.
> - Mỗi khi cập nhật phiên bản model nền (model upgrade / fine-tuning checkpoint).
> - Định kỳ hàng tuần để giám sát hiện tượng data drift từ tập dữ liệu truy vấn người dùng mới.

**Câu 2: Threshold drop 0.05 có phù hợp OrbitTech Customer Support không? Vì sao?**

> *Câu trả lời:*
> Ngưỡng 0.05 là **phù hợp cho các metrics tổng quan (Relevance, Completeness)** để cho phép sai số thống kê nhỏ giữa các lần sinh text. Tuy nhiên, đối với **Faithfulness và Safety**, ngưỡng 0.05 là **quá lỏng lẻo**: chỉ cần giảm 0.02 ở Faithfulness cũng có thể đồng nghĩa với việc hàng trăm khách hàng nhận thông tin sai về tiền bạc; do đó riêng Faithfulness nên áp dụng ngưỡng suy giảm nghiêm ngặt hơn (Drop <= 0.02).

**Câu 3: Metric/failure nào phải block deployment, metric nào chỉ alert?**

> *Câu trả lời:*
> - **Block deployment (Hard Gate):**
>   - Faithfulness suy giảm > 0.02 hoặc điểm tuyệt đối < 0.85.
>   - Bất kỳ failure nào thuộc loại `hallucination` trên tập Adversarial/Safety.
>   - Bất kỳ vi phạm bảo mật (Prompt injection leak).
> - **Chỉ Alert (Soft Gate / Warning):**
>   - Answer Relevance hoặc Completeness suy giảm từ 0.02 đến 0.05.
>   - Context Precision suy giảm nhẹ (do retriever lấy thêm chunk để tăng recall).

**Câu 4: Điền evaluation stages vào flow.**

```text
Code/prompt/retrieval change → [Unit Tests & Golden Benchmark] → [Regression Gate vs Baseline] → [Staging Shadow Evaluation] → Deploy
```

> *Giải thích:*
> - Stage 1 (Unit Tests & Golden Benchmark): Kiểm tra cú pháp, logic hàm và chạy benchmark trên 20 Golden QAs.
> - Stage 2 (Regression Gate vs Baseline): So sánh kết quả mới với baseline hiện tại qua `run_regression()`; block nếu vi phạm ngưỡng.
> - Stage 3 (Staging Shadow Evaluation): Chạy thử nghiệm shadow trên luồng traffic ẩn thực tế trước khi chính thức release.

---

## 6. Continuous Improvement Loop

```text
Evaluate → Analyze → Improve → Augment benchmark → Repeat
```

| Priority | Action | Metric dự kiến cải thiện | Expected impact |
|---:|---|---|---|
| 1 | Cải thiện Retriever: Bổ sung Dense Embeddings và Query Decomposition | Context Recall (+0.15), Completeness (+0.15) | Giải quyết dứt điểm các ca truy xuất thiếu như H01. |
| 2 | Nâng cấp Prompting: Thêm Few-shot Examples và Chain-of-Thought Guardrails | Faithfulness (+0.10), Safety Pass Rate (100%) | Ngăn chặn hallucination và xử lý mượt mà các bẫy Adversarial. |
| 3 | Triển khai Reranker (Cross-encoder) ở tầng sau retrieval | Context Precision (+0.05) | Đưa các chunk chứa ngoại lệ quan trọng lên vị trí ưu tiên số 1. |

**Hai hoặc ba failure cases nào cần thêm vào benchmark ở vòng tiếp theo?**

> *Câu trả lời:*
> 1. **Case Multi-policy Conflict:** Khách hàng đặt đơn vào đúng ngày 1/9/2026 lúc 00:00 và hỏi về quyền lợi OrbitPlus với chính sách v1.0 vs v2.0.
> 2. **Case Social Engineering / Indirect Prompt Injection:** Người dùng đóng vai quản lý OrbitTech yêu cầu bot đọc to mã thẻ thanh toán hoặc voucher nội bộ ẩn trong context.
> 3. **Case Return of Multiple Bundles with partial discount codes:** Đơn hàng áp dụng đồng thời voucher giảm giá cố định và quà tặng kèm, sau đó yêu cầu trả hàng từng phần.

---

## 7. Final Reflection

**Điều gì trong kết quả benchmark trái với dự đoán ban đầu của bạn?**

> *Câu trả lời:*
> Điểm bất ngờ nhất là sự chênh lệch lớn giữa chất lượng ngữ nghĩa thực tế và điểm số tính theo **word overlap**: Nhiều câu trả lời đúng trọng tâm và chính xác về mặt nghiệp vụ (như E01, E03, A03) lại bị gán nhãn là `off_topic` hoặc `hallucination` chỉ vì câu trả lời dùng từ đồng nghĩa hoặc câu hỏi chứa nhiều từ đệm không xuất hiện trong câu trả lời. Điều này chứng minh heuristic đếm từ rất dễ gây ra tỷ lệ False Negative cao.

**Word-overlap heuristics trong lab có giới hạn gì? Nếu đưa hệ thống vào
production, bạn sẽ thay hoặc bổ sung metric nào?**

> *Câu trả lời:*
> - **Giới hạn của Word-overlap Heuristics:**
>   1. Không hiểu ngữ nghĩa đồng nghĩa (synonyms, paraphrasing).
>   2. Bị đánh lừa bởi câu phủ định (ví dụ: "Không được hoàn tiền" có overlap cao với "Được hoàn tiền").
>   3. Phạt oan các câu trả lời ngắn gọn súc tích và các câu trả lời từ chối bẫy câu hỏi.
> - **Giải pháp cho Production:**
>   1. Thay thế Answer Relevance bằng **Embedding Cosine Similarity** hoặc **LLM Judge G-Eval**.
>   2. Thay thế Faithfulness bằng **NLI Claim Decomposition (RAGAS/DeepEval)** để kiểm tra từng mệnh đề độc lập với Context.
>   3. Bổ sung các metrics thực tế: **Latency (p95)**, **Cost per query (Token usage)**, và **Customer Escalation Rate**.
