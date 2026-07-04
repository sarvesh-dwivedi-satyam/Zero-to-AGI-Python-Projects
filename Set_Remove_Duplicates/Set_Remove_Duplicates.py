def remove_duplicate_name():
    raw_name = ["Satyam", "Amit", "Rahul", "Satyam", "Amit", "Vijay"]
    print(f"Raw Dataset: {raw_name}")
    clean_names = list(set(raw_name))
    print(f"Deduplicated Dataset: {clean_names}")
if __name__ == '__main__':
    remove_duplicate_name()