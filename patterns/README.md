# 🏛️ CÁC MẪU THIẾT KẾ HỆ THỐNG AI THỰC CHIẾN (AI ENGINEERING DESIGN PATTERNS)

> Tuyển tập các mẫu thiết kế kiến trúc (Architecture & Design Patterns) đã được kiểm chứng trong môi trường sản xuất (Production-Grade) dành cho Kỹ sư AI Ứng Dụng.

---

## 🧭 Bảng Tổng Hợp 6 Mẫu Thiết Kế Trọng Tâm

| STT | Mẫu Thiết Kế (Pattern) | Vấn Đề Giải Quyết | Công Nghệ Cốt Lõi | Mã Nguồn Mẫu |
| :---: | :--- | :--- | :--- | :---: |
| **01** | [**Structured Outputs & Self-Healing JSON**](01_structured_output_and_self_healing/) | LLM trả lời tùy ý, vỡ schema khi tích hợp backend microservices. | Pydantic V2, AST Parser, Zero-latency Regex Healing | [Xem Code](01_structured_output_and_self_healing/) |
| **02** | [**Hybrid Search & Reciprocal Rank Fusion (RRF)**](02_hybrid_search_and_reranking_rrf/) | Vector Search thuần túy bị trượt từ khóa chính xác (mã lỗi, serial, acronyms). | BM25 Okapi, Cosine Distance, RRF ($k=60$) | [Xem Code](02_hybrid_search_and_reranking_rrf/) |
| **03** | [**Agentic ReAct & Dynamic Routing**](03_agentic_react_and_routing/) | Mô hình không thể truy xuất API động, dễ lặp vô tận khi gọi công cụ. | ReAct Loop, Scratchpad Reasoning, Tool Sandboxing | [Xem Code](03_agentic_react_and_routing/) |
| **04** | [**Human-in-the-Loop & Breakpoints**](04_human_in_the_loop_guardrails/) | Rủi ro thất thoát tài chính hoặc rò rỉ dữ liệu khi AI tự hành ra quyết định lớn. | `state.interrupt()`, Approval Gates, Audit Trail | [Xem Code](04_human_in_the_loop_guardrails/) |
| **05** | [**Semantic Caching & FinOps Latency Waterfall**](05_semantic_caching_and_finops/) | Độ trễ gọi LLM cao (~1s), lãng phí chi phí token khi người dùng hỏi các câu tương đồng. | Vector Cosine Threshold, TTL Eviction, FinOps Tracker | [Xem Code](05_semantic_caching_and_finops/) |
| **06** | [**AI Security Guardrails & Injection Defense**](06_ai_firewall_and_injection_defense/) | Bị tấn công Jailbreak (DAN), Prompt Injection, đánh cắp Canary Token, lộ PII. | Canary Trap, PII Redaction, Layered Defense Firewall | [Xem Code](06_ai_firewall_and_injection_defense/) |

---

## 🎯 Nguyên Tắc Thiết Kế (Design Philosophy)

1. **Type-Safety Tuyệt Đối**: Mọi dữ liệu ra vào các hệ thống AI đều phải được định kiểu tường minh với Pydantic V2.
2. **Defensive Programming**: Không tin tưởng 100% vào đầu ra của mô hình; luôn có bộ lọc deterministic (Regex, AST parser, Rule-based checks) trước khi chuyển tiếp payload.
3. **Độc Lập Phụ Thuộc (Zero-Friction Local Testing)**: Toàn bộ code mẫu được viết thuần Python (hoặc sử dụng thư viện chuẩn), chạy được ngay cả khi không có kết nối internet hoặc API Key trả phí thông qua Mocking Engines.
4. **CI/CD Verifiable**: Tất cả các pattern đều đi kèm bộ kiểm thử tự động `pytest` với độ bao phủ cao.
