def analyze_tuple_stats():
    data_stream = (45, 12, 89, 7, 34, 66)
    lowest = min(data_stream)
    highest = max(data_stream)
    print(f"📉 Minimum Value: {lowest}")
    print(f"📈 Maximum Value: {highest}")
if __name__ == '__main__':
    analyze_tuple_stats()