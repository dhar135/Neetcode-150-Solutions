# NeetCode 150 Solutions

This repository contains my solutions to the NeetCode 150 coding problems (https://neetcode.io/practice). The project is structured to provide clean, tested, and well-documented solutions for each problem.

## Project Structure

```
neetcode150/
├── src/               # Source code for solutions
│   ├── arrays_and_hashing/
│   ├── two_pointers/
│   ├── sliding_window/
│   └── ...
└── tests/            # Test cases for solutions
    ├── arrays_and_hashing/
    ├── two_pointers/
    └── ...
```

## Problem Categories

- Arrays & Hashing (0/9)
- Two Pointers (0/5)
- Sliding Window (0/6)
- Stack (0/7)
- Binary Search (0/7)
- Linked List (0/11)
- Trees (0/15)
- Tries (0/3)
- Heap / Priority Queue (0/7)
- Backtracking (0/9)
- Graphs (0/13)
- Advanced Graphs (0/6)
- 1-D Dynamic Programming (0/12)
- 2-D Dynamic Programming (0/11)
- Greedy (0/8)
- Intervals (0/6)
- Math & Geometry (0/8)
- Bit Manipulation (0/7)

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Testing

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src
```

Run tests for a specific category:
```bash
pytest tests/arrays_and_hashing/
```

## Solution Template

Each solution file follows this template:

```python
"""
Problem: [Problem Name]
Difficulty: [Easy/Medium/Hard]
Link: [LeetCode Problem URL]

Approach:
1. [Step 1]
2. [Step 2]
...

Time Complexity: O(?)
Space Complexity: O(?)
"""

def solution_function():
    # Implementation
    pass
```

## Progress Tracking

- [ ] Arrays & Hashing
  - [ ] Contains Duplicate
  - [ ] Valid Anagram
  - [ ] Two Sum
  ...

## Contributing

Feel free to submit issues and enhancement requests!

## Resources

- [NeetCode.io](https://neetcode.io/)
- [LeetCode](https://leetcode.com/)
- [Python Documentation](https://docs.python.org/3/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Donovan Harrison

## Acknowledgments

- NeetCode for the curated list of problems
- The Python community for excellent tools and frameworks