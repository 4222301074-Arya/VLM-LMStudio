def load_ground_truth(label_file):
    with open(label_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    # Hilangkan spasi supaya konsisten
    text = text.replace(" ", "")

    return text.upper()