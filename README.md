🛡️ InternGuard+

InternGuard+ is a deployed web application that analyzes internship listings and flags potential scams or red flags using a combination of rule-based heuristics and machine learning–based text analysis.
The tool is designed to help students make informed decisions before applying to internships by providing:
1) a risk score
2) a confidence level
and 3) clear, human-readable explanations

🔗 Live Demo:
https://internguardplus.streamlit.app/

🚩 Why InternGuard+?

Internship scams are increasingly common, especially on informal job portals and social media.
Many listings:
1) ask for upfront payments
2) lack company details
3) use urgency to pressure students
4) provide vague or misleading descriptions

InternGuard+ acts as a decision-support tool, helping users identify warning signs early and encouraging safer verification practices.

⚠️ This tool does not replace human judgment — it supports it.

✨ Key Features
🔍 Text-based risk analysis of internship descriptions
🧠 Hybrid detection system:
Rule-based red flag detection (payments, urgency, fake websites, etc.)
Machine learning model trained on labeled internship text
📊 Risk Score (0–100) indicating potential threat level
🎯 Confidence Level based on strength and number of detected signals
🧾 Explainable output with user-friendly reasons and guidance
🌐 Website validation heuristics for suspicious or placeholder domains
🖥️ Deployed web app using Streamlit Cloud

🧠 How It Works
1. Rule-Based Analysis

The system checks for common scam indicators such as:
1)Requests for upfront payment (registration/training fees)
2) Missing or suspicious company websites
3) Unrealistically high stipends
4) Urgent or pressure-based language
5) Very low-information descriptions
Each detected signal contributes to the overall risk score.

2. Machine Learning Model

A lightweight NLP model:
1) Uses TF-IDF vectorization
2) Trained with Logistic Regression
3) Learns patterns from labeled internship descriptions (safe vs risky)
4) The ML output is combined with rule-based scoring for balanced results.

3. Explainability & UX

Instead of just saying “unsafe”, InternGuard+ explains:
1) what was detected
2) why it matters
3) what users should verify next

This keeps the system ethical, transparent, and user-centric.

🧪 Example Outputs

🟢 Likely Safe — detailed role, no payment, legitimate website
⚠️ Proceed with Caution — missing details, unverifiable company
🚨 High Risk Internship — upfront payment + fake website + vague description
Each verdict includes explanations and guidance.

🛠️ Tech Stack
Python
Streamlit (UI + deployment)
Pandas, NumPy
Scikit-learn
NLP (TF-IDF)
Git & GitHub

📁 Project Structure
InternGuardPlus/
│
├── app.py                # Streamlit UI
├── risk_engine.py        # Rule-based risk logic
├── model.py              # ML model & prediction logic
├── requirements.txt      # Dependencies
├── data/
│   └── internships.csv   # Training dataset
└── .gitignore

⚠️ Limitations

1) The ML model is trained on a small curated dataset
2) Website validation is heuristic-based, not DNS or reputation-based
3) Results should be treated as advisory, not definitive

🚀 Future Enhancements

1) Larger and more diverse training dataset
2) Domain reputation checks (WHOIS / SSL validation)
3) User feedback loop to improve predictions
4) Browser extension or API version
5) Multilingual support

👩‍💻 Author

Built by Madhumita Ash
B.Tech IT | Cybersecurity & Data Analytics Enthusiast

📌 Disclaimer

InternGuard+ is an educational and decision-support tool.
Users should always independently verify internships through official company channels.
