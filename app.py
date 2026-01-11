import streamlit as st
from risk_engine import calculate_risk
from model import predict_risk

EXPLANATIONS = {
    "Urgent language detected":
        "Scam listings often use urgency to pressure candidates into quick decisions.",

    "No company website provided":
        "Legitimate companies usually have an official website or careers page.",

    "Unusually high stipend mentioned":
        "Very high stipends for internships are often used as bait.",

    "Candidate asked to pay for internship":
        "Legitimate internships do not require upfront payment from candidates.",

    "Low information internship description":
        "The internship description lacks sufficient details. Verify role responsibilities, company background, and contact information.",

    "Suspicious or placeholder company website":
        "The provided website does not appear to be an official company domain. Verify the organization independently."
}

st.title("InternGuard+")
st.caption(
    "Analyze internship listings for potential scams, red flags, and trust signals. "
    "This tool provides decision support — always verify independently."
)

description = st.text_area(
    "Paste internship description here:",
    placeholder="Example: Software Engineering Intern, 6-month role with stipend, no fees..."
)

website = st.text_input(
    "Company website (optional):",
    placeholder="https://careers.company.com"
)

if st.button("Check Risk"):
    rule_score, reasons = calculate_risk(description, website)
    ml_score = predict_risk(description)
    score = int((rule_score + ml_score) / 2)

    # === SUMMARY ===
    st.subheader(f"Risk Score: {score}/100")

    # Confidence estimation
    if ("Candidate asked to pay for internship" in reasons) or len(reasons) >= 3:
        confidence = "High"
    elif len(reasons) == 2:
        confidence = "Medium"
    else:
        confidence = "Low"

    st.markdown(f"**Confidence Level:** {confidence}")

    # === VERDICT ===
    if score >= 60:
        st.error("🚨 High Risk Internship")
    elif score >= 30:
        st.warning("⚠️ Proceed with Caution")
    else:
        st.success("✅ Likely Safe")

    # Reassurance for safe cases
    if score < 30:
        st.info(
            "No major red flags were detected. "
            "The internship description is detailed, does not request payment, "
            "and the company website appears legitimate."
        )

    # === DETAILED ANALYSIS ===
    with st.expander("🔍 View Detailed Analysis", expanded=False):
        st.subheader("Reasons & Explanations")

        if not reasons:
            st.write("• No significant risk indicators were detected.")
        else:
            for r in reasons:
                st.write("•", r)
                if r in EXPLANATIONS:
                    st.caption(EXPLANATIONS[r])
