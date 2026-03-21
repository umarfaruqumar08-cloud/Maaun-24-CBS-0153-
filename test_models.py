from models import Patient, ClinicQueue

# Create a queue
queue = ClinicQueue()

# Create some patients
patient1 = Patient("John Doe", 25, "Headache")
patient2 = Patient("Jane Smith", 30, "Fever")

# Add them to queue
queue.enqueue(patient1)
queue.enqueue(patient2)

# Check queue size
print(f"\nTotal waiting: {queue.size()}")

# See who's first
first = queue.peek()
print(f"Next to serve: {first}")

# Serve the first patient
served = queue.dequeue()
print(f"\nServed: {served}")

# Check remaining
print(f"Still waiting: {queue.size()}")
print(f"Total served today: {queue.get_total_served()}")