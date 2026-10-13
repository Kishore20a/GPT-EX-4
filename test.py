"""
test.py
Automated end-to-end verification script for Experiment 4.
Validates all modules (Parts A to I, Q1 to Q10).
"""

import os
import sys

# Ensure UTF-8 output on Windows consoles if available
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from input_module import get_sample_input
from profile_module import analyze_preferences
from prompt_module import construct_recommendation_prompt
from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations
from explanation_module import generate_explanations
from feedback_module import refine_recommendations
from intent_module import detect_intent
from save_module import save_recommendations


def run_tests():
    print("Running verification tests for Experiment 4...\n")

    # 1. Test Part A: User Profile Collection
    profile_a = get_sample_input("A")
    assert profile_a["name"] == "Arun", "Profile name should be Arun"
    assert "Artificial Intelligence" in profile_a["interests"], "AI interest missing"
    print("[PASS] Part A (Q1, Q2): User Profile Collection passed.")

    # 2. Test Part B: Preference Analysis
    analysis = analyze_preferences(profile_a)
    assert analysis["primary_interest"] == "Artificial Intelligence"
    assert analysis["skill_level"] == "Beginner"
    print("[PASS] Part B (Q3): User Preference Analysis passed.")

    # 3. Test Part C: Prompt Construction
    prompt = construct_recommendation_prompt(profile_a, analysis)
    assert "Arun" in prompt and "Artificial Intelligence" in prompt
    print("[PASS] Part C (Q4): Prompt Construction passed.")

    # 4. Test Part D: Recommendation Generation
    recs = generate_recommendations(profile_a, prompt)
    assert len(recs) == 5, f"Expected 5 recommendations, got {len(recs)}"
    assert recs[0]["name"] == "Python for AI"
    print("[PASS] Part D (Q5): Recommendation Generation passed.")

    # 5. Test Part E: Recommendation Ranking
    ranked = rank_recommendations(recs)
    assert ranked[0]["rank"] == 1
    assert ranked[0]["score"] >= ranked[-1]["score"]
    print("[PASS] Part E (Q6): Recommendation Ranking passed.")

    # 6. Test Part F: Recommendation Explanation
    explanations = generate_explanations(ranked, profile_a)
    assert len(explanations) == 5
    assert "Python for AI" in explanations
    print("[PASS] Part F (Q7): Recommendation Explanation passed.")

    # 7. Test Part G: Feedback Refinement
    feedback = "I prefer Artificial Intelligence and do not want Web Development resources."
    refined = refine_recommendations(profile_a, prompt, ranked, feedback)
    assert len(refined) == 5
    assert refined[0]["name"] == "Artificial Intelligence"
    print("[PASS] Part G (Q8): User Feedback & Refinement passed.")

    # 8. Test Part H: Intent Detection
    assert detect_intent("Recommend some AI courses.") == "GENERATE_RECOMMENDATION"
    assert detect_intent("Give me more beginner-friendly options.") == "REFINE_RECOMMENDATION"
    assert detect_intent("Why did you recommend this course?") == "EXPLAIN_RECOMMENDATION"
    assert detect_intent("Show my profile") == "SHOW_PROFILE"
    assert detect_intent("Save recommendations") == "SAVE_RECOMMENDATION"
    assert detect_intent("Exit") == "EXIT"
    print("[PASS] Part H (Q9): Intelligent Intent Detection passed.")

    # 9. Test Part I: Persistence
    output_path = save_recommendations(profile_a, analysis, prompt, refined, explanations)
    assert os.path.exists(output_path), "File does not exist"
    print("[PASS] Part I (Q10): File Persistence passed.")

    print("\nALL 10 MODULES / QUESTIONS VERIFIED SUCCESSFULLY!")


if __name__ == "__main__":
    run_tests()
