# 🎯 Experiment 4: Personalized Recommendation System

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-24CS2506_Building_Applications_using_GPT--4-orange.svg)]()
[![LLM Engine](https://img.shields.io/badge/LLM-GPT--4_%7C_Ollama-purple.svg)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, modular personalized recommendation system developed for **Experiment 4: Personalized Recommendation System** under course **24CS2506 – Building Applications using GPT-4**.

---

## 📌 Problem Statement
Design and develop a personalized recommendation system using GPT-4. The application collects user information, interests, preferences, and requirements, performs preference analysis, constructs structured LLM prompts, generates personalized recommendations with suitability scores (%) and justification reasons, ranks recommendations, explains suitability, refines results based on natural language user feedback, detects user intent, and persists reports to disk.

---

## 📚 Core Theoretical Concepts

### 1. What is a Recommendation System?
A **Recommendation System** is an AI-based system that suggests items, content, products, services, or information to users based on their preferences, interests, previous interactions, or requirements.

**Examples:**
- **Netflix** → Movie recommendations
- **YouTube** → Video recommendations
- **Amazon** → Product recommendations
- **Spotify** → Music recommendations
- **Online learning platforms** → Course recommendations

**Simple Example:**
- **User Preference:** Interested in Python, Artificial Intelligence, and Data Science.
- **Recommendations:**
  1. Python for Data Science
  2. Machine Learning Fundamentals
  3. Generative AI with Python
  4. Data Analytics using Python
  5. Deep Learning Fundamentals

---

### 2. What is Personalized Recommendation?
A personalized recommendation provides different suggestions for different users.

**Comparison:**
- **Student A**
  - *Interests:* Python, AI, Data Science
  - *Recommendations:* Python Programming, Machine Learning, Data Science Projects
- **Student B**
  - *Interests:* Cybersecurity, Networks, Ethical Hacking
  - *Recommendations:* Network Security, Ethical Hacking, Cybersecurity Fundamentals

$$\text{User Profile} \longrightarrow \text{Preferences} \longrightarrow \text{AI Analysis} \longrightarrow \text{Personalized Recommendations}$$

---

### 3. Why Use Generative AI for Recommendation?
Traditional recommendation systems generally depend on predefined rules, ratings, or similarity calculations. Generative AI can understand natural-language descriptions of user preferences.

**Example User Input:**
> *"I am a beginner who likes programming and wants to learn AI. I prefer practical courses rather than theoretical courses."*

**Key Advantages:**
- Understands natural language descriptions
- Can analyze multi-faceted user preferences
- Generates transparent explanations for recommendations
- Can consider multiple interests simultaneously
- Can personalize recommendations dynamically
- Can interact conversationally with users

---

### 4. Role of GPT-4 in Recommendation Systems
GPT-4 is a Generative AI language model capable of understanding and generating natural language. In a recommendation application, GPT-4 is used to:
- Analyze user preferences
- Identify latent interests and goals
- Understand user constraints
- Generate tailored recommendations
- Explain why an item was recommended
- Refine recommendations based on natural language feedback

---

### 5. Understanding User Profile
A recommendation system requires structured information about the user:

| Parameter | Example Value |
|---|---|
| **Name** | Arun |
| **Age** | 20 |
| **Field / Background** | Computer Science |
| **Interests** | AI, Python |
| **Skill Level** | Beginner |
| **Preferred Type** | Practical learning |
| **Goal** | Learn AI |
| **Number of items** | 5 |

The system converts these inputs into a structured prompt for the LLM.

---

### 6. Feedback-Based Recommendation
The system improves recommendations based on conversational feedback:

- **Initial Recommendations:**
  1. Python Programming
  2. Machine Learning
  3. Web Development
- **User Feedback:**
  > *"I am more interested in AI than Web Development."*
- **Updated Recommendations:**
  1. Artificial Intelligence
  2. Machine Learning
  3. Deep Learning
  4. Generative AI
  5. Computer Vision

---

### 7. Example Expected Output

**User:** Computer Science student  
**Interests:** AI, Python  
**Level:** Beginner  

| Rank | Recommendation | Reason | Score |
|---|---|---|---|
| **1** | Python for AI | Matches Python and AI interests | 95% |
| **2** | Machine Learning Basics | Suitable for beginner AI learners | 92% |
| **3** | Generative AI | Relevant to current AI interests | 88% |
| **4** | Data Science with Python | Combines Python and data analysis | 85% |
| **5** | Deep Learning Basics | Natural progression after ML | 80% |

---

## 🏗️ System Architecture & Workflow

```
+--------------------+      +----------------------+      +-------------------------+
|     User Input     | ---> | User Profile Collect | ---> |   Preference Analysis   |
| (Name, Age, Field) |      |      (Part A)        |      |        (Part B)         |
+--------------------+      +----------------------+      +-------------------------+
                                                                       |
                                                                       v
+--------------------+      +----------------------+      +-------------------------+
| Recommendation Gen | <--- |  GPT-4 / Ollama LLM  | <--- |   Prompt Construction   |
|     (Part D)       |      |      AI Engine       |      |        (Part C)         |
+--------------------+      +----------------------+      +-------------------------+
          |
          v
+--------------------+      +----------------------+      +-------------------------+
| Recommendation     | ---> | Recommendation       | ---> | Natural Language        |
| Ranking (Part E)   |      | Explanation (Part F) |      | Feedback Loop (Part G)  |
+--------------------+      +----------------------+      +-------------------------+
                                                                       |
                                                                       v
+--------------------+      +----------------------+      +-------------------------+
| Save Report File   | <--- | Complete Application | <--- | Intelligent Intent      |
| recommendations.txt|      | Continuous Loop (I)  |      | Detection (Part H)      |
+--------------------+      +----------------------+      +-------------------------+
```

---

## 📁 Suggested Project Structure

```
RecommendationSystem/
│
├── main.py                     # Part I (Q10): Integrated CLI loop
├── input_module.py             # Part A (Q1, Q2): User Profile Collection
├── profile_module.py           # Part B (Q3): User Preference Analysis
├── prompt_module.py            # Part C (Q4): GPT-4 Prompt Construction
├── recommendation_module.py    # Part D (Q5): Recommendation Generation
├── ranking_module.py           # Part E (Q6): Recommendation Ranking
├── explanation_module.py       # Part F (Q7): Recommendation Explanation
├── feedback_module.py          # Part G (Q8): User Feedback & Refinement
├── intent_module.py            # Part H (Q9): Intelligent Intent Detection
├── save_module.py              # Part I (Q10): Report File Persistence
├── utils.py                    # ASCII Tables, Headers, Ollama health checks
│
├── outputs/
│   └── recommendations.txt     # Saved recommendation report
│
└── models/                     # LLM vector & cache storage
```

---

## 🚀 How to Run

1. **Clone or Open Workspace:**
   ```bash
   cd "NEW EX 4"
   ```

2. **Run Interactive Application:**
   ```bash
   python main.py
   ```
   *(Or double-click `run.bat` on Windows)*

3. **Select Profile Option:**
   - Press **`Enter`** (Option 1) to run with default lab sample (**Arun** - Student A).
   - Or press **`2`** for Student B (**Bala** - Cybersecurity).
   - Or press **`3`** for custom profile.

4. **Continuous Interaction Commands:**
   - Type `"Recommend some AI courses."` → Re-generates recommendations
   - Type `"I prefer Artificial Intelligence and do not want Web Development resources."` → Refines recommendations
   - Type `"Why did you recommend this course?"` → Displays explanations
   - Type `"Show my profile"` → Displays current user profile & preference analysis
   - Type `"Save recommendations"` → Saves report to `outputs/recommendations.txt`
   - Type `"Exit"` → Exits the application cleanly.

---

## 📄 Lab Documentation
- Complete filled lab record is available in [`LAB_RECORD_FILLED.md`](LAB_RECORD_FILLED.md).
- Output text file is stored in [`outputs/recommendations.txt`](outputs/recommendations.txt).
