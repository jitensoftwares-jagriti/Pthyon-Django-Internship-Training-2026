print_jobs = []

print_jobs.append("resume.pdf")
print_jobs.append("invoice.pdf")
print_jobs.append("report.pdf")

# while list: truthy check
# Queue naturally empties
while print_jobs:
	print("Printing:", print_jobs.pop(0))
	print(print_jobs)