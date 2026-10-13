"""
profile_module.py
Part B: User Preference Analysis (Q3)
Experiment 4: Personalized Recommendation System
"""


def analyze_preferences(profile: dict) -> dict:
    """
    Analyze the user profile and identify:
    - Primary interest
    - Secondary interest
    - Skill level
    - Learning goal
    - Preferred type
    - Important constraints
    """
    interests = profile.get("interests", [])
    primary_interest = interests[0] if len(interests) > 0 else "General Computing"
    secondary_interest = interests[1] if len(interests) > 1 else (interests[0] if interests else "Programming")

    analysis = {
        "primary_interest": primary_interest,
        "secondary_interest": secondary_interest,
        "skill_level": profile.get("skill_level", "Beginner"),
        "goal": profile.get("goal", "Skill Acquisition"),
        "preference": profile.get("preference", "Practical learning"),
        "constraints": f"Tailored for {profile.get('skill_level')} level in {profile.get('background', 'Computing')} focusing on {profile.get('preference', 'Practical')}"
    }
    return analysis


def display_preference_analysis(analysis: dict) -> None:
    """
    Display preference analysis results matching the sample output in Q3.
    """
    print("\nPreference Analysis")
    print("-" * 30)
    print(f"Primary Interest   : {analysis.get('primary_interest')}")
    print(f"Secondary Interest : {analysis.get('secondary_interest')}")
    print(f"Skill Level        : {analysis.get('skill_level')}")
    print(f"Goal               : {analysis.get('goal')}")
    print(f"Preference         : {analysis.get('preference')}")
    print("-" * 30)
