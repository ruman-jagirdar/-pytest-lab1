from employee import employee_details
def test_employee_details():
    expected_output=(
        "Employee Name:RUMAN\n"
        "Employee ID:E1001\n"
        "Department:IT\n"
        "Salary:50000"
    )
  assert employee_details("RUMAN","E1001","IT",50000)==expected_output
