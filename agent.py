from memory import recall_memory


def analyze_feedback(feedback):
    """Analyze new feedback using organizational memory."""

    memories = recall_memory(feedback)

    if not memories:
        return {
            "feedback": feedback,
            "past_experience": [],
            "recommendation": "No relevant past experience found. Review this feedback as a new case."
        }

    past_experience = []

    for memory in memories:
        past_experience.append({
            "text": memory.get("text", ""),
            "score": memory.get("scores", {}).get("final", 0)
        })

    recommendation = (
        "Relevant organizational experience was found. "
        "Review the previous decisions and outcomes before making a new product decision."
    )

    return {
        "feedback": feedback,
        "past_experience": past_experience,
        "recommendation": recommendation
    }