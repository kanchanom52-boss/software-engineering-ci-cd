import subprocess

def test_percentage():
    result = subprocess.run(
        ["python", "student_marks_analyzer.py"],
        input="80\n80\n80\n80\n80\n",
        text=True,
        capture_output=True
    )

    assert "Percentage: 80.0 %" in result.stdout
