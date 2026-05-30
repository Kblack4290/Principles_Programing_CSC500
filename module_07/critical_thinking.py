import sys

# This program allows the user to look up course information based on a course number.
def main():
    # The course information is stored in a nested dictionary
    course_info = {
        'CSC101':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        },
        'CSC102':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '9:00 a.m.'
        },
        'CSC103':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '10:00 a.m.'
        },
        'NET110':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '11:00 a.m.'
        },
        'COM241':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '1:00 a.m.'
        }
    }
    # This function looks up the course information based on the course number provided by the user.
    def course_info_lookup(course_number, course_info, attempt_counter):

        # Check if the course number is in the course information dictionary
        # If it is, print the course information. If it is not, increment the recursion counter and prompt the user to enter a valid course number.
        if course_number in course_info:
            
            print(f"\033[1;4;33m Course information for {course_number}\033[0m")
            for info in course_info[course_number]:
                print(f"\033[94m    {info}: {course_info[course_number].get(info)}\033[0m")
        else:
            attempt_counter += 1
            print(f"\033[91m Course number {course_number} not found.\033[0m")

            if attempt_counter < 3:
                course_number = input('Enter a valid course number: ').strip().upper()
                course_info_lookup(course_info=course_info, course_number=course_number, attempt_counter=attempt_counter)
            else:
                print("\033[1;31m\nMax tries reached. Program exiting.\033[0m")
                sys.exit()
    
    # Prompt the user to enter a course number and call the course_info_lookup function to retrieve and display the course information.
    course_number = input('Enter a course number: ').strip().upper()
    course_info_lookup(course_number, course_info, attempt_counter=0)
    
if __name__ == "__main__":
    main()