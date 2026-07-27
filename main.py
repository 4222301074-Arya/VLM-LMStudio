from pathlib import Path

import pandas as pd
from tqdm import tqdm

from config import DATASET_DIR
from ground_truth import load_ground_truth
from metrics import compute_cer
from vlm_ocr import predict_plate


def main():

    dataset_dir = Path(DATASET_DIR)

    image_dir = dataset_dir / "image"
    label_dir = dataset_dir / "ground-truth"

    image_files = []

    image_files.extend(
        image_dir.glob("*.jpg")
    )

    image_files.extend(
        image_dir.glob("*.jpeg")
    )

    image_files.extend(
        image_dir.glob("*.png")
    )

    image_files = sorted(image_files)

    print(
        f"Found {len(image_files)} images"
    )

    results = []

    for image_path in tqdm(image_files):

        label_path = (
            label_dir /
            f"{image_path.stem}.txt"
        )

        if not label_path.exists():

            print(
                f"Missing label: {label_path}"
            )
            continue

        gt = load_ground_truth(
            label_path
        )

        try:

            pred = predict_plate(
                str(image_path)
            )

            score = compute_cer(
                gt,
                pred
            )

        except Exception as e:

            print(
                f"\nERROR: {image_path.name}"
            )
            print(e)

            pred = ""
            score = None

        results.append(
            {
                "image":
                    image_path.name,

                "ground_truth":
                    gt,

                "prediction":
                    pred,

                "CER_score":
                    score
            }
        )

    if len(results) == 0:

        print(
            "No results generated."
        )
        return

    df = pd.DataFrame(results)

    output_dir = Path("outputs")

    output_dir.mkdir(
        exist_ok=True
    )

    output_csv = (
        output_dir /
        "results.csv"
    )

    df.to_csv(
        output_csv,
        index=False
    )

    print()
    print(
        f"Saved: {output_csv}"
    )

    valid_scores = (
        df["CER_score"]
        .dropna()
    )

    if len(valid_scores) > 0:

        avg_cer = (
            valid_scores.mean()
        )

        accuracy = (
            1 - avg_cer
        ) * 100

        print(
            f"Average CER : {avg_cer:.4f}"
        )

        print(
            f"Accuracy    : {accuracy:.2f}%"
        )


if __name__ == "__main__":
    main()