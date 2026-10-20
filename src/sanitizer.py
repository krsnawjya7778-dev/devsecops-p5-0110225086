import html

def sanitize_input(raw_text: str) -> str:
    """
    Membersihkan input string dari potensi injeksi HTML/XSS dasar.
    """
    if not isinstance(raw_text, str):
        return ""
    escaped_text = html.escape(raw_text)
    return escaped_text