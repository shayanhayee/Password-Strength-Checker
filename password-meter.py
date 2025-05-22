import streamlit as st
import re
st.set_page_config(page_title="Password Strength Checker", page_icon=":lock:")

st.title("Password Strength Checker")
st.write("##### Check the strength of your password and get tips to make it stronger")
st.write("Use the password strength checker to evaluate the strength of your password and get suggestions for improvement")
st.write("#### Enter your password below:") 

password = st.text_input("Enter Your Password", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Check digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:   
        feedback.append("Password should contain at least one special character.")

    # Final evaluation
    if score == 4:
        feedback.append("✅ Woahhhh! Your password is very strong!🎉")
    elif score == 3:
        feedback.append("👍Your password is Medium!")
    else:
        feedback.append("❌Your password is weak! Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter a password to check its strength.")