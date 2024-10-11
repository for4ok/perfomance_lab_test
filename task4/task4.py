import sys


def read_numbers(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]


def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <numbers_file>")
        return

    numbers_file = sys.argv[1]
    nums = read_numbers(numbers_file)
    moves = min_moves(nums)
    print(moves)


if __name__ == "__main__":
    main()
