def analyze_text(text: str) -> dict:
    """
    Menganalisis panjang teks, jumlah kata, dan karakter.
    """
    words = text.split()
    return {
        "char_count": len(text),
        "word_count": len(words),
        "is_empty": len(text.strip()) == 0
    }