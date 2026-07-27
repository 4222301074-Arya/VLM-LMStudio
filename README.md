# License Plate OCR Using Visual Language Model (VLM)

## Description

This project performs Optical Character Recognition (OCR) on Indonesian vehicle license plates using a Visual Language Model (VLM) running through LM Studio.

The model reads license plate images and predicts the plate text. Predictions are evaluated using Character Error Rate (CER).

---

## Dataset

Dataset:

Indonesian License Plate Recognition Dataset

Structure:

```text
dataset/
└── Indonesian License Plate Recognition Dataset/
    ├── classes.names
    ├── images/test/
    └── labels/test/
```

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## LM Studio Setup

1. Install LM Studio.
2. Download:

```text
Qwen2.5-VL-7B-Instruct
```

3. Load the model.
4. Start Local Server.

Default endpoint:

```text
http://localhost:1234/v1
```

---

## Project Structure

```text
license_plate_vlm/
│
├── dataset/
├── src/
│   ├── config.py
│   ├── ground_truth.py
│   ├── vlm_ocr.py
│   ├── metrics.py
│   └── main.py
│
├── outputs/
├── requirements.txt
└── README.md
```

---

## Running the Program

Move to source directory:

```bash
cd src
```

Run:

```bash
python main.py
```

---

## Output

Generated file:

```text
outputs/results.csv
```

Format:

```csv
image,ground_truth,prediction,CER_score
```

Example:

```csv
img001.jpg,B2842PKM,B2842PKM,0.0
img002.jpg,B1234ABC,B1234A8C,0.125
```

---

## Character Error Rate (CER)

Formula:

\[
CER = \frac{S + D + I}{N}
\]

Where:

- S = Substitution
- D = Deletion
- I = Insertion
- N = Number of characters in ground truth

Lower CER indicates better OCR performance.

---

## Workflow

```text
Image
  ↓
Qwen2.5-VL (LM Studio)
  ↓
Prediction
  ↓
CER Evaluation
  ↓
CSV Output
```

---

## Author

Computer Vision Final Project
Robotics Engineering
