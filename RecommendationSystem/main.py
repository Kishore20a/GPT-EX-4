"""
24CS2506 – Building Applications using GPT-4
Experiment 4: Personalized Recommendation System

Part I - Complete Personalized Recommendation System (Q10)
Integrates all required modules:
- Part A: User Profile Collection (input_module.py)
- Part B: User Preference Analysis (profile_module.py)
- Part C: Prompt Construction (prompt_module.py)
- Part D: Personalized Recommendation Generation (recommendation_module.py)
- Part E: Recommendation Ranking (ranking_module.py)
- Part F: Recommendation Explanation (explanation_module.py)
- Part G: User Feedback & Refinement (feedback_module.py)
- Part H: Intelligent Intent Detection (intent_module.py)
- Part I: Saving & Continuous Interaction (save_module.py & main.py)
"""

import sys
import os

from utils import print_header, print_divider, print_section
from input_module import collect_user_input, display_user_profile, get_sample_input
from profile_module import analyze_preferences, display_preference_analysis
from prompt_module import construct_recommendation_prompt, display_generated_prompt
from recommendation_module import generate_recommendations, display_recommendations
from ranking_module import rank_recommendations, display_ranked_recommendations
from explanation_module import generate_explanations, display_explanations
from feedback_module import refine_recommendations, get_user_feedback
from intent_module import detect_intent, display_detected_intent
from save_module import save_recommendations


def run_experiment_demonstration(profile: dict = None):
    """
    Run complete sequential demonstration covering Part A through Part H
    as specified in the Experiment 4 lab manual.
    """
    print_header("Experiment 4: Personalized Recommendation System")

    # -------------------------------------------------------------
    # Part A: User Profile Collection (Q1, Q2)
    # -------------------------------------------------------------
    if profile is None:
        profile = collect_user_input()
    display_user_profile(profile)

    # -------------------------------------------------------------
    # Part B: User Preference Analysis (Q3)
    # -------------------------------------------------------------
    analysis = analyze_preferences(profile)
    display_preference_analysis(analysis)

    # -------------------------------------------------------------
    # Part C: Prompt Construction (Q4)
    # -------------------------------------------------------------
    prompt = construct_recommendation_prompt(profile, analysis)
    display_generated_prompt(prompt)

    # -------------------------------------------------------------
    # Part D: Recommendation Generation (Q5)
    # -------------------------------------------------------------
    recommendations = generate_recommendations(profile, prompt)
    display_recommendations(recommendations)

    # -------------------------------------------------------------
    # Part E: Recommendation Ranking (Q6)
    # -------------------------------------------------------------
    ranked_recs = rank_recommendations(recommendations)
    display_ranked_recommendations(ranked_recs)

    # -------------------------------------------------------------
    # Part F: Recommendation Explanation (Q7)
    # -------------------------------------------------------------
    explanations = generate_explanations(ranked_recs, profile)
    display_explanations(explanations)

    # -------------------------------------------------------------
    # Part G: User Feedback Demonstration (Q8)
    # -------------------------------------------------------------
    print_section("Part G: User Feedback Demonstration (Q8)")
    sample_feedback = "I prefer Artificial Intelligence and do not want Web Development resources."
    print("Example User Feedback:")
    print(f'"{sample_feedback}"')
    refined_recs = refine_recommendations(profile, prompt, ranked_recs, sample_feedback)
    print("\nUpdated Recommendations after Feedback:")
    display_ranked_recommendations(refined_recs)
    refined_explanations = generate_explanations(refined_recs, profile)

    # -------------------------------------------------------------
    # Part H: Intelligent Intent Detection Demonstration (Q9)
    # -------------------------------------------------------------
    print_section("Part H: Intelligent Intent Detection Demonstration (Q9)")
    demo_queries = [
        "Recommend some AI courses.",
        "Give me more beginner-friendly options.",
        "Why did you recommend this course?"
    ]
    for q in demo_queries:
        intent = detect_intent(q)
        display_detected_intent(q, intent)

    # Save output to recommendations.txt
    save_recommendations(profile, analysis, prompt, refined_recs, refined_explanations)

    return profile, analysis, prompt, refined_recs, refined_explanations


def continuous_interactive_loop(profile: dict, analysis: dict, prompt: str, current_recs: list, explanations: dict):
    """
    Part I (Q10): Continuous interaction loop until user selects Exit.
    """
    print_header("Part I: Continuous Interaction Mode (Q10)")
    print("Commands / Queries accepted:")
    print(" - Recommend some AI courses.        (GENERATE_RECOMMENDATION)")
    print(" - I prefer AI over Web Dev.         (REFINE_RECOMMENDATION)")
    print(" - Why did you recommend this?       (EXPLAIN_RECOMMENDATION)")
    print(" - Show my profile                   (SHOW_PROFILE)")
    print(" - Save recommendations              (SAVE_RECOMMENDATION)")
    print(" - Exit                              (EXIT)\n")

    while True:
        try:
            user_input = input("User > ").strip()
            if not user_input:
                continue

            detected_intent = detect_intent(user_input)
            display_detected_intent(user_input, detected_intent)
            print_divider()

            if detected_intent == "EXIT":
                print("Exiting Personalized Recommendation System. Goodbye!")
                break

            elif detected_intent == "SHOW_PROFILE":
                display_user_profile(profile)
                display_preference_analysis(analysis)

            elif detected_intent == "GENERATE_RECOMMENDATION":
                recs = generate_recommendations(profile, prompt)
                current_recs = rank_recommendations(recs)
                explanations = generate_explanations(current_recs, profile)
                display_ranked_recommendations(current_recs)

            elif detected_intent == "REFINE_RECOMMENDATION":
                current_recs = refine_recommendations(profile, prompt, current_recs, user_input)
                explanations = generate_explanations(current_recs, profile)
                print("\nRefined Recommendations:")
                display_ranked_recommendations(current_recs)

            elif detected_intent == "EXPLAIN_RECOMMENDATION":
                display_explanations(explanations)

            elif detected_intent == "SAVE_RECOMMENDATION":
                save_recommendations(profile, analysis, prompt, current_recs, explanations)

            print_divider()

        except (KeyboardInterrupt, EOFError):
            print("\nExiting system...")
            break


def main():
    # Execute full lab workflow demonstration (Parts A - H + Save)
    profile, analysis, prompt, current_recs, explanations = run_experiment_demonstration()

    # Enter continuous interaction loop (Part I - Q10)
    continuous_interactive_loop(profile, analysis, prompt, current_recs, explanations)


if __name__ == "__main__":
    main()
