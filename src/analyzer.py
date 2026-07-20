def analyze(text):
    checks = {
        "개인정보처리방침": "개인정보처리방침" in text,
        "수집 목적": "수집" in text,
        "보유기간": "보유" in text,
        "제3자 제공": "제3자" in text,
        "파기": "파기" in text,
    }

    return checks