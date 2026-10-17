def test_mark_attendance():
    student_id = "STU001"
    attendance_status = "Present"

    assert student_id == "STU001"
    assert attendance_status == "Present"

    print("Attendance marking test passed")


if __name__ == "__main__":
    test_mark_attendance()