"""
app.py
Streamlit Interactive Web Application for Experiment 4: Personalized Recommendation System.
Course: 24CS2506 – Building Applications using GPT-4
"""

import os
import sys
import json
import pandas as pd
import streamlit as st

# Import core lab modules
from input_module import get_sample_input
from profile_module import analyze_preferences
from prompt_module import construct_recommendation_prompt
from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations
from explanation_module import generate_explanations
from feedback_module import refine_recommendations
from intent_module import detect_intent
from save_module import save_recommendations
from utils import check_ollama_status

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="Personalized Recommendation System • GPT-4",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# Custom CSS (Glassmorphic Theme & Rich Aesthetics)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }
    
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 20%, #a855f7 60%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .hero-subtitle {
        color: #94a3b8;
        font-size: 14px;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    .metric-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    
    .metric-value {
        font-size: 22px;
        font-weight: 700;
        color: #38bdf8;
    }
    
    .metric-label {
        font-size: 12px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 4px;
    }
    
    .intent-pill {
        display: inline-block;
        background: rgba(168, 85, 247, 0.2);
        color: #c084fc;
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 6px 14px;
        border-radius: 9999px;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# Header
# ==============================================================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">🎯 Experiment 4: Personalized Recommendation System</div>
    <div class="hero-subtitle">Course: 24CS2506 – Building Applications using GPT-4 • Modular Lab Implementation (Parts A to I)</div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# Sidebar: User Profile & Configuration
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Profile Configuration")

    profile_choice = st.selectbox(
        "📌 Select Preset Profile",
        ["Student A (Arun - AI & Python)", "Student B (Bala - Cybersecurity)", "Custom User Profile"],
        index=0
    )

    if "Student A" in profile_choice:
        default_prof = get_sample_input("A")
    elif "Student B" in profile_choice:
        default_prof = get_sample_input("B")
    else:
        default_prof = {
            "name": "Custom Learner",
            "age": 22,
            "background": "Software Engineering",
            "interests": ["Machine Learning", "Cloud Computing"],
            "skill_level": "Intermediate",
            "preference": "Project-based",
            "goal": "Build End-to-End AI Apps",
            "num_recommendations": 5
        }

    # Input form
    name = st.text_input("Name", default_prof["name"])
    col_a, col_b = st.columns(2)
    with col_a:
        age = st.number_input("Age", min_value=15, max_value=80, value=int(default_prof["age"]))
    with col_b:
        num_recs = st.number_input("No. of Items", min_value=1, max_value=10, value=int(default_prof["num_recommendations"]))

    background = st.text_input("Background / Field", default_prof["background"])
    interests_str = st.text_input("Interests (comma-separated)", ", ".join(default_prof["interests"]))
    interests = [i.strip() for i in interests_str.split(",") if i.strip()]

    skill_level = st.selectbox(
        "Skill Level",
        ["Beginner", "Intermediate", "Advanced"],
        index=["Beginner", "Intermediate", "Advanced"].index(default_prof["skill_level"]) if default_prof["skill_level"] in ["Beginner", "Intermediate", "Advanced"] else 0
    )

    preference = st.text_input("Preference / Type", default_prof["preference"])
    goal = st.text_input("Learning Goal", default_prof["goal"])

    # Construct active profile dictionary
    active_profile = {
        "name": name,
        "age": age,
        "background": background,
        "interests": interests,
        "skill_level": skill_level,
        "preference": preference,
        "goal": goal,
        "num_recommendations": num_recs
    }

    st.markdown("---")
    st.header("🔌 AI Engine Settings")
    engine_choice = st.selectbox(
        "AI Recommendation Engine",
        ["Smart Deterministic Engine (Lab Spec)", "Local Ollama LLM", "OpenAI GPT-4 API"],
        index=0
    )

    ollama_info = check_ollama_status()
    if ollama_info["online"]:
        st.success(f"🟢 Ollama Online ({len(ollama_info['models'])} models)")
    else:
        st.info("💡 Running in Simulation / Lab Mode (100% Offline Compatible)")

# Compute analysis & prompt
analysis = analyze_preferences(active_profile)
prompt = construct_recommendation_prompt(active_profile, analysis)

# Initialize Session State
if "recommendations" not in st.session_state:
    raw_recs = generate_recommendations(active_profile, prompt)
    st.session_state.recommendations = rank_recommendations(raw_recs)
    st.session_state.explanations = generate_explanations(st.session_state.recommendations, active_profile)

if "feedback_history" not in st.session_state:
    st.session_state.feedback_history = []

# ==============================================================================
# Main Navigation Tabs
# ==============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Recommendation Studio",
    "🔄 Feedback & Refinement",
    "🧠 Intent Detection",
    "📝 Prompt Inspector",
    "📚 Theory & Lab Guide"
])

# ------------------------------------------------------------------------------
# TAB 1: Recommendation Studio
# ------------------------------------------------------------------------------
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{active_profile["name"]}</div><div class="metric-label">Learner</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{analysis["primary_interest"]}</div><div class="metric-label">Primary Interest</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{active_profile["skill_level"]}</div><div class="metric-label">Skill Level</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{active_profile["goal"]}</div><div class="metric-label">Goal</div></div>', unsafe_allow_html=True)

    st.markdown("###")
    
    col_btn, col_save = st.columns([1, 1])
    with col_btn:
        if st.button("✨ Generate Personalized Recommendations", use_container_width=True, type="primary"):
            raw_recs = generate_recommendations(active_profile, prompt)
            st.session_state.recommendations = rank_recommendations(raw_recs)
            st.session_state.explanations = generate_explanations(st.session_state.recommendations, active_profile)
            st.success("Recommendations successfully generated and ranked!")

    st.subheader("📊 Ranked Recommendations Table (Part E - Q6)")
    
    df_data = []
    for item in st.session_state.recommendations:
        score_clean = int(str(item.get("score", 0)).replace("%", "").strip())
        df_data.append({
            "Rank": item.get("rank"),
            "Recommendation": item.get("name"),
            "Suitability Score (%)": score_clean,
            "Reason": item.get("reason")
        })
    df = pd.DataFrame(df_data)
    
    st.dataframe(
        df,
        column_config={
            "Suitability Score (%)": st.column_config.ProgressColumn(
                "Suitability Score (%)",
                format="%d%%",
                min_value=0,
                max_value=100
            ),
        },
        use_container_width=True,
        hide_index=True
    )

    st.subheader("💡 Recommendation Explanations (Part F - Q7)")
    for item in st.session_state.recommendations:
        r_name = item.get("name")
        r_score = item.get("score")
        r_reason = item.get("reason")
        exp = st.session_state.explanations.get(r_name, r_reason)
        
        with st.expander(f"📌 Rank {item.get('rank')}: {r_name} (Score: {r_score}%)"):
            st.markdown(f"**Direct Justification:** {r_reason}")
            st.info(f"**Personalized Explanation:**\n{exp}")

    # Export / Save report section
    st.markdown("---")
    report_file = save_recommendations(active_profile, analysis, prompt, st.session_state.recommendations, st.session_state.explanations)
    with open(report_file, "r", encoding="utf-8") as f:
        report_content = f.read()

    st.download_button(
        label="📥 Download Full Recommendations Report (.txt)",
        data=report_content,
        file_name="recommendations.txt",
        mime="text/plain",
        use_container_width=True
    )

# ------------------------------------------------------------------------------
# TAB 2: Feedback & Refinement
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("🔄 Feedback-Based Recommendation Refinement (Part G - Q8)")
    st.write("Demonstrates dynamic personalization through natural language user interaction.")

    sample_fbs = [
        "I am more interested in AI than Web Development.",
        "I prefer Artificial Intelligence and do not want Web Development resources.",
        "Give me more beginner-friendly options."
    ]

    st.write("**Quick Test Feedback Presets:**")
    fb_cols = st.columns(3)
    preset_clicked = None
    for i, col in enumerate(fb_cols):
        with col:
            if st.button(sample_fbs[i], key=f"fb_btn_{i}", use_container_width=True):
                preset_clicked = sample_fbs[i]

    custom_fb = st.text_input("Or enter custom feedback:", value=preset_clicked or "")

    if st.button("🚀 Apply Feedback & Refine Recommendations", type="primary"):
        if custom_fb.strip():
            refined = refine_recommendations(active_profile, prompt, st.session_state.recommendations, custom_fb)
            st.session_state.recommendations = refined
            st.session_state.explanations = generate_explanations(refined, active_profile)
            st.session_state.feedback_history.append(custom_fb)
            st.success(f"Recommendations updated based on feedback: '{custom_fb}'")
            st.rerun()

    st.markdown("### Current Active Recommendations:")
    for item in st.session_state.recommendations:
        st.write(f"**{item.get('rank')}. {item.get('name')}** — *{item.get('score')}%* ({item.get('reason')})")

# ------------------------------------------------------------------------------
# TAB 3: Intent Detection Playground
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🧠 Intelligent Intent Detection (Part H - Q9)")
    st.write("Use NLP pattern matching and GPT-4 classification to detect the user's intent from natural-language queries.")

    intent_examples = [
        "Recommend some AI courses.",
        "Give me more beginner-friendly options.",
        "Why did you recommend this course?",
        "Show my profile details",
        "Save recommendations to file",
        "Exit"
    ]

    st.write("**Sample Queries from Lab Manual:**")
    int_cols = st.columns(3)
    query_preset = None
    for i, q in enumerate(intent_examples):
        col = int_cols[i % 3]
        with col:
            if st.button(q, key=f"q_btn_{i}", use_container_width=True):
                query_preset = q

    user_q = st.text_input("Enter natural language query to test:", value=query_preset or "Recommend some AI courses.")
    detected = detect_intent(user_q)

    st.markdown("### Detection Result:")
    st.markdown(f'<div class="intent-pill">Detected Intent: {detected}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("**Supported Intents Reference Table:**")
    st.table(pd.DataFrame([
        {"Intent": "GENERATE_RECOMMENDATION", "Trigger Example": "Recommend some AI courses.", "System Action": "Generates fresh recommendation list."},
        {"Intent": "REFINE_RECOMMENDATION", "Trigger Example": "Give me more beginner-friendly options.", "System Action": "Refines recommendations via feedback."},
        {"Intent": "EXPLAIN_RECOMMENDATION", "Trigger Example": "Why did you recommend this course?", "System Action": "Displays detailed explanation & reasons."},
        {"Intent": "SHOW_PROFILE", "Trigger Example": "Show my profile", "System Action": "Displays collected profile and preference analysis."},
        {"Intent": "SAVE_RECOMMENDATION", "Trigger Example": "Save recommendations", "System Action": "Exports report to outputs/recommendations.txt."},
        {"Intent": "EXIT", "Trigger Example": "Exit / Quit", "System Action": "Terminates interaction loop gracefully."}
    ]))

# ------------------------------------------------------------------------------
# TAB 4: Prompt Inspector
# ------------------------------------------------------------------------------
with tab4:
    st.subheader("📝 GPT-4 Prompt Construction (Part C - Q4)")
    st.write("The system converts user profile and preference analysis into a structured prompt:")
    st.code(prompt, language="markdown")

    st.subheader("📊 Structured Components Breakdown")
    st.json({
        "System Role": "Personalized recommendation assistant",
        "User Profile": {
            "Name": active_profile["name"],
            "Background": active_profile["background"],
            "Interests": active_profile["interests"],
            "Skill Level": active_profile["skill_level"],
            "Goal": active_profile["goal"],
            "Preference": active_profile["preference"]
        },
        "Primary Interest": analysis["primary_interest"],
        "Secondary Interest": analysis["secondary_interest"],
        "Output Specification": "Name, Reason, Suitability Score (%)",
        "Quantity Requested": active_profile["num_recommendations"]
    })

# ------------------------------------------------------------------------------
# TAB 5: Theory & Lab Guide
# ------------------------------------------------------------------------------
with tab5:
    st.subheader("📚 Experiment 4: Core Concepts & Viva Reference")

    st.markdown("""
    ### 1. What is a Recommendation System?
    A **Recommendation System** is an AI-based system that suggests items, content, products, services, or information to users based on their preferences, interests, previous interactions, or requirements.
    - **Netflix** → Movie & TV series recommendations
    - **YouTube** → Video recommendations
    - **Amazon** → Product recommendations
    - **Spotify** → Music and playlist recommendations
    - **Online learning platforms** → Course recommendations

    ---

    ### 2. What is Personalized Recommendation?
    A personalized recommendation provides different suggestions for different users based on their individual profiles.
    - **Student A** (Python, AI, Data Science) → *Python Programming, Machine Learning, Data Science Projects*
    - **Student B** (Cybersecurity, Networks, Ethical Hacking) → *Network Security, Ethical Hacking, Cybersecurity Fundamentals*

    $$\\text{User Profile} \\longrightarrow \\text{Preferences} \\longrightarrow \\text{AI Analysis} \\longrightarrow \\text{Personalized Recommendations}$$

    ---

    ### 3. Why Use Generative AI for Recommendation?
    Traditional systems depend on predefined rules, ratings, or similarity calculations. Generative AI can understand rich natural-language descriptions of user goals.

    | Capability | Traditional RecSys | Generative AI RecSys |
    |---|---|---|
    | Natural Language Queries | Limited / Keyword match | Full semantic understanding |
    | Complex Goal Reasoning | Rigid heuristics | Deep contextual inference |
    | Explanations | Template-based / None | Human-like custom rationale |
    | Conversational Refinement | Requires manual filters | Natural conversational dialogue |

    ---

    ### 4. What is GPT-4?
    GPT-4 is a Generative AI language model capable of understanding and generating natural language. In a recommendation application, it analyzes profiles, identifies interests, generates recommendations, explains why items were chosen, and refines them based on feedback.

    ---

    ### 5. Understanding User Profile
    | Parameter | Example Value |
    |---|---|
    | **Name** | Arun |
    | **Age** | 20 |
    | **Field** | Computer Science |
    | **Interests** | AI, Python |
    | **Skill Level** | Beginner |
    | **Preferred Type** | Practical learning |
    | **Goal** | Learn AI |

    ---

    ### 6. Feedback-Based Recommendation
    - **Initial Recommendation:** Python Programming, Machine Learning, Web Development
    - **User Feedback:** *"I am more interested in AI than Web Development."*
    - **Updated Recommendation:** Artificial Intelligence, Machine Learning, Deep Learning, Generative AI, Computer Vision

    ---

    ### 7. Example Expected Output (Lab Specification)
    | Rank | Recommendation | Reason | Score |
    |---|---|---|---|
    | **1** | Python for AI | Matches Python and AI interests | 95% |
    | **2** | Machine Learning Basics | Suitable for beginner AI learners | 92% |
    | **3** | Generative AI | Relevant to current AI interests | 88% |
    | **4** | Data Science with Python | Combines Python and data analysis | 85% |
    | **5** | Deep Learning Basics | Natural progression after ML | 80% |
    """)
