# 🚀 CẨM NANG KỸ SƯ AI THỰC CHIẾN (APPLIED AI ENGINEERING HANDBOOK)
### Nền Tảng Học Tập & Tham Chiếu Dự Án AI Ứng Dụng Hàng Đầu

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=TontonYuta/Applied-AI-Engineering-Handbook)
[![Colab Lab 1: Hybrid RAG](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TontonYuta/Applied-AI-Engineering-Handbook/blob/main/notebooks/01_interactive_rag_cookbook.ipynb)
[![Colab Lab 2: ReAct HITL](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TontonYuta/Applied-AI-Engineering-Handbook/blob/main/notebooks/02_agentic_langgraph_hitl.ipynb)
[![Colab Lab 3: Cache & Firewall](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TontonYuta/Applied-AI-Engineering-Handbook/blob/main/notebooks/03_semantic_cache_and_guardrails.ipynb)
[![Colab Lab 4: Self-Healing JSON](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TontonYuta/Applied-AI-Engineering-Handbook/blob/main/notebooks/04_self_healing_structured_outputs.ipynb)
[![CI Evals](https://img.shields.io/badge/CI%20Evals-20%2F20%20Passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()

> **Chào mừng bạn đến với Cẩm Nang Kỹ Sư AI Thực Chiến!**  
> Kho lưu trữ này được thiết kế để bạn có thể **học tập, chạy thử code và thực hành trực tiếp 100% ngay trên GitHub hoặc Google Colab mà không cần cài đặt bất kỳ phần mềm nào trên máy tính cá nhân**.

---

## 🎓 AI ENG ACADEMY — HỌC TỪ NHỎ ĐẾN LỚN + QUIZ TƯƠNG TÁC (SIÊU CLEAN)

> **"AI Eng Academy"** là phiên bản cải tiến tối thượng, loại bỏ hoàn toàn các nút bấm phức tạp. Người học được dẫn dắt theo **lộ trình 8 bài học nguyên tử từ số 0**, kiến thức nâng dần lên để không bị ngợp, đi kèm **thử thách trắc nghiệm (Interactive Quiz) phản hồi thời gian thực**.

```mermaid
flowchart LR
    L1["Bài 1: Token là gì?"] --> L2["Bài 2: Embedding & Vector"]
    L2 --> L3["Bài 3: Chunking & Overlap"]
    L3 --> L4["Bài 4: RAG Cơ Chế"]
    L4 --> L5["Bài 5: ReAct Agent"]
    L5 --> L6["Bài 6: Human-in-the-Loop"]
    L6 --> L7["Bài 7: AI Security & Guardrails"]
    L7 --> L8["Bài 8: Self-Healing JSON"]
```

### 1. Trải nghiệm học tối giản (Zero Cognitive Load)
* **Giao diện tập trung tuyệt đối**: Chỉ có 1 thẻ bài học cô đọng + 1 minh họa trực quan 60fps + 1 thẻ Quiz 4 lựa chọn (A, B, C, D).
* **Phản hồi tức thì**: Chọn đúng hiện thẻ xanh lá `CHÍNH XÁC! (+1 ⭐ KỸ NĂNG THỰC CHIẾN)` kèm lời giải thích tại sao đúng trong thực tế sản xuất.

| Bài 1: Tokenizer Trực Quan + Quiz Câu Hỏi | Bài 1: Phản Hồi Xanh Lá Khi Chọn Đúng |
| :---: | :---: |
| ![Lesson 1 Question](docs/images/lesson_01_token_question.png) | ![Lesson 1 Answered](docs/images/lesson_01_token_answered.png) |

| Bài 2: Embedding 2D & Khoảng Cách Cosine | Bài 3: Chunking & Vùng Gối Đầu Overlap |
| :---: | :---: |
| ![Lesson 2 Embedding](docs/images/lesson_02_embedding.png) | ![Lesson 3 Chunking](docs/images/lesson_03_chunking.png) |

| Bài 4: Quy Trình RAG 3 Bước | Bài 5: Chu Trình ReAct Agent |
| :---: | :---: |
| ![Lesson 4 RAG](docs/images/lesson_04_rag.png) | ![Lesson 5 Agent](docs/images/lesson_05_agent.png) |

| Bài 6: Breakpoint Phê Duyệt An Toàn | Bài 7: AI Firewall & Canary Token |
| :---: | :---: |
| ![Lesson 6 HITL](docs/images/lesson_06_hitl.png) | ![Lesson 7 Security](docs/images/lesson_07_security.png) |

| Bài 8: Tự Vá Lỗi AST JSON trong 0.4ms | Bài 8: Hoàn Tất Khóa Học & Điểm Thưởng |
| :---: | :---: |
| ![Lesson 8 JSON](docs/images/lesson_08_json.png) | ![Lesson 8 Answered](docs/images/lesson_08_answered.png) |

---

## 🎨 PHÒNG LAB TỔNG HỢP VÀ THỰC HÀNH CHUYÊN SÂU (ADVANCED LABS)

### 1. 🔍 RAG & 2D Vector Space Explorer + RRF Fusion
* **Slider Chunk Size (50-500) & Overlap (0-100)**: Chia đoạn tài liệu trực tiếp, tô màu phân đoạn và làm nổi bật overlap gối đầu.
* **Canvas 2D Scatter Plot 60fps**: Chiếu không gian nhúng vector, bắn tia đo Cosine Similarity từ Query Point tới Top-K chunks gần nhất.
* **Reciprocal Rank Fusion (RRF)**: Dung hợp đa tầng Sparse BM25 + Dense Vector Embeddings với công thức $RRF(d) = \sum \frac{1}{k + rank_i}$ ($k=60$).

![RAG 2D Canvas](docs/images/01_rag_vector_2d.png)
![RRF Hybrid Search](docs/images/01_rag_rrf_fusion.png)

---

### 2. 🕸️ LangGraph Agentic Flowchart Simulator + Cổng Human-In-The-Loop
* **StateGraph Canvas**: Mô phỏng trực quan luồng xử lý `Customer Request -> Planner -> SQL Sandbox -> Human Gate -> Disbursement`.
* **Data Orb Animation**: Gói dữ liệu chuyển động phát sáng mượt mà dọc theo các nhánh có điều kiện.
* **Breakpoint An Toàn `state.interrupt()`**: Với các giao dịch vượt ngưỡng (ví dụ: hoàn 25.000.000 VNĐ > 5.000.000 VNĐ), hệ thống tự động ngắt và kích hoạt popup phê duyệt của Quản lý trước khi giải ngân.

![LangGraph HITL Breakpoint](docs/images/02_langgraph_hitl_breakpoint.png)
![LangGraph Completed Path](docs/images/02_langgraph_completed.png)

---

### 3. ⚡ Semantic Cache & FinOps Latency Waterfall
* **Ngưỡng tương đồng $\tau$ (0.70 - 0.98)**: Phân biệt Paraphrase Query để quyết định Cache Hit vs Cache Miss.
* **Waterfall Latency Benchmark**: Trực quan hóa độ trễ $880\text{ ms}$ (LLM Cloud Roundtrip) so với $14\text{ ms}$ (Redis Vector Cache Hit) — **nhanh hơn 98.4%**.
* **Đồng hồ đo FinOps**: Tính toán chi phí tiết kiệm trực tiếp theo bảng giá GPT-4o, Claude 3.5 Sonnet và Gemini Flash.

![Semantic Cache](docs/images/03_semantic_cache_cost.png)

---

### 4. 🛡️ AI Security Guardrails & Injection Firewall Sandbox
* **Red Team Presets**: Nạp sẵn các mẫu tấn công: DAN Jailbreak v9.2, Prompt Leak & Canary Extraction, PII Exfiltration, Indirect Markdown Injection.
* **Tường lửa 4 tầng**: Heuristic Regex, Secret Canary Token Trap, PII Masking & Redactor, Jailbreak Classifier.
* **Token Risk Inspector**: Đánh dấu trực quan các token nguy hiểm trong câu lệnh và chặn trả lời (HTTP 403 Forbidden).

![AI Security Firewall](docs/images/04_ai_security_firewall.png)

---

### 5. 🧩 Self-Healing JSON AST Engine
* **Phục hồi AST trong $0.4\text{ ms}$**: Tự động vá các lỗi phổ biến của LLM mà không cần tốn chi phí và thời gian gọi lại model ($1,850\text{ ms}$):
  1. Loại bỏ Markdown fences (````json```) và văn bản đàm thoại thừa.
  2. Chuẩn hóa Python Literals (`True`/`False`/`None` sang `true`/`false`/`null`).
  3. Xóa trailing commas thừa trước dấu đóng `}` hoặc `]`.
  4. Bổ sung ngoặc kép cho Object Keys chưa có ngoặc.
  5. Cân bằng ngoặc đóng bị đứt nửa chừng do token limit.

![Self-Healing JSON Lab](docs/images/05_self_healing_json.png)

---

## 🏛️ 6 MẪU THIẾT KẾ HỆ THỐNG AI THỰC CHIẾN (CANONICAL DESIGN PATTERNS)

> Toàn bộ các mẫu thiết kế đều đi kèm mã nguồn Python chuẩn mực, độc lập phụ thuộc và có **100% bộ kiểm thử tự động `pytest`** xác minh trong CI/CD. Chi tiết xem tại thư mục [`patterns/`](patterns/):

| STT | Mẫu Thiết Kế (Pattern) | Vấn Đề Giải Quyết | Công Nghệ Cốt Lõi | Mã Nguồn Mẫu |
| :---: | :--- | :--- | :--- | :---: |
| **01** | [**Structured Outputs & Self-Healing JSON**](patterns/01_structured_output_and_self_healing/) | LLM trả lời tùy ý, vỡ schema khi tích hợp backend microservices. | Pydantic V2, AST Parser, Zero-latency Regex Healing | [Xem Code](patterns/01_structured_output_and_self_healing/) |
| **02** | [**Hybrid Search & Reciprocal Rank Fusion (RRF)**](patterns/02_hybrid_search_and_reranking_rrf/) | Vector Search thuần túy bị trượt từ khóa chính xác (mã lỗi, serial, acronyms). | BM25 Okapi, Cosine Distance, RRF ($k=60$) | [Xem Code](patterns/02_hybrid_search_and_reranking_rrf/) |
| **03** | [**Agentic ReAct & Dynamic Routing**](patterns/03_agentic_react_and_routing/) | Mô hình không thể truy xuất API động, dễ lặp vô tận khi gọi công cụ. | ReAct Loop, Scratchpad Reasoning, Tool Sandboxing | [Xem Code](patterns/03_agentic_react_and_routing/) |
| **04** | [**Human-in-the-Loop & Breakpoints**](patterns/04_human_in_the_loop_guardrails/) | Rủi ro thất thoát tài chính hoặc rò rỉ dữ liệu khi AI tự hành ra quyết định lớn. | `state.interrupt()`, Approval Gates, Audit Trail | [Xem Code](patterns/04_human_in_the_loop_guardrails/) |
| **05** | [**Semantic Caching & FinOps Latency Waterfall**](patterns/05_semantic_caching_and_finops/) | Độ trễ gọi LLM cao (~1s), lãng phí chi phí token khi người dùng hỏi các câu tương đồng. | Vector Cosine Threshold, TTL Eviction, FinOps Tracker | [Xem Code](patterns/05_semantic_caching_and_finops/) |
| **06** | [**AI Security Guardrails & Injection Defense**](patterns/06_ai_firewall_and_injection_defense/) | Bị tấn công Jailbreak (DAN), Prompt Injection, đánh cắp Canary Token, lộ PII. | Canary Trap, PII Redaction, Layered Defense Firewall | [Xem Code](patterns/06_ai_firewall_and_injection_defense/) |

---

## 💻 4 CÁCH HỌC & TRẢI NGHIỆM TRỰC TIẾP (KHÔNG CẦN CÀI ĐẶT MÁY TÍNH)

```mermaid
flowchart LR
    A["Kho Tri Thức GitHub"] --> B["Cách 1: GitHub Codespaces<br/>(1-Click mở full VS Code + Linux trên Web)"]
    A --> C["Cách 2: Google Colab Badges<br/>(1-Click mở 4 Jupyter Notebooks có GPU)"]
    A --> D["Cách 3: AI Eng Studio Web App<br/>(Mở studio-app/index.html tương tác 60fps)"]
    A --> E["Cách 4: Đọc Web / Mobile<br/>(Markdown chuẩn mực + Sơ đồ Mermaid)"]
```

### 1. Cách 1: Chạy toàn bộ kho code bằng GitHub Codespaces (Khuyên dùng)
* Nhấn vào nút: [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=TontonYuta/Applied-AI-Engineering-Handbook)
* GitHub sẽ tự động tạo một máy ảo Linux đám mây với **VS Code trên trình duyệt**, đã cài sẵn Python 3.11, Jupyter Notebooks và toàn bộ thư viện trong `requirements.txt` qua cấu hình [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json).
* Miễn phí **60 giờ sử dụng mỗi tháng** cho mọi tài khoản GitHub.

### 2. Cách 2: Thực hành 4 bài lab trên Google Colab
* Mở thư mục [`notebooks/`](notebooks/) và nhấn vào nút **Open In Colab** ở đầu mỗi notebook để chạy code tương tác và thử nghiệm miễn phí với GPU của Google:
  - [`01_interactive_rag_cookbook.ipynb`](notebooks/01_interactive_rag_cookbook.ipynb): BM25 + Vector Search + RRF Fusion.
  - [`02_agentic_langgraph_hitl.ipynb`](notebooks/02_agentic_langgraph_hitl.ipynb): ReAct Loop & Breakpoint Cổng Quản Lý Duyệt.
  - [`03_semantic_cache_and_guardrails.ipynb`](notebooks/03_semantic_cache_and_guardrails.ipynb): Semantic Cache FinOps & Tường Lửa Canary Token.
  - [`04_self_healing_structured_outputs.ipynb`](notebooks/04_self_healing_structured_outputs.ipynb): Pydantic V2 & Tự Vá Lỗi AST JSON trong 0.4ms.

### 3. Cách 3: Chạy AI Eng Studio Web App trực tiếp trên trình duyệt
* Mở file [`studio-app/index.html`](studio-app/index.html) bằng bất kỳ trình duyệt nào (hoặc chạy lệnh `python3 -m http.server 8000` trong terminal) để trải nghiệm giao diện trực quan 60fps đầy đủ cả 2 chế độ:
  - **AI Eng Academy**: 8 bài học tuần tự từ số 0 kèm bộ Quiz trắc nghiệm tương tác chấm điểm thời gian thực.
  - **Advanced Labs**: 5 phòng lab mô phỏng đồ thị LangGraph, không gian vector 2D, thác nước độ trễ Semantic Cache, và Red Team Firewall.

### 4. Cách 4: Đọc trực tiếp trên ứng dụng GitHub (Web & Mobile)
* Toàn bộ tài liệu được viết theo chuẩn GitHub Flavored Markdown với sơ đồ luồng dữ liệu Mermaid trực quan, công thức toán học và bảng biểu so sánh rõ ràng.

---

## 📑 BỘ 12 PAPERS KINH ĐIỂN CỦA KỸ SƯ AI THỰC CHIẾN

*Chi tiết phân tích kiến trúc và bài học thực tế xem tại thư mục [`papers/`](papers/):*

| Nhóm Chuyên Đề | Tên Paper | Tác Giả & Tổ Chức | Giá Trị Thực Chiến Cốt Lõi | Chi Tiết |
| :--- | :--- | :--- | :--- | :---: |
| **RAG Nâng Cao** | **RAG** | Patrick Lewis et al. *(Meta AI)* | Khai sinh kiến trúc RAG; LLM là Reasoning Engine, Vector DB là Hard Drive. | [Xem](papers/01_rag_retrieval_papers.md#1-rag) |
| | **Self-RAG** | Akari Asai et al. *(UW / AI2)* | Token tự phản biện (`[Retrieve]`, `[IsRel]`, `[IsSup]`) chống ảo giác. | [Xem](papers/01_rag_retrieval_papers.md#2-self-rag) |
| | **CRAG** | Shi-Qi Yan et al. *(2024)* | Cơ chế tự sửa sai; fallback sang Web Search khi Vector DB không khớp. | [Xem](papers/01_rag_retrieval_papers.md#3-corrective-rag-crag) |
| | **ColBERT / ColPali** | Khattab et al. / Faysse et al. | Late Interaction (MaxSim); tìm kiếm PDF/bảng biểu thị giác không cần OCR. | [Xem](papers/01_rag_retrieval_papers.md#4-colbert--colpali) |
| | **GraphRAG** | Darren Edge et al. *(Microsoft)* | Gom cụm cộng đồng Leiden; trả lời câu hỏi tổng hợp vĩ mô toàn tập dữ liệu. | [Xem](papers/01_rag_retrieval_papers.md#5-graphrag) |
| **Agents & Tools** | **ReAct** | Shunyu Yao et al. *(Princeton / Google)* | Công thức vàng: `Thought -> Action -> Observation`. | [Xem](papers/02_agentic_workflows_papers.md#1-react) |
| | **Reflexion** | Noah Shinn et al. *(MIT / Northeastern)* | Vòng lặp rút kinh nghiệm bằng ngôn ngữ (Verbal RL) khi gặp lỗi. | [Xem](papers/02_agentic_workflows_papers.md#2-reflexion) |
| | **Toolformer** | Timo Schick et al. *(Meta AI)* | Cơ chế mô hình tự quyết định thời điểm và tham số gọi API ngoại vi. | [Xem](papers/02_agentic_workflows_papers.md#3-toolformer) |
| | **Effective Agents** | Erik Schluntz *(Anthropic, Dec 2024)* | 5 mẫu thiết kế quy trình: Chaining, Routing, Parallel, Orchestrator, Optimizer. | [Xem](papers/02_agentic_workflows_papers.md#4-anthropic-agents) |
| **Evals & Serving**| **LLM-as-a-Judge** | Lianmin Zheng et al. *(LMSYS / Berkeley)* | Đánh giá tự động; khắc phục 4 thiên kiến (Position, Verbosity, Self-bias). | [Xem](papers/03_evals_and_serving_papers.md#1-llm-as-a-judge) |
| | **LoRA & QLoRA** | Edward Hu / Tim Dettmers | Đóng băng trọng số gốc, tinh chỉnh ma trận phân rã $B \cdot A$ trên 4-bit NF4. | [Xem](papers/03_evals_and_serving_papers.md#2-lora--qlora) |
| | **vLLM PagedAttention**| Woosuk Kwon et al. *(UC Berkeley)* | Phân trang bộ nhớ ảo KV Cache, tăng thông lượng serving lên $24\times$. | [Xem](papers/03_evals_and_serving_papers.md#3-vllm-pagedattention) |

---

## 🛠️ TOP 15 GITHUB REPOSITORIES THỰC CHIẾN HÀNG ĐẦU THẾ GIỚI

### 1. Tuyển tập Thực hành & Cookbooks
* [**NirDiamant/RAG_Techniques**](https://github.com/NirDiamant/RAG_Techniques) — Kho mẫu RAG thực chiến số 1: Chunking, Hybrid, Reranking, CRAG.
* [**NirDiamant/GenAI_Agents**](https://github.com/NirDiamant/GenAI_Agents) — Tuyển tập hàng chục notebook triển khai các mẫu thiết kế Agent.
* [**anthropics/anthropic-cookbook**](https://github.com/anthropics/anthropic-cookbook) — Code mẫu chính thức từ Anthropic (Tool calling, Caching, Vision).
* [**openai/openai-cookbook**](https://github.com/openai/openai-cookbook) — Cẩm nang doanh nghiệp từ OpenAI (Structured Outputs, Evals).
* [**meta-llama/llama-cookbook**](https://github.com/meta-llama/llama-cookbook) — Cẩm nang tối ưu và chạy mô hình mã nguồn mở Llama.

### 2. Giao thức Mở & Khung Tác Tử (Agents & Protocols)
* [**modelcontextprotocol/servers**](https://github.com/modelcontextprotocol/servers) — Chuẩn mở MCP: Kết nối AI với Postgres, SQLite, Slack, Git.
* [**langchain-ai/langgraph**](https://github.com/langchain-ai/langgraph) — Nền tảng điều phối Agent có trạng thái và điểm ngắt Human-in-the-loop.
* [**pydantic/pydantic-ai**](https://github.com/pydantic/pydantic-ai) — Khung Agent hiện đại, hướng type-safe từ đội ngũ Pydantic.
* [**jxnl/instructor**](https://github.com/jxnl/instructor) — Chuẩn hóa trích xuất dữ liệu có cấu trúc với Pydantic V2.

### 3. Đánh giá Tự động (Evals) & Giám sát (LLMOps)
* [**confident-ai/deepeval**](https://github.com/confident-ai/deepeval) — Bộ kiểm thử Unit Test cho LLM trong CI/CD.
* [**explodinggradients/ragas**](https://github.com/explodinggradients/ragas) — Khung đo lường độ trung thực (Faithfulness) và độ liên quan của RAG.
* [**langfuse/langfuse**](https://github.com/langfuse/langfuse) — Nền tảng mã nguồn mở số 1 về Tracing, Token, Latency và Cost tracking.
* [**Arize-ai/phoenix**](https://github.com/Arize-ai/phoenix) — AI Observability và trực quan hóa trace phân tán.

### 4. Cụm Phục Vụ & Fine-Tuning
* [**vllm-project/vllm**](https://github.com/vllm-project/vllm) — Cụm serving suy luận tốc độ cao nhất hiện nay.
* [**unslothai/unsloth**](https://github.com/unslothai/unsloth) — Huấn luyện LoRA/QLoRA siêu tốc, tiết kiệm 80% VRAM GPU.

---

## 🧭 CẤU TRÚC THƯ MỤC KHO LƯU TRỮ

```text
Applied-AI-Engineering-Handbook/
├── .devcontainer/                  # Cấu hình 1-Click mở trên GitHub Codespaces
│   └── devcontainer.json
├── .github/workflows/              # Tự động hóa CI/CD Evals (20/20 Passing Tests)
│   └── ci.yml
├── patterns/                       # 6 Mẫu Thiết Kế Hệ Thống AI Thực Chiến
│   ├── README.md                   # Tổng hợp kiến trúc & hướng dẫn sử dụng
│   ├── 01_structured_output_and_self_healing/
│   ├── 02_hybrid_search_and_reranking_rrf/
│   ├── 03_agentic_react_and_routing/
│   ├── 04_human_in_the_loop_guardrails/
│   ├── 05_semantic_caching_and_finops/
│   └── 06_ai_firewall_and_injection_defense/
├── notebooks/                      # 4 Bài Lab tương tác chạy trên Google Colab
│   ├── 01_interactive_rag_cookbook.ipynb
│   ├── 02_agentic_langgraph_hitl.ipynb
│   ├── 03_semantic_cache_and_guardrails.ipynb
│   └── 04_self_healing_structured_outputs.ipynb
├── studio-app/                     # Ứng dụng Web Tương Tác Trực Quan Độc Lập
│   └── index.html                  # Giao diện Academy 8 bài + 5 Advanced Labs
├── papers/                         # Bản phân tích & Đúc kết 12 Papers kinh điển
│   ├── 01_rag_retrieval_papers.md
│   ├── 02_agentic_workflows_papers.md
│   └── 03_evals_and_serving_papers.md
├── tests/                          # Bộ kiểm thử tự động xác minh môi trường & code
│   └── test_handbook_smoke.py
├── requirements.txt                # Thư viện Python cần thiết
└── .env.example                    # Mẫu cấu hình API keys
```

---

## ⚖️ Giấy Phép & Đóng Góp
Kho tài liệu được phát hành theo giấy phép **MIT License**. Mọi đóng góp (Pull Requests) bổ sung paper mới, repo mới hoặc notebook thực hành đều được hoan nghênh nồng nhiệt!
