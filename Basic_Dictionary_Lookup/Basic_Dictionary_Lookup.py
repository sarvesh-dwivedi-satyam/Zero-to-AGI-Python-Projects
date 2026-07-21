def lookup_tech_term():
    tech_lexicon = {
        "python": "A high-level interpreted programming language powering modern AI.",
        "loop": "A control structure that repeats a block of code until a condition is met.",
        "variable": "A named memory location used to store dynamic data values.",
        "algorithm": "A set of step-by-step instructions to solve a specific problem."
    }
    query_term = input("Enter term to search (e.g., python, loop): ").strip().lower()
    definition = tech_lexicon.get(query_term, "Term not found in the tech lexicon database.")
    print(f"Term: {query_term.title()}")
    print(f"Definition: {definition}")
if __name__ == '__main__':
    lookup_tech_term()