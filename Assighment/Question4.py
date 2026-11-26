fee = 1200
rate = 5.5
gym_name = "Fitness Club"
is_open = True
workouts = ["Yoga", "Cardio", "Weight Training"]
trainer = {"name": "Rahul", "age": 30}

# Print data types
print("Fee Type:", type(fee))
print("Rate Type:", type(rate))
print("Gym Name Type:", type(gym_name))
print("Open Flag Type:", type(is_open))
print("Workouts Type:", type(workouts))
print("Trainer Type:", type(trainer))

# Check ID
fee_copy = fee

print("Fee ID:", id(fee))
print("Fee Copy ID:", id(fee_copy))

# Change fee_copy
fee_copy = 2000

print("After Changing Fee Copy:")
print("Fee ID:", id(fee))
print("Fee Copy ID:", id(fee_copy))

print("Fee:", fee)
print("Fee Copy:", fee_copy)
