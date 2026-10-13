"""
prompt_module.py
Part C: GPT-4 Prompt Construction (Q4)
Experiment 4: Personalized Recommendation System
"""


def construct_recommendation_prompt(profile: dict, analysis: dict) -> str:
    """
    Construct a suitable GPT-4 prompt using the collected user information.
    Includes user profile, interests, skill level, goal, preferences, and count.
    """
    interests_str = ", ".join(profile.get("interests", []))
    num_recs = profile.get("num_recommendations", 5)

    prompt = f"""You are a personalized recommendation assistant.

User:
Name: {profile.get('name', 'User')}
Background: {profile.get('background', 'Computer Science')}
Interests: {interests_str}
Skill Level: {profile.get('skill_level', 'Beginner')}
Goal: {profile.get('goal', 'Learn AI')}
Preference: {profile.get('preference', 'Practical learning')}

Recommend {num_recs} suitable learning resources.

For each recommendation provide:
1. Name
2. Reason
3. Suitability score (e.g. 95%)
"""
    return prompt


def display_generated_prompt(prompt: str) -> None:
    """Display the constructed GPT-4 prompt neatly."""
    print("\n--- Part C: Prompt Construction ---")
    print(prompt.strip())
    print("-" * 55)
