'''
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

    If a customer purchases 0 books, they earn 0 points.
    If a customer purchases 2 books, they earn 5 points.
    If a customer purchases 4 books, they earn 15 points.
    If a customer purchases 6 books, they earn 30 points.
    If a customer purchases 8 or more books, they earn 60 points.
    Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
'''
# Create a class to calculate points based on the number of books purchased
class PointsCalculator:
    # Initialize the class with points and books attributes
    def __init__(self, points=0, books=0):
        self.points = points
        self.books = books
    # Define a method to calculate points based on the number of books purchased    
    def points_calc(self):
        
        if self.books >= 8:
            print(f'Wow! You purchased {self.books} books! You receive 60 points!')
            self.points += 60
        elif self.books < 8 and self.books >= 6:
            print(f'You purchased {self.books} books! You receive 30 points.')
            self.points += 30
        elif self.books < 6 and self.books >= 4:
            print(f'You purchased {self.books} books! You receive 15 points.')
            self.points += 15
        elif self.books < 4 and self.books >=2:
            print(f'You purchased {self.books} books! You receive 5 points.')
            self.points += 5
        else:
            print(f'0 points awarded! You must purchase 2 or more books to receive points.')
        
        return self.points

# Get the number of books purchased and current points from the user
while True:    
    try:        
        books = int(input('Enter the number of books purchase. '))
        points = int(input('How many points does the customer currently have? '))
        # Validate that the user input is not negative
        if books >= 0 and points >= 0:
            break
        else:
            print('You must enter a non-negative number.')
    except ValueError:
        print('You must enter a valid number')
    
# Create an instance of the PointsCalculator class and calculate the total points
total_points = PointsCalculator(points,books)
# Display the new points balance to the user
print(f'Your new points balance is {total_points.points_calc()}')


