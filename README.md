# HCMUS-Vietnamese-correction-project

![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![BARTpho](https://img.shields.io/badge/Model-BARTpho-orange)

Đồ án cuối kỳ môn **Xử lý Ngôn ngữ Tự nhiên (NLP)** - Trường ĐH Khoa học Tự nhiên, ĐHQG-HCM (HCMUS).

Dự án xây dựng mô hình tự động phát hiện và sửa lỗi chính tả tiếng Việt (bao gồm lỗi gõ sai, lỗi dấu, lỗi OCR) sử dụng mô hình ngôn ngữ tiền huấn luyện **BARTpho-syllable**.

## 🚀 Demo
Trải nghiệm mô hình trực tiếp tại Hugging Face Space hoặc chạy code dưới đây.
* **Model on Hub:** [pqthinh232/HCMUS-vietnamese-correction-project](https://huggingface.co/pqthinh232/HCMUS-vietnamese-correction-project)
* **Dataset:** [pqthinh232/vietnamese-correction-60k-mixed](https://huggingface.co/datasets/pqthinh232/vietnamese-correction-60k-mixed)

## 📊 Dataset
Chúng tôi sử dụng tổng cộng **60,351 cặp câu** để huấn luyện, bao gồm:
1. **HCMUS Dataset (20k):** Dữ liệu do nhóm tự thu thập và gán nhãn thủ công (xử lý lỗi OCR từ văn bản hành chính/sách).
2. **External Dataset (40k):** Lấy từ bộ dữ liệu mã nguồn mở (bmd1905) để tăng độ đa dạng.

| Split | Số lượng mẫu |
|-------|--------------|
| Train | 50,000       |
| Val   | 5,000        |
| Test  | 5,000        |

## 🛠️ Phương pháp (Methodology)
* **Base Model:** `vinai/bartpho-syllable`
* **Technique:** Fine-tuning Seq2Seq (Sequence-to-Sequence).
* **Hardware:** NVIDIA A100 (40GB VRAM) on Vast.ai.
* **Training Config:**
    * Epochs: 5
    * Batch size: 32
    * Learning rate: 3e-5
    * FP16/BF16: Enabled

## 📈 Kết quả (Results)
Mô hình đạt kết quả rất tốt trên tập kiểm thử (Test set):

| Metric | Score | Ý nghĩa |
|--------|-------|---------|
| **BLEU** | **89.35** | Độ tương đồng rất cao so với câu gốc |
| **CER** | **0.019** | Tỷ lệ lỗi ký tự chỉ ~1.9% |
| **Loss** | 0.021 | Mô hình hội tụ tốt |

*(Kết quả đã được chuẩn hóa văn bản trước khi đánh giá)*

## 💻 Cài đặt & Sử dụng (Installation & Usage)

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt