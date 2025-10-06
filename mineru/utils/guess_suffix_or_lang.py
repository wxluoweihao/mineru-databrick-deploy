from pathlib import Path

from magika import Magika


DEFAULT_LANG = "txt"
magika = Magika()

def guess_language_by_text(code):
    codebytes = code.encode(encoding="utf-8")
    lang = magika.identify_bytes(codebytes).prediction.output.label
    return lang if lang != "unknown" else DEFAULT_LANG


def guess_suffix_by_bytes(file_bytes, file_path=None) -> str:
    suffix = magika.identify_bytes(file_bytes).prediction.output.label
    if file_path and suffix in ["ai"] and Path(file_path).suffix.lower() in [".pdf"]:
        suffix = "pdf"
    return suffix


def guess_suffix_by_path(file_path) -> str:
    if not isinstance(file_path, Path):
        file_path = Path(file_path)
    suffix = magika.identify_path(file_path).prediction.output.label
    if suffix in ["ai"] and file_path.suffix.lower() in [".pdf"]:
        suffix = "pdf"
    return suffix