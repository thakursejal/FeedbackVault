import streamlit as st
from agent import analyze_feedback
from memory import retain_memory

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

        st.markdown("### 📌 Record Product Decision")

        decision = st.text_area(
            "What decision did the product team make?",
            placeholder="Example: Reconsidered WhatsApp notifications because customer demand increased."
        )
        outcome = st.text_area(
    "What was the outcome?",
    placeholder="Example: Customer demand increased and the feature moved to product review."
)

if st.button("💾 Save Decision to Hindsight"):

    if not decision.strip():
        st.warning("Please enter the product decision.")

    elif not outcome.strip():
        st.warning("Please enter the outcome.")

    else:
        memory_text = f"""
Customer feedback:
{result["feedback"]}

Product team decision:
{decision}

Outcome:
{outcome}

This decision and outcome were recorded as organizational experience
for future product feedback analysis.
"""

        with st.spinner("Saving decision to Hindsight..."):
            retain_memory(memory_text)

        st.success("✅ Decision and outcome saved to Hindsight!")