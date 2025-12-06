def employee_details(name,emp_id,department,salary):
    result=(
      f"Empployee Name:{name}\n"
      f"Employee ID:{emp_id}\n"
      f"Department:{department}\n"
      f"Salary:{salary}\n"
    )
return result
if__name__=="__main__":
   name="RUMAN"
   emp_id="E1001"
   department="IT"
   salary=50000
   print(employee_details(name,emp_id,department,salary))
