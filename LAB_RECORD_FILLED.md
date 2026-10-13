# LAB RECORD - EXPERIMENT 4

| **Ex. No.: 4** | **Personalized Recommendation System** | **REG. NO:** `<REG_NO>` |
| :--- | :---: | ---: |
| **DATE:** `<DATE>` | **24CS2506 – Building Applications using GPT-4** | **MARKS:** `___ / 100` |

---

## Aim:
To develop a personalized recommendation system using GPT-4 that analyzes user preferences and generates, ranks and explains suitable recommendations based on the user's profile, interests, skill level and goals.

## Problem Statement:
Design and develop an intelligent personalized recommendation system using GPT-4. The application should collect user information and preferences, analyze the user's requirements, generate personalized recommendations, rank them according to suitability, provide explanations for the recommendations and refine the results based on user feedback.

---

## Software Requirements:

| Software / Library | Version | Description |
| :--- | :--- | :--- |
| **Python** | `3.10+` | Core programming language |
| **Ollama / GPT-4** | Local / API | Large Language Model AI engines |
| **VS Code** | `1.90+` | Integrated Development Environment |
| **Requests / Urllib** | Standard / `2.28+` | HTTP requests to Ollama and OpenAI APIs |
| **Streamlit** | `1.30+` | Interactive Web Dashboard (Optional GUI) |

---

## Input Parameters:

| Parameters | Description | Sample Input Value |
| :--- | :--- | :--- |
| **Name** | User's full name | `Arun` |
| **Age** | User's age in years | `20` |
| **Background** | Educational or professional background | `Computer Science` |
| **Interests** | Subject areas of interest | `Artificial Intelligence, Python` |
| **Skill Level** | Proficiency level (Beginner/Intermediate/Advanced) | `Beginner` |
| **Preferred Category** | Format or style of learning | `Practical learning` |
| **Goal** | Primary objective or milestone | `Learn AI` |
| **Preferences** | Learning preference | `Practical` |
| **Number of items** | Quantity of recommendations required | `5` |

---

## System Architecture Diagram:

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

## Module Design:

| Module | File | Responsibility |
| :--- | :--- | :--- |
| **Input Module** | `input_module.py` | **Part A (Q1, Q2)**: Reads user profile details and displays collected information neatly. |
| **Profile Module** | `profile_module.py` | **Part B (Q3)**: Analyzes user profile to extract primary & secondary interests, level, goal, and constraints. |
| **Prompt Module** | `prompt_module.py` | **Part C (Q4)**: Constructs structured GPT-4 prompt with user profile, parameters, and expected format. |
| **Recommendation Module** | `recommendation_module.py` | **Part D (Q5)**: Generates personalized recommendations with names, scores (%), and rationale via GPT-4/Ollama/simulation. |
| **Ranking Module** | `ranking_module.py` | **Part E (Q6)**: Sorts recommendations by score in descending order and outputs a clean tabular summary. |
| **Explanation Module** | `explanation_module.py` | **Part F (Q7)**: Generates personalized explanations detailing why each resource fits user profile and goals. |
| **Feedback Module** | `feedback_module.py` | **Part G (Q8)**: Accepts natural language feedback to dynamically adjust and refine recommendation lists. |
| **Intent Module** | `intent_module.py` | **Part H (Q9)**: Classifies user queries into standard intents (`GENERATE_RECOMMENDATION`, `REFINE_RECOMMENDATION`, etc.). |
| **Save Module** | `save_module.py` | **Part I (Q10)**: Persists session summary, profile, rankings, and explanations to `outputs/recommendations.txt`. |
| **Main Integration Module** | `main.py` | **Part I (Q10)**: Integrates all components into an interactive loop with continuous user interaction. |

---

## Implementation Details:
- **GitHub Repository Link:** [https://github.com/Kishore20a/GPT-EX-4](https://github.com/Kishore20a/GPT-EX-4)
- **LinkedIn Post Link:** `<LinkedIn Post Link>`

---

## Theoretical Background & Core Concepts:

### 1. What is a Recommendation System?
A **Recommendation System** is an AI-based system that suggests items, content, products, services, or information to users based on their preferences, interests, previous interactions, or requirements.
- **Netflix** → Movie & TV series recommendations
- **YouTube** → Video suggestions
- **Amazon** → Product recommendations
- **Spotify** → Music & playlist recommendations
- **Online learning platforms** → Course recommendations

### 2. What is Personalized Recommendation?
A personalized recommendation provides different suggestions for different users based on their distinct profiles:
- **Student A** (Interests: Python, AI, Data Science) → *Python Programming, Machine Learning, Data Science Projects*
- **Student B** (Interests: Cybersecurity, Networks, Ethical Hacking) → *Network Security, Ethical Hacking, Cybersecurity Fundamentals*

$$\text{User Profile} \longrightarrow \text{Preferences} \longrightarrow \text{AI Analysis} \longrightarrow \text{Personalized Recommendations}$$

### 3. Why Use Generative AI for Recommendation?
Traditional systems rely on predefined ratings or rigid collaborative filtering matrices. Generative AI understands rich, unstructured natural language descriptions of user goals.

**Key Advantages:**
- Understands nuanced natural language descriptions.
- Analyzes multi-faceted preferences and constraints simultaneously.
- Generates clear, reasoned explanations for every recommendation.
- Interacts conversationally to refine results iteratively.

### 4. Role of GPT-4 in Recommendation Systems:
GPT-4 analyzes complex user profiles, identifies implicit learning goals, generates ranked lists with suitability scores, provides natural-language justifications, and refines results upon conversational feedback.

---

## Step-by-Step Algorithm:

1. **Start** the application.
2. **Collect User Profile (Part A)**: Prompt user for Name, Age, Background, Interests, Skill Level, Preference, Goal, and number of items required.
3. **Analyze Preferences (Part B)**: Parse inputs to extract Primary Interest, Secondary Interest, Skill Level, Goal, and constraints.
4. **Construct Prompt (Part C)**: Assemble structured system prompt combining persona, user parameters, and explicit JSON / list output directives.
5. **Generate Recommendations (Part D)**: Query GPT-4 / Ollama engine to produce tailored recommendations with scores and reasons.
6. **Rank Recommendations (Part E)**: Sort resources by score descending and format as `Rank | Recommendation | Score`.
7. **Generate Explanations (Part F)**: Produce personalized reasoning connecting user goals with the recommended resource.
8. **Demonstrate Feedback Refinement (Part G)**: Accept feedback (e.g., *"I prefer Artificial Intelligence and do not want Web Development resources"*) and update the ranked recommendations.
9. **Detect User Intent (Part H)**: Route queries to predefined intents (`GENERATE_RECOMMENDATION`, `REFINE_RECOMMENDATION`, `SHOW_PROFILE`, `EXPLAIN_RECOMMENDATION`, `SAVE_RECOMMENDATION`, `EXIT`).
10. **Persist Output & Continuous Loop (Part I)**: Save complete report to `outputs/recommendations.txt` and continue session until user exits.
11. **Stop**.

---

## Output Listings & Screenshots:

### 1. Collected User Profile (Part A - Q2):
```text
Collected User Profile:
-----------------------------------
Name         : Arun
Age          : 20
Background   : Computer Science
Interests    : Artificial Intelligence, Python
Skill Level  : Beginner
Preference   : Practical learning
Goal         : Learn AI
No. of Items : 5
-----------------------------------
```

### 2. Preference Analysis (Part B - Q3):
```text
Preference Analysis
------------------------------
Primary Interest   : Artificial Intelligence
Secondary Interest : Python
Skill Level        : Beginner
Goal               : Learn AI
Preference         : Practical learning
------------------------------
```

### 3. Constructed GPT-4 Prompt (Part C - Q4):
```text
You are a personalized recommendation assistant.

User:
Name: Arun
Background: Computer Science
Interests: Artificial Intelligence, Python
Skill Level: Beginner
Goal: Learn AI
Preference: Practical learning

Recommend 5 suitable learning resources.

For each recommendation provide:
1. Name
2. Reason
3. Suitability score (e.g. 95%)
```

### 4. Generated Recommendations (Part D - Q5):
```text
PERSONALIZED RECOMMENDATIONS
------------------------------------

1. Python for AI
   Score: 95%
   Reason:
   Matches Python and AI interests with hands-on practical focus.

2. Machine Learning Basics
   Score: 92%
   Reason:
   Suitable foundation for beginner AI learners.

3. Generative AI
   Score: 88%
   Reason:
   Relevant to current AI interests and modern LLM application building.

4. Data Science with Python
   Score: 85%
   Reason:
   Combines Python and data analysis required for real-world AI pipelines.

5. Deep Learning Basics
   Score: 80%
   Reason:
   Natural progression after mastering basic machine learning concepts.
```

### 5. Recommendation Ranking (Part E - Q6):
```text
RECOMMENDATION RANKING
-----------------------------------
Rank | Recommendation           | Score
-----+--------------------------+------
1    | Python for AI            | 95%  
2    | Machine Learning Basics  | 92%  
3    | Generative AI            | 88%  
4    | Data Science with Python | 85%  
5    | Deep Learning Basics     | 80%  
```

### 6. Recommendation Explanations (Part F - Q7):
```text
* Resource    : Python for AI
  Explanation : 'Python for AI' was selected for Arun because it directly supports their goal to 'Learn AI' and matches their specified interests [Artificial Intelligence, Python]. As a Beginner-level resource with practical orientation, it provides immediate hands-on value. Core justification: Matches Python and AI interests with hands-on practical focus.

* Resource    : Machine Learning Basics
  Explanation : 'Machine Learning Basics' was selected for Arun because it directly supports their goal to 'Learn AI' and matches their specified interests [Artificial Intelligence, Python]. As a Beginner-level resource with practical orientation, it provides immediate hands-on value. Core justification: Suitable foundation for beginner AI learners.
```

### 7. User Feedback & Refinement (Part G - Q8):
```text
User Feedback:
"I prefer Artificial Intelligence and do not want Web Development resources."

Updated Recommendations after Feedback:
Rank | Recommendation          | Score
-----+-------------------------+------
1    | Artificial Intelligence | 98%  
2    | Machine Learning        | 95%  
3    | Deep Learning           | 93%  
4    | Generative AI           | 90%  
5    | Computer Vision         | 86%  
```

### 8. Intelligent Intent Detection (Part H - Q9):
```text
User: Recommend some AI courses.
Detected Intent: GENERATE_RECOMMENDATION

User: Give me more beginner-friendly options.
Detected Intent: REFINE_RECOMMENDATION

User: Why did you recommend this course?
Detected Intent: EXPLAIN_RECOMMENDATION
```

### 9. File Persistence (Part I - Q10):
```text
Recommendation Saved Successfully to: outputs/recommendations.txt
```

---

## Result:
Thus, a personalized recommendation system using GPT-4 was successfully developed and evaluated. The system accurately collects user profile information, analyzes preferences, constructs targeted prompts, generates, ranks, and explains personalized learning recommendations, dynamically refines outputs through natural language feedback, detects user intents, and persists reports.
