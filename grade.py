import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Student Grade", page_icon="🎓")

# App Heading
st.title("🎓 Student Grade Calculator")
st.write("Enter a mark between 0 and 100 to find the corresponding letter grade.")

# Input widget (number_input handles numeric inputs cleanly)
# Default value is set to 0.0, step to 1.0
mark = st.number_input(
    "Enter your mark (0 - 100):",
    min_value=-100.0,
    max_value=200.0,
    value=75.0,
    step=1.0,
    help="Type a score from 0 to 100"
)

# Button to trigger grading logic
if st.button("Calculate Grade", type="primary"):
    
    # --- Edge Case Handling ---
    if mark < 0 or mark > 100:
        st.error("⚠️ Invalid Mark! Please enter a number between 0 and 100.")
    
    # --- Grading Scale Logic ---
    else:
        if mark >= 90:
            grade = "A"
            color = "green"
        elif mark >= 80:
            grade = "B"
            color = "blue"
        elif mark >= 70:
            grade = "C"
            color = "orange"
        elif mark >= 60:
            grade = "D"
            color = "orange"
        else:
            grade = "E"
            color = "red"
            
        # Output Display
        st.success(f"**Mark:** {mark:.1f} ➔ **Grade:** {grade}")
        st.balloons() if grade in ["A", "B"] else None