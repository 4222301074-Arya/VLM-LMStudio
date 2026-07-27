from jiwer import cer


def compute_cer(gt, pred):

    gt = gt.strip().upper().replace(" ", "")
    pred = pred.strip().upper().replace(" ", "")

    return cer(gt, pred)