import math

def can_reach_candy_shop(x, y, u, v, t):
    # Calculate the Euclidean distance between (x, y) and (u, v)
    distance = math.sqrt((u - x)**2 + (v - y)**2)
    
    # Check if Tony can reach the candy shop in time
    if distance <= t:
        return "YES"
    else:
        return "NO"

def main():
    # Read the number of scenarios
    N = int(input().strip())
    
    results = []
    
    # Process each scenario
    for _ in range(N):
        # Read x, y, u, v, t for each scenario
        x, y, u, v, t = map(int, input().strip().split())
        
        # Check if Tony can reach the candy shop
        result = can_reach_candy_shop(x, y, u, v, t)
        results.append(result)
    
    # Output results for each scenario
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
