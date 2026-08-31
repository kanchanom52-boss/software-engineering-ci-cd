def test_percentage():
    marks = [80, 80, 80, 80, 80]
    total = sum(marks)
    percentage = total / 4

    assert percentage == 80
