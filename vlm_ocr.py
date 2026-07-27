import base64

from openai import OpenAI

from config import (
    LMSTUDIO_URL,
    MODEL_NAME,
    PROMPT
)

client = OpenAI(
    base_url=LMSTUDIO_URL,
    api_key="lm-studio"
)


def predict_plate(image_path):

    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(
            f.read()
        ).decode()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": PROMPT
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )

    result = (
        response
        .choices[0]
        .message
        .content
    )

    return result.strip().upper().replace(" ", "")