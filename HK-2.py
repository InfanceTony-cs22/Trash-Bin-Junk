def can_stack_cubes(test_cases):
    results = []
    for cubes in test_cases:
        n, blocks = cubes[0], cubes[1]

        left = 0
        right = n - 1
        prev = float('inf')

        while left <= right:
            if blocks[left] >= blocks[right] and blocks[left] <= prev:
                prev = blocks[left]
                left += 1
            elif blocks[right] >= blocks[left] and blocks[right] <= prev:
                prev = blocks[right]
                right -= 1
            else:
                results.append("No")
                break
        else:
            results.append("Yes")

    return results

if __name__ == '__main__':
    t = int(input().strip())
    test_cases = []
    
    for _ in range(t):
        n = int(input().strip())
        blocks = list(map(int, input().split()))
        test_cases.append((n, blocks))
    
    results = can_stack_cubes(test_cases)
    for result in results:
        print(result)
