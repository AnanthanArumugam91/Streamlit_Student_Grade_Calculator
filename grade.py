import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# --- MODERN ELEGANT STYLING ---
st.markdown("""
<style>
    /* Dark Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Elegant Grade Display Badges */
    .grade-badge {
        font-size: 3.5rem;
        font-weight: 800;
        padding: 12px 32px;
        border-radius: 16px;
        display: inline-block;
        text-align: center;
    }
    .grade-A { background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1.5px solid #22c55e; }
    .grade-B { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1.5px solid #3b82f6; }
    .grade-C { background: rgba(234, 179, 8, 0.15); color: #facc15; border: 1.5px solid #eab308; }
    .grade-D { background: rgba(249, 115, 22, 0.15); color: #fb923c; border: 1.5px solid #f97316; }
    .grade-E { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1.5px solid #ef4444; }

    /* Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #6366f1 0%, #4f46e5 100%);
        color: #ffffff;
        font-weight: 600;
        font-size: 1rem;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🎓 Student Grade App")
st.caption("Enter a score between 0 and 100 to determine the exact performance grade.")
st.divider()

# --- INPUT & ACTION SECTION ---
mark = st.number_input(
    "Enter your mark (0 - 100):",
    min_value=-50.0,
    max_value=150.0,
    value=85.0,
    step=1.0,
    help="Type any mark between 0 and 100"
)

calculate_btn = st.button("Calculate Grade", type="primary")

st.divider()

# --- OUTPUT RESULT DISPLAY ---
if calculate_btn:
    # Edge case handling
    if mark < 0 or mark > 100:
        st.error("⚠️ Invalid input! Please enter a mark strictly between 0 and 100.")
    else:
        # Grading Logic
        if mark >= 90:
            grade, badge_style = "A", "grade-A"
        elif mark >= 80:
            grade, badge_style = "B", "grade-B"
        elif mark >= 70:
            grade, badge_style = "C", "grade-C"
        elif mark >= 60:
            grade, badge_style = "D", "grade-D"
        else:
            grade, badge_style = "E", "grade-E"

        # Result Layout using native Streamlit Divider Cards
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f'<div class="grade-badge {badge_style}">{grade}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f"### Mark: {mark:.1f}")
            st.markdown(f"Resulting Grade: **{grade}**")

        if grade in ["A", "B"]:
            st.balloons()