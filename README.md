# HCMUS-Vietnamese-spelling-correction-project

![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)

### Final project for the Introduction to Natural Language Processing course, University of Science, VNU-HCM (HCMUS)

### Vietnamese Spelling Correction based on [BARTpho](https://github.com/VinAIResearch/BARTpho)

## Introduction
This project focuses on building a robust **Vietnamese Spelling Correction system**. The model is designed to detect and correct various types of errors, including OCR errors, typos, missing diacritics, and grammatical mistakes in Vietnamese text.

The core architecture is based on **[BARTpho-syllable](https://huggingface.co/vinai/bartpho-syllable)**, a state-of-the-art pre-trained sequence-to-sequence model for Vietnamese, fine-tuned on a mixed dataset of 60,000 samples.

## Model
The fine-tuned model and dataset are hosted on Hugging Face Hub:

- **Model Weights:** [pqthinh232/HCMUS-vietnamese-correction-project](https://huggingface.co/pqthinh232/HCMUS-vietnamese-correction-project)
- **Dataset:** [pqthinh232/vietnamese-correction-60k](https://huggingface.co/datasets/pqthinh232/vietnamese-correction-60k)

## Dataset
To ensure both domain-specific accuracy and general language understanding, we constructed a dataset of **60,000 samples** by combining two sources:

| Source | Samples | Domain | Description |
| :--- | :--- | :--- | :--- |
| **Internal (Midterm)** | ~20k | **History** | Collected by our team. Focuses on Vietnamese historical events, OCR errors from scanned books |
| **External** | ~40k | **News articles** | Sourced from **[bmd1905/error-correction-vi](https://huggingface.co/datasets/bmd1905/error-correction-vi)**. Covers general news, articles and society to improve model generalization. |
| **Total** | **60k** | **Mixed** | Split: 50k Train / 5k Val / 5k Test |

## Methodology
We utilized the **Seq2Seq (Sequence-to-Sequence)** approach to treat spelling correction as a "translation" task (from *Error Text* to *Correct Text*).

- **Base Model:** `vinai/bartpho-syllable`
- **Infrastructure:** Fine-tuned on **NVIDIA A100 (40GB VRAM)** via Vast.ai.
- **Training Configuration:**
    - Epochs: 5
    - Batch Size: 64 (Effective)
    - Learning Rate: 3e-5
    - Optimizer: AdamW
    - Precision: BF16 (Brain Floating Point)

## Results

### Final Evaluation on Test Set (5,000 samples)
We evaluated the model on a strictly held-out Test set. The table below compares the performance of the pre-trained `vinai/bartpho-syllable` (Baseline) versus our Fine-tuned model.

| Model | BLEU (↑) | CER (↓) | WER (↓) | F1-Rouge1 (↑) |
| :--- | :---: | :---: | :---: | :---: |
| **Baseline** (Pre-trained) | 32.97 | 0.5859 | 0.8174 | 0.7421 |
| **Our Fine-tuned Model** | **89.05** | **0.0201** | **0.0564** | **0.9825** |

### Training Progression (Validation Set)
The model showed consistent convergence across 5 epochs on the Validation set (5,000 samples).
![Visual improvement](images/training_log.png)
*(Note: Metrics were calculated after text normalization to handle whitespace and underscore inconsistencies).*

## Usage

### Installation
```bash
pip install transformers torch sentencepiece
```

### Inference
```bash
from transformers import pipeline

# Load the fine-tuned model
checkpoint = "pqthinh232/HCMUS-vietnamese-correction-project"
corrector = pipeline("text2text-generation", model=checkpoint)

# Inference
input_text = "toiii la sinh viến đai học khoa hoc tu nhien"
output = corrector(input_text, max_length=128)

print(f"Input: {input_text}")
print(f"Output: {output[0]['generated_text']}")
# Expected Output: "tôi là sinh viên đại học khoa học tự nhiên."
```
# References
[BARTpho](https://github.com/VinAIResearch/BARTpho) - The pre-trained model used as the backbone.
[bmd1905/error-correction-vi](https://huggingface.co/datasets/bmd1905/error-correction-vi) - Used for data augmentation.

## References
We would like to express our gratitude to the authors of the following open-source projects and papers:

*   **BARTpho:** [VinAI Research](https://github.com/VinAIResearch/BARTpho) - The pre-trained model used as the backbone.
*   **External Dataset:** [bmd1905/error-correction-vi](https://huggingface.co/datasets/bmd1905/error-correction-vi) - Used for data augmentation to improve model generalization.

## Authors
This project was developed by a team of students from the **University of Science, VNU-HCM (HCMUS)**:

| Student Name | Student ID |
| :--- | :--- |
| **Phạm Quang Thịnh** | 23127485 | 
| **Lê Quốc Thiện** | 23127481 | 
| **Nguyễn Lê Quang** | 23127109 | 
| **Đỗ Ngọc Minh Tuấn** | 23127137 | 

