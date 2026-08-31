def test_percentage():
    marks = [80, 80, 80, 80, 80]
    total = sum(marks)

    # Current program's wrong calculation
    percentage = total / 4

    # Correct expected percentage
    assert percentage == 80
