import streamlit as st

st.header(f"Here is a test header!")
activity = st.selectbox("Choose an activity:", ["Activity 1", "Activity 2", "Activity 3"])
st.write(f"You selected: {activity}")

count = 0
if st.button("Confirm Selection"):
    st.write(f"Confirmed activity: {activity}")
    count += 1
    st.write(f"Selection confirmed {count} time(s).")


