# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.


try:
    # Ask the user for the current time as requested by the prompt
    current_time = int(input("Enter the current time (0-23): "))
    if current_time < 0 or current_time > 23:
        print("Invalid input. Please enter a value between 0 and 23 for the current time.")
        exit()
    
    # Ask the user for the number of hours until the alarm goes off
    alarm_hours = int(input("Enter the number of hours till alarm sounds off: "))
    if alarm_hours < 0:
        print("Invalid input. Please enter a non-negative value for the number of hours.")
        exit()
    
except ValueError:
    print("Invalid input. Please enter a numeric value for the number of hours.")
    exit()
    
# Calculate the time when the alarm will go off using modulo operator to wrap around 24 hours
alarm_time = (current_time + alarm_hours) % 24

# Display the current time and the alarm time
if alarm_time == 0:
    print(f"Alarm will go off at: {alarm_time}:00 at midnight.")
elif alarm_time < 12:
    print(f"Alarm will go off at: {alarm_time}:00 in the morning.")
elif alarm_time == 12:
    print(f"Alarm will go off at: {alarm_time}:00 at noon.")
elif alarm_time > 12 and alarm_time < 17:
    print(f"Alarm will go off at: {alarm_time}:00 in the afternoon.")
elif alarm_time >= 17 and alarm_time < 24:
    print(f"Alarm will go off at: {alarm_time}:00 in the evening.")
