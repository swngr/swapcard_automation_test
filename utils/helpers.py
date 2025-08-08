def extract_rating_from_aria_label(text):
    # Example input: "Rated 4.6 out of 5"
    import re
    match = re.search(r'Rated\s+([\d.]+)', text)
    if match:
        return float(match.group(1))
    raise ValueError(f"Cannot parse rating from: '{text}'")