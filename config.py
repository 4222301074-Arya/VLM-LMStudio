DATASET_DIR = "dataset"

LMSTUDIO_URL = "http://127.0.0.1:1234/v1"

MODEL_NAME = "qwen/qwen2.5-vl-7b"

PROMPT = """
Read the license plate carefully.

Return ONLY the license plate number.

Rules:
- No explanation
- No punctuation
- No extra words
- Keep letters and numbers only
"""