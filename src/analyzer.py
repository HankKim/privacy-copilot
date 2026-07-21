import ollama
from config import OLLAMA_MODEL

def contains_any(text, keywords):
    """키워드 중 하나라도 포함되면 True"""
    return any(keyword in text for keyword in keywords)


def analyze(text):
    checks = {
        "개인정보처리방침": contains_any(
            text,
            [
                "개인정보처리방침",
                "개인정보 처리방침",
                "개인정보 처리 방침",
                "처리방침",
                "Privacy Policy",
            ],
       ),

        "수집 목적": contains_any(
            text,
            [
                "수집 목적",
                "수집목적",
                "이용 목적",
                "이용목적",
                "처리 목적",
                "처리목적",
            ],
        ),

        "보유기간": contains_any(
            text,
            [
                "보유기간",
                "보유 기간",
                "보관기간",
                "보관 기간",
            ],
        ),

        "제3자 제공": contains_any(
            text,
            [
                "제3자",
                "제3자 제공",
                "제3자제공",
            ],
        ),

        "파기": contains_any(
            text,
            [
                "파기",
                "파기절차",
                "파기 절차",
            ],
        ),
    }

    return checks