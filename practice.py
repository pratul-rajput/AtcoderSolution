import sys

# Fast input
input = sys.stdin.read

# Read all input at once
data = input().split()

# The first item is the number of values (n)
n = int(data[0])

# The rest are the list of integers
values = map(int, data[1:])

# Use a set to find distinct values
distinct_values = set(values)

# Output the number of distinct values
sys.stdout.write(str(len(distinct_values)) + "\n")
