class Company:
    company_name = "TechCorp"  # Class variable (shared)

    def __init__(self, employee_name):
        self.employee_name = employee_name  # Instance variable


e1 = Company("Anita")
e2 = Company("Vikram")

print(e1.company_name, e1.employee_name)
print(e2.company_name, e2.employee_name)
