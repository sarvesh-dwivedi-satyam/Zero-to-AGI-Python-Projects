def track_skill_gap():
    required_skills = {"Python", "AI", "Git", "Machine Learning", "Docker"}
    acquired_skills = {"Python", "Git"}
    pending_skills = required_skills.difference(acquired_skills)
    print(f"Target Roadmap: {required_skills}")
    print(f"Mastered Assets: {acquired_skills}")
    print(f"Delta To Achieve (Pending): {pending_skills}")
if __name__ == '__main__':
    track_skill_gap()