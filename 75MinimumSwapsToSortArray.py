def minSwaps(arr):
    n = len(arr)

    # Step 1: Store array elements with original indices
    arrpos = [(val, i) for i, val in enumerate(arr)]
    
    # Step 2: Sort by array values
    arrpos.sort(key=lambda x: x[0])

    # Step 3: Track visited elements
    visited = [False] * n
    ans = 0

    # Step 4: Traverse array elements
    for i in range(n):
        # Skip if already visited or already in correct place
        if visited[i] or arrpos[i][1] == i:
            continue

        # Find size of cycle
        cycle_size, j = 0, i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][1]   # Jump to next index
            cycle_size += 1

        # Update answer
        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans

# Example
print(minSwaps([4, 3, 2, 1]))  # Output: 2
