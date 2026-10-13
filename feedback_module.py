"""
feedback_module.py
Part G: User Feedback & Recommendation Refinement (Q8)
Experiment 4: Personalized Recommendation System
"""

from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations


def get_user_feedback() -> str:
    """
    Prompt the user to provide natural language feedback on current recommendations.
    """
    print("\nPart G - User Feedback")
    print("Example: 'I prefer Artificial Intelligence and do not want Web Development resources.'")
    feedback = input("\nEnter feedback: ").strip()
    return feedback


def refine_recommendations(profile: dict, prompt: str, current_recs: list, feedback_text: str) -> list:
    """
    Refine recommendation list based on user feedback.
    """
    if not feedback_text or not feedback_text.strip():
        return current_recs

    # Generate updated recommendations incorporating user feedback
    refined_recs = generate_recommendations(profile, prompt, feedback=feedback_text)
    ranked_refined = rank_recommendations(refined_recs)
    return ranked_refined
