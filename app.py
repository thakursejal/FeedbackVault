import streamlit as st
from agent import analyze_feedback

st.set_page_config(
    page_title="FeedbackVault AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 FeedbackVault AI")
st.subheader("AI Product Feedback Agent with Hindsight Memory")

st.write(
    "Submit new customer feedback and let the agent recall "
    "relevant organizational experience before recommending a product action."
)

feedback = st.text_area(
    "💬 Enter customer feedback",
    placeholder="Example: Customers are requesting WhatsApp notifications again..."
)

if st.button("🔍 Analyze Feedback", type="primary"):

    if not feedback.strip():
        st.warning("Please enter some customer feedback.")
    else:
        with st.spinner("Searching organizational memory..."):
            result = analyze_feedback(feedback)

        st.success("Analysis complete!")

        st.markdown("### 📝 New Feedback")
        st.write(result["feedback"])

        st.markdown("### 🧠 Hindsight Memory")

        if result["past_experience"]:
            for memory in result["past_experience"]:
                st.info(memory["text"])
        else:
            st.info("No relevant past experience found.")

        st.markdown("### 💡 Agent Recommendation")
        st.write(result["recommendation"])