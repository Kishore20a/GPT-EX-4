"""
intent_module.py
Part H: Intelligent Intent Detection (Q9)
Experiment 4: Personalized Recommendation System

Identifies user intent using natural language patterns or LLM.
Supported intents:
- GENERATE_RECOMMENDATION
- REFINE_RECOMMENDATION
- SHOW_PROFILE
- EXPLAIN_RECOMMENDATION
- SAVE_RECOMMENDATION
- EXIT
"""


def detect_intent(user_input: str) -> str:
    """
    Detect user intent from a natural language query or command.
    """
    text = user_input.strip().lower()

    if not text:
        return "GENERATE_RECOMMENDATION"

    if any(k in text for k in ["exit", "quit", "bye", "stop", "close"]):
        return "EXIT"

    if any(k in text for k in ["save", "export", "download", "write file", "store"]):
        return "SAVE_RECOMMENDATION"

    if any(k in text for k in ["why", "explain", "reason", "justification", "why did you"]):
        return "EXPLAIN_RECOMMENDATION"

    if any(k in text for k in ["show profile", "my profile", "view profile", "profile details", "user info"]):
        return "SHOW_PROFILE"

    if any(k in text for k in ["refine", "prefer", "don't want", "do not want", "more", "less", "filter", "beginner", "advanced", "change", "feedback", "instead"]):
        return "REFINE_RECOMMENDATION"

    if any(k in text for k in ["recommend", "suggest", "find courses", "generate", "start", "give me"]):
        return "GENERATE_RECOMMENDATION"

    # Default fallback intent
    return "GENERATE_RECOMMENDATION"


def display_detected_intent(user_input: str, detected_intent: str) -> None:
    """
    Display query and detected intent matching Part H Q9 examples.
    """
    print(f"\nUser:")
    print(f"{user_input}")
    print(f"Detected Intent:")
    print(f"{detected_intent}")
