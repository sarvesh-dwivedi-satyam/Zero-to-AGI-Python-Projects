def generate_squares_matrix():
    squares_list = [x**2 for x in range (1,11)]
    print("Vectorized Matrix Construction Complete.")
    print(f"Squares Sequence (1 to 10): {squares_list}")
if __name__ == '__main__':
    generate_squares_matrix()