import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sanitizer import sanitize_input
from analyzer import analyze_text

def test_sanitize_input():
    malicious = "<script>alert('test')</script>"
    safe = sanitize_input(malicious)
    assert "<script>" not in safe

def test_analyze_text():
    sample = "DevSecOps Pipeline Test"
    stats = analyze_text(sample)
    assert stats["word_count"] == 3
    assert stats["char_count"] > 0