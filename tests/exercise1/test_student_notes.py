import pytest
from src.exercise1.student_notes import student_notes


def test_student_notes():
    assert student_notes(8, 8, 8, 8) == 8
