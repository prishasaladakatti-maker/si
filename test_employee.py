from employee import employee_details

def test_employee_details():
    result = employee_details("rahul","emp101","It","50000")

    expected = "name: rahul\nEmployeeId:EMP101\nDepartment:IT\nsalary:50000"

    assert result == expected