from abstra.forms import TextInput, EmailInput, DateInput, DropdownInput, TextOutput, run
from abstra.tasks import send_task

print("🚀 Starting Employee Registration Form...")

# Welcome message and form
employee_data = run([
    TextOutput("welcome", "# Welcome to Our Company! 👋\nPlease fill out your information to start the onboarding process."),
    TextInput("full_name", "Full Name", placeholder="Enter your full name"),
    EmailInput("email", "Work Email", placeholder="your.name@company.com"),
    DropdownInput("department", "Department", [
        "Engineering", 
        "Marketing", 
        "Sales", 
        "HR", 
        "Finance", 
        "Operations"
    ]),
    TextInput("position", "Job Position", placeholder="e.g., Software Engineer"),
    DateInput("start_date", "Start Date"),
    TextOutput("next_steps", "✅ Thank you! Your information will be reviewed by HR.")
])

print(f"📝 Form submitted for: {employee_data['full_name']}")
print(f"📧 Email: {employee_data['email']}")
print(f"🏢 Department: {employee_data['department']}")

# Send task to HR review stage
send_task("employee_review", "976a578f-2350-4c4b-88fc-f72a4ea92315", {
    "employee": employee_data,
    "status": "pending_review",
    "submitted_at": "2024-01-15"  # In real app, use datetime.now()
})

print("📤 Task sent to HR Review stage")
print("✅ Employee registration completed!")
