#!/bin/bash

# Usage:
# ./new_problem.sh 1342 number_of_steps_to_reduce_a_number_to_zero

if [ "$#" -ne 2 ]; then
    echo "Usage: ./new_problem.sh <problem_number> <slug_with_underscores>"
    exit 1
fi

PROBLEM_NUMBER=$1
SLUG=$2

FOLDER="problems/lc${PROBLEM_NUMBER}_${SLUG}"

if [ -d "$FOLDER" ]; then
    echo "Directory already exists: $FOLDER"
    exit 1
fi

mkdir -p "$FOLDER"

touch "$FOLDER/__init__.py"

# ---------------- solution.py ----------------
cat > "$FOLDER/solution.py" <<EOF
class Solution:
    def solve(self, *args):
        """
        Replace method name and logic with actual LeetCode solution.
        """
        pass


if __name__ == "__main__":
    s = Solution()
    print("Manual run example:")
    print(s.solve())
EOF

# ---------------- description.txt ----------------
cat > "$FOLDER/description.txt" <<EOF
================================================================================
LeetCode ${PROBLEM_NUMBER} — ${SLUG}
================================================================================

Problem description:

(Write problem statement here)

--------------------------------------------------------------------------------
Solution explanation:

(Write explanation here)

--------------------------------------------------------------------------------
Time Complexity:
?

Space Complexity:
?

================================================================================
EOF

# ---------------- test_pytest.py ----------------
cat > "$FOLDER/test_pytest.py" <<EOF
import pytest
from problems.lc${PROBLEM_NUMBER}_${SLUG}.solution import Solution


def test_basic():
    s = Solution()
    assert True  # replace with real test
EOF

# ---------------- test_hypothesis.py ----------------
cat > "$FOLDER/test_hypothesis.py" <<EOF
import pytest
from hypothesis import given, strategies as st
from problems.lc${PROBLEM_NUMBER}_${SLUG}.solution import Solution


@given(st.integers())
def test_property_example(x):
    s = Solution()
    assert True  # replace with real property-based logic
EOF

echo "Problem template created:"
echo "$FOLDER"
