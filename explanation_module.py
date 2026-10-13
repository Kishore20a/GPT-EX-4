"""
explanation_module.py
Part F: Recommendation Explanation (Q7)
Experiment 4: Personalized Recommendation System
"""


def generate_explanations(recommendations: list, profile: dict) -> dict:
    """
    Generate tailored explanations for each recommendation describing why it fits
    the user's profile, skill level, and goals.
    """
    name = profile.get("name", "User")
    skill = profile.get("skill_level", "Beginner")
    goal = profile.get("goal", "Learn AI")
    interests_str = ", ".join(profile.get("interests", []))

    explanations = {}
    for item in recommendations:
        item_name = item.get("name", "Resource")
        reason = item.get("reason", "")
        exp = (
            f"'{item_name}' was selected for {name} because it directly supports their goal to '{goal}' "
            f"and matches their specified interests [{interests_str}]. As a {skill}-level resource with practical "
            f"orientation, it provides immediate hands-on value. Core justification: {reason}"
        )
        explanations[item_name] = exp

    return explanations


def display_explanations(explanations: dict) -> None:
    """
    Neatly display generated explanations for all recommendations.
    """
    print("\nRECOMMENDATION EXPLANATIONS")
    print("-" * 55)
    for title, exp in explanations.items():
        print(f"* Resource    : {title}")
        print(f"  Explanation : {exp}\n")
