"""
ranking_module.py
Part E: Recommendation Ranking (Q6)
Experiment 4: Personalized Recommendation System
"""

from utils import format_table


def rank_recommendations(recommendations: list) -> list:
    """
    Sort recommendations by score descending and assign rank (1, 2, 3...).
    """
    def parse_score(val):
        try:
            return float(str(val).replace("%", "").strip())
        except (ValueError, TypeError):
            return 0.0

    sorted_recs = sorted(recommendations, key=lambda x: parse_score(x.get("score", 0)), reverse=True)
    ranked = []
    for idx, item in enumerate(sorted_recs, start=1):
        item_copy = dict(item)
        item_copy["rank"] = idx
        ranked.append(item_copy)
    return ranked


def display_ranked_recommendations(ranked_recommendations: list) -> None:
    """
    Display ranked recommendations matching the table format in Part E Q6.
    """
    headers = ["Rank", "Recommendation", "Score"]
    rows = []
    for item in ranked_recommendations:
        score_val = str(item.get('score', 0)).replace('%', '').strip()
        rows.append([str(item.get('rank', '-')), item.get('name', 'N/A'), f"{score_val}%"])

    print("\nRECOMMENDATION RANKING")
    print("-" * 35)
    print(format_table(headers, rows))
    print()
