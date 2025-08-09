import textract

def parse_resume(file):
    try:
        text = textract.process(file).decode("utf-8")
    except Exception:
        text = file.read().decode("utf-8")
    return text
