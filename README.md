# Interval Scheduling

## Complexity

- Best: O(n log n)
- Worst: O(n log n)
- Avg: O(n log n)
- Space: O(n)

## Problem Description

Interval scheduling selects the largest possible set of mutually compatible intervals. Two intervals are compatible when one starts at or after the other finishes, so the goal is to keep as many intervals as possible without introducing overlaps.

This implementation uses the standard greedy rule: sort by finishing time and always take the next interval that finishes earliest among the remaining compatible choices. That rule is important because the interval that ends sooner leaves more room for later intervals, which is exactly what helps the algorithm build an optimal schedule.

## Code

```javascript
/**
 * Select a maximum-size set of compatible intervals with the greedy finish-time rule.
 *
 * @param {Array<[number, number]>} intervals Input intervals as [start, end] pairs.
 * @returns {Array<[number, number]>} Selected non-overlapping intervals.
 */
function intervalScheduling(intervals) {
    const sortedIntervals = [...intervals].sort((a, b) => a[1] - b[1]);

    if (sortedIntervals.length === 0) {
        return [];
    }

    const compatible = [sortedIntervals[0]];
    let finishTime = sortedIntervals[0][1];

    for (let index = 1; index < sortedIntervals.length; index++) {
        const currentInterval = sortedIntervals[index];

        // Keep the interval only if it starts after or when the last one finishes.
        if (currentInterval[0] >= finishTime) {
            compatible.push(currentInterval);
            finishTime = currentInterval[1];
        }
    }

    return compatible;
}

/**
 * Convert interval pairs into a readable string for console output.
 *
 * @param {Array<[number, number]>} intervals Interval list.
 * @returns {string} Formatted interval string.
 */
function formatIntervals(intervals) {
    return intervals.map(([start, end]) => `[${start}, ${end}]`).join(", ");
}

/**
 * Run the interval-scheduling demonstration.
 *
 * @returns {void}
 */
function main() {
    const times = [
        [1, 4],
        [3, 5],
        [0, 6],
        [5, 7],
        [3, 9],
        [5, 9],
        [6, 10],
        [8, 11],
        [8, 12],
        [2, 14],
        [12, 16],
    ];

    console.log(`Original intervals = ${formatIntervals(times)}`);
    console.log(`Compatible intervals = ${formatIntervals(intervalScheduling(times))}`);
}

main();
```

## Algorithm Steps

1. Sort the intervals by finishing time in ascending order.
2. Select the first interval in that sorted order.
3. Track the finish time of the most recently selected interval.
4. Scan the remaining intervals from left to right.
5. Whenever the current interval starts at or after the stored finish time, add it to the solution and update the stored finish time.
6. Return the full list of selected intervals after the scan completes.

## Explanation

The greedy choice is correct because selecting the interval with the earliest finish time leaves as much room as possible for later intervals. If an interval finishes earlier, it cannot block more future choices than an interval that finishes later. That is why sorting by finishing time gives the correct rule for building a maximum-size compatible set.

Once the intervals are sorted, the algorithm is straightforward. It keeps the first interval, stores its finish time, and then scans the remaining intervals from left to right. Whenever the next interval starts at or after the stored finish time, that interval is compatible with everything selected so far, so it is added to the result and its finish time becomes the new boundary.

Sorting dominates the runtime, so the total time complexity is `O(n log n)`. The scan itself is only `O(n)`. This JavaScript implementation returns a new list of selected intervals, so the extra space used for the result is `O(n)` in the worst case.
