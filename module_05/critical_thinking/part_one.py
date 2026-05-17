'''
Part 1:
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

'''

# Get the number of years from the user
try:
    num_years = int(input("Enter the number of years: "))
except ValueError:
    print("You must enter a valid number.")
    exit()

total_months = 0
total_rainfall = 0.0

# Use nested loops to collect rainfall data
for year in range (1, num_years + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        try:
            rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
            if rainfall < 0:
                print("Rainfall cannot be negative. Please enter a valid number.")
                exit()
        except ValueError:
            print("You must enter a valid number.")
            exit()
        total_rainfall += rainfall
        total_months += 1
        
# Calculate the average rainfall
average_rainfall = total_rainfall / total_months
print()
print("\nRainfall Data:")
print(f'Total months: {total_months} months')
print(f'Total inches of rain: {total_rainfall:.2f} inches')
print(f'Average amount of rainfall per month: {average_rainfall:.2f} inches')