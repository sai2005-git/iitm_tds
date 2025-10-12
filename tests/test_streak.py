import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak surrounded by non-positives."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 0, -5]) == 3

def test_multiple_streaks_longest_first():
    """Test with multiple streaks, where the longest streak is first."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6, 0, 7]) == 4

def test_multiple_streaks_longest_last():
    """Test with multiple streaks, where the longest streak is last."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 6, 0, 7]) == 4

def test_multiple_streaks_longest_middle():
    """Test with multiple streaks, where the longest streak is in the middle."""
    assert longest_positive_streak([1, 0, 3, 4, 5, -2, 6, 7]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5, 6]) == 3

def test_example_from_prompt():
    """Test the specific example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_another_example():
    """Test another case to be sure."""
    assert longest_positive_streak([1, 1, 1]) == 3