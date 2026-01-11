import re

def calculate_risk(text, website):
    risk = 0
    reasons = []

    text = text.lower()

    # Urgent language
    urgent_words = ["apply now", "urgent", "limited slots", "immediate"]
    for word in urgent_words:
        if word in text:
            risk += 15
            reasons.append("Urgent language detected")
            break

    # Missing website
    if website.strip() == "":
        risk += 30
        reasons.append("No company website provided")

    # Unrealistic stipend
    if re.search(r"\b\d{5,}\b", text):
        risk += 25
        reasons.append("Unusually high stipend mentioned")

    # Pay-to-join detection (IMPORTANT)
    payment_patterns = [
        "registration fee",
        "training fee",
        "enrollment fee",
        "onboarding charge",
        "pay.*fee",
        "payment required",
        "fees applicable",
        "must pay",
        "pay .* amount"
    ]

    for pattern in payment_patterns:
        if re.search(pattern, text):
            risk += 40
            reasons.append("Candidate asked to pay for internship")
            break
    # Low information detection
    # Improved low information detection
    important_sections = ["responsibilities", "eligibility", "requirements", "internship details"]
    missing_sections = 0
    for section in important_sections:
        if section not in text:
            missing_sections += 1
        if missing_sections >= 3:
            risk += 10
            reasons.append("Low information internship description")

    # Suspicious website detection
    suspicious_domains = ["example.com", "unknowncompany.com", "freehosting", "blogspot", "wordpress"]
    for domain in suspicious_domains:
        if domain in website.lower():
            risk += 15
            reasons.append("Suspicious or placeholder company website")
            break

    trusted_domains = ["deloitte.com", "infosys.com", "tcs.com", "microsoft.com", "google.com"]
    for domain in trusted_domains:
        if domain in website.lower():
            risk -= 10
            break


    return min(risk, 100), reasons
