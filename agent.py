from memory import recall_memory


def analyze_feedback(feedback):
    """Analyze new feedback using organizational memory."""

    memories = recall_memory(feedback)

    past_experience = []
    seen = set()

    for memory in memories:
        text = memory.get("text", "").strip()

        if text and text not in seen:
            seen.add(text)

            past_experience.append({
                "text": text,
                "score": memory.get("scores", {}).get("final", 0)
            })

    if not past_experience:
        recommendation = (
            "No relevant organizational experience was found. "
            "Treat this as a new product feedback case and evaluate demand."
        )

    else:
        combined_memory = " ".join(
            memory["text"].lower()
            for memory in past_experience
        )

        if "product review" in combined_memory:
            recommendation = (
                "📌 A previous decision moved this feature to product review "
                "after increased customer demand. Use that outcome as the latest "
                "organizational context when evaluating this request."
            )

        elif "rejected" in combined_memory and "low customer demand" in combined_memory:
            recommendation = (
                "🔄 Reconsider the previous decision. "
                "This request was previously rejected because customer demand was low, "
                "but the request has appeared again. Review the current demand before "
                "making the same decision."
            )

        elif "implemented" in combined_memory:
            recommendation = (
                "📈 A similar request was previously implemented. "
                "Review its historical outcome before deciding how to handle this feedback."
            )

        else:
            recommendation = (
                "🧠 Relevant organizational experience was found. "
                "Use the previous decisions and outcomes as context for the new decision."
            )

    return {
        "feedback": feedback,
        "past_experience": past_experience,
        "recommendation": recommendation
    }