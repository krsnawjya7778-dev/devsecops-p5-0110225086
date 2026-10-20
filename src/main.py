from sanitizer import sanitize_input
from analyzer import analyze_text
from logger import log_event

def main():
    print("=== Secure Text & Tag Analyzer Utility ===")
    sample_input = "<script>alert('XSS');</script> Halo, selamat datang di pipeline DevSecOps!"
    
    log_event("Application started.")
    
    cleaned = sanitize_input(sample_input)
    print(f"Sanitized Input: {cleaned}")
    
    stats = analyze_text(cleaned)
    print(f"Analysis Stats: {stats}")
    
    log_event("Application finished successfully.")

if __name__ == "__main__":
    main()