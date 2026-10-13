"""
input_module.py
Part A: User Profile Collection (Q1, Q2)
Experiment 4: Personalized Recommendation System
"""


def get_sample_input(profile_type: str = "A") -> dict:
    """
    Return standard sample profiles specified in Experiment 4 lab manual.
    Student A: Arun (Computer Science, AI & Python)
    Student B: Bala (Cybersecurity & Networks)
    """
    if profile_type.upper() == "B":
        return {
            "name": "Bala",
            "age": 21,
            "background": "Information Technology",
            "interests": ["Cybersecurity", "Networks", "Ethical Hacking"],
            "skill_level": "Beginner",
            "preference": "Practical hands-on labs",
            "goal": "Become a Security Analyst",
            "num_recommendations": 5
        }
    return {
        "name": "Arun",
        "age": 20,
        "background": "Computer Science",
        "interests": ["Artificial Intelligence", "Python"],
        "skill_level": "Beginner",
        "preference": "Practical learning",
        "goal": "Learn AI",
        "num_recommendations": 5
    }


def collect_user_input() -> dict:
    """
    Interactively collect user profile details with preset shortcuts and custom inputs.
    """
    print("\n--- Part A: User Profile Collection ---")
    print("Select Profile Option:")
    print("  [1] Student A (Arun: AI & Python) [Default - Press Enter]")
    print("  [2] Student B (Bala: Cybersecurity & Networks)")
    print("  [3] Custom User Profile")

    choice = input("\nEnter choice [1/2/3] (Default 1): ").strip()

    if choice == "2":
        profile = get_sample_input("B")
        print("\nLoaded Student B profile successfully!")
        return profile
    elif choice == "3":
        print("\nEnter custom profile details:")
        name = input("Name [Default: Arun]: ").strip() or "Arun"
        age_str = input("Age [Default: 20]: ").strip() or "20"
        try:
            age = int(age_str)
        except ValueError:
            age = 20

        background = input("Educational/Professional background [Default: Computer Science]: ").strip() or "Computer Science"
        interests_raw = input("Interests (comma-separated) [Default: Artificial Intelligence, Python]: ").strip()
        if interests_raw:
            interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
        else:
            interests = ["Artificial Intelligence", "Python"]

        skill_level = input("Skill level (Beginner/Intermediate/Advanced) [Default: Beginner]: ").strip() or "Beginner"
        preference = input("Preferred category/type [Default: Practical learning]: ").strip() or "Practical learning"
        goal = input("Goal [Default: Learn AI]: ").strip() or "Learn AI"
        num_str = input("Number of recommendations required [Default: 5]: ").strip() or "5"
        try:
            num_recs = int(num_str)
        except ValueError:
            num_recs = 5

        return {
            "name": name,
            "age": age,
            "background": background,
            "interests": interests,
            "skill_level": skill_level,
            "preference": preference,
            "goal": goal,
            "num_recommendations": num_recs
        }
    else:
        profile = get_sample_input("A")
        print("\nLoaded Student A (Default Lab Profile) successfully!")
        return profile


def display_user_profile(profile: dict) -> None:
    """
    Neatly display collected user information as required in Q2.
    """
    print("\nCollected User Profile:")
    print("-" * 35)
    print(f"Name         : {profile.get('name')}")
    print(f"Age          : {profile.get('age')}")
    print(f"Background   : {profile.get('background')}")
    interests_str = ", ".join(profile.get("interests", []))
    print(f"Interests    : {interests_str}")
    print(f"Skill Level  : {profile.get('skill_level')}")
    print(f"Preference   : {profile.get('preference')}")
    print(f"Goal         : {profile.get('goal')}")
    print(f"No. of Items : {profile.get('num_recommendations')}")
    print("-" * 35)
