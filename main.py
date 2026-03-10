def interval_scheduling(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
    selected = []
    current_end = float("-inf")

    for start, end in sorted_intervals:
        if start >= current_end:
            selected.append((start, end))
            current_end = end

    return selected


if __name__ == "__main__":
    sample = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print("Intervals:", sample)
    print("Selected:", interval_scheduling(sample))
