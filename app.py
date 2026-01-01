import gradio as gr
from transformers import pipeline

# Load model từ Hugging Face
model_checkpoint = "pqthinh232/HCMUS-vietnamese-correction-project"
corrector = pipeline("text2text-generation", model=model_checkpoint)

def correct_text(text):
    # Hàm xử lý
    result = corrector(text, max_length=128, num_beams = 10, early_stopping=True)
    return result[0]['generated_text']

# Tạo giao diện
demo = gr.Interface(
    fn=correct_text,
    inputs=gr.Textbox(lines=3, placeholder="Nhập câu sai chính tả hoặc không dấu vào đây... (Ví dụ: hom lay troi dep qua)"),
    outputs=gr.Textbox(label="Kết quả sửa lỗi"),
    title="Vietnamese Spelling Correction - HCMUS",
    description="Mô hình sửa lỗi chính tả tiếng Việt (Fine-tuned on 60k samples). Nhập câu sai và xem kết quả.",
    examples=[
        ["mo hình hoat dọng khá tót"],
        ["toi dang di hoc o truong dai hoc khoa hoc tu nhien"],
        ["toiiii học chuyen ngành Khoa hóc may tínhhhhh"],
        ["câu chuyen cua ban that thu vị"]
    ]
)

if __name__ == "__main__":
    demo.launch()