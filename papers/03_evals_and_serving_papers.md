# 📊 TỔNG HỢP PAPERS KINH ĐIỂN: EVALS, SERVING & HẠ TẦNG SẢN XUẤT

> Tuyển tập phân tích các bài báo về đo lường chất lượng tự động (LLM Evals), tối ưu hóa bộ nhớ suy luận (vLLM Serving), và tinh chỉnh tham số hiệu quả (LoRA / QLoRA).

---

## 1. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
* **Tác giả:** Lianmin Zheng, Wei-Lin Chiang et al. (LMSYS Org, UC Berkeley, UCSD, CMU) — NeurIPS 2023
* **Liên kết Paper:** [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)
* **Vấn đề giải quyết:** Đánh giá bằng con người (Human Evaluation) quá chậm, cực kỳ đắt đỏ và không thể đưa vào quy trình phát hành phần mềm CI/CD hàng ngày.

### ⚙️ Phát hiện cốt lõi & Cách xử lý 4 Thiên kiến của LLM Judge:
1. **Position Bias (Thiên kiến vị trí):** LLM có xu hướng thích câu trả lời nằm ở vị trí đầu tiên (Model A).
   * *Cách khắc phục:* Đảo ngược vị trí (Swap Order: A/B rồi B/A) và tính điểm trung bình.
2. **Verbosity Bias (Thiên kiến độ dài):** LLM thường chấm điểm cao hơn cho câu trả lời dài dòng dù nội dung rỗng tuếch.
   * *Cách khắc phục:* Thêm ràng buộc rõ ràng vào Prompt của Judge: *"Độ súc tích và chính xác là tiêu chí hàng đầu, câu trả lời dài dòng không liên quan sẽ bị trừ điểm"*.
3. **Self-Enhancement Bias (Thiên kiến tự thân):** Mô hình của OpenAI có xu hướng chấm điểm cao hơn cho chính output của OpenAI.
   * *Cách khắc phục:* Dùng giám khảo chéo (ví dụ: Claude chấm GPT, hoặc Gemini chấm Claude).

---

## 2. LoRA (Low-Rank Adaptation) & QLoRA
* **LoRA Paper:** Edward J. Hu et al. (Microsoft) — ICLR 2022 ([arXiv:2106.09685](https://arxiv.org/abs/2106.09685))
* **QLoRA Paper:** Tim Dettmers et al. (University of Washington) — NeurIPS 2023 ([arXiv:2305.14314](https://arxiv.org/abs/2305.14314))

### ⚙️ Bản chất toán học & Công nghệ:
Thay vì cập nhật toàn bộ ma trận trọng số gốc $W_0 \in \mathbb{R}^{d \times k}$ (đòi hỏi lưu gradient và optimizer state cực lớn):
$$W = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A)$$
* $W_0$ được đóng băng hoàn toàn (Frozen).
* $A \in \mathbb{R}^{r \times k}$ được khởi tạo phân phối chuẩn $\mathcal{N}(0, \sigma^2)$.
* $B \in \mathbb{R}^{d \times r}$ được khởi tạo bằng $0$.
* Với rank $r \ll \min(d, k)$ (ví dụ: $r=8$ hoặc $16$), số lượng tham số cần huấn luyện giảm hơn $99.9\%$.

**Đột phá của QLoRA:**
* Nén ma trận trọng số gốc $W_0$ xuống định dạng **4-bit NormalFloat (NF4)** (tối ưu theo phân phối chuẩn tích lũy).
* **Double Quantization:** Lượng tử hóa tiếp cả các hằng số lượng tử hóa, tiết kiệm thêm $0.37\text{ bit/tham số}$.
* **Paged Optimizers:** Đẩy Optimizer States qua lại giữa RAM và VRAM GPU qua CUDA Unified Memory để không bao giờ bị lỗi OOM (Out Of Memory).

---

## 3. vLLM: Efficient Memory Management with PagedAttention
* **Tác giả:** Woosuk Kwon et al. (UC Berkeley) — SOSP 2023
* **Liên kết Paper:** [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
* **Vấn đề giải quyết:** Trong suy luận LLM, bộ nhớ KV Cache (lưu trữ Key/Value của các token trước) phình to rất nhanh. Các hệ thống cũ cấp phát bộ nhớ tĩnh liên tục (contiguous memory), gây lãng phí từ $60\% - 80\%$ VRAM do hiện tượng phân mảnh bộ nhớ (Memory Fragmentation).

### ⚙️ Đột phá của PagedAttention:
Lấy cảm hứng từ cơ chế phân trang bộ nhớ ảo (Virtual Memory Paging) trong hệ điều hành:
* Chia KV Cache thành các khối cố định (**Physical Blocks** - ví dụ 16 token/block).
* Cấp phát bộ nhớ không liên tục trên VRAM và dùng **Bảng trang (Block Table)** để ánh xạ từ Logical Token Index sang Physical Block.
* Cho phép nhiều luồng suy luận chia sẻ chung khối tiền tố (Prefix Caching) mà không tốn thêm VRAM.
* **Kết quả:** Tăng số lượng request phục vụ đồng thời lên từ $2\times$ đến $4\times$.

---

## 4. Báo Cáo Thực Nghiệm: What We Learned from a Year of Building with LLMs
* **Tác giả:** Eugene Yan, Bryan Bischof, Charles Frye et al. — [applied-llms.org](https://applied-llms.org/)

### 📌 4 Đúc kết sống còn cho Sản phẩm Thực tế:
1. **Evals là vũ khí cạnh tranh số 1:** Không có bộ kiểm thử tự động, bạn sẽ không bao giờ dám sửa prompt hay đổi model khi sản phẩm đã có người dùng.
2. **Kỹ thuật Few-Shot Prompting luôn đánh bại Zero-Shot:** Cung cấp ít nhất 3 đến 5 ví dụ mẫu ($n \ge 3$) vào prompt giúp độ ổn định của output tăng vọt.
3. **Cấu trúc dữ liệu có kiểm định (Structured Outputs):** Không bao giờ tin tưởng chuỗi văn bản tự do; luôn bọc đầu ra trong Pydantic / JSON Schema có cơ chế thử lại.
4. **Nhỏ trước, Lớn sau:** Bắt đầu bằng prompt đơn giản và model nhỏ (như GPT-4o-mini hoặc Gemini 2.0 Flash) trước khi nghĩ đến model khổng lồ hoặc fine-tuning phức tạp.
