"""
save_module.py
Part I: Report Persistence (Q10)
Experiment 4: Personalized Recommendation System

Persists profile, preference analysis, prompts, recommendations, and explanations
to outputs/recommendations.txt.
"""

import os


def save_recommendations(profile: dict, analysis: dict, prompt: str, recommendations: list, explanations: dict, filepath: str = None) -> str:
    """
    Save all session recommendations and details into outputs/recommendations.txt.
    """
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "outputs")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, "recommendations.txt")
    else:
        output_dir = os.path.dirname(filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

    lines = []
    lines.append("=" * 60)
    lines.append("     PERSONALIZED RECOMMENDATION SYSTEM REPORT")
    lines.append("     Course: 24CS2506 - Building Applications using GPT-4")
    lines.append("=" * 60 + "\n")

    lines.append("1. USER PROFILE")
    lines.append("-" * 50)
    lines.append(f"Name         : {profile.get('name')}")
    lines.append(f"Age          : {profile.get('age')}")
    lines.append(f"Background   : {profile.get('background')}")
    lines.append(f"Interests    : {', '.join(profile.get('interests', []))}")
    lines.append(f"Skill Level  : {profile.get('skill_level')}")
    lines.append(f"Preference   : {profile.get('preference')}")
    lines.append(f"Goal         : {profile.get('goal')}")
    lines.append(f"No. of Items : {profile.get('num_recommendations')}\n")

    lines.append("2. PREFERENCE ANALYSIS")
    lines.append("-" * 50)
    lines.append(f"Primary Interest   : {analysis.get('primary_interest')}")
    lines.append(f"Secondary Interest : {analysis.get('secondary_interest')}")
    lines.append(f"Skill Level        : {analysis.get('skill_level')}")
    lines.append(f"Goal               : {analysis.get('goal')}")
    lines.append(f"Preference         : {analysis.get('preference')}")
    lines.append(f"Important Constraint: {analysis.get('constraints')}\n")

    lines.append("3. RANKED RECOMMENDATIONS")
    lines.append("-" * 50)
    lines.append(f"{'Rank':<6} | {'Recommendation':<32} | {'Score':<8}")
    lines.append("-" * 50)
    for item in recommendations:
        rank = item.get('rank', '-')
        name = item.get('name', '')
        score = f"{str(item.get('score')).replace('%', '')}%"
        lines.append(f"{str(rank):<6} | {name:<32} | {score:<8}")
    lines.append("")

    lines.append("4. RECOMMENDATION DETAILS & EXPLANATIONS")
    lines.append("-" * 50)
    for item in recommendations:
        item_name = item.get('name')
        score = f"{str(item.get('score')).replace('%', '')}%"
        reason = item.get('reason', '')
        exp = explanations.get(item_name, reason)
        lines.append(f"* Resource : {item_name} (Score: {score})")
        lines.append(f"  Reason   : {reason}")
        lines.append(f"  Details  : {exp}\n")

    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nRecommendation Saved Successfully to: {filepath}")
    return filepath
