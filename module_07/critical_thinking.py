import sys

def main():
    course_info = {
        'CSC101':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        },
        'CSC102':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        },
        'CSC103':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        },
        'NET110':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        },
        'COM241':{
            'Room Number' : 3004,
            'Instructor Name': 'Haynes',
            'Meeting Time': '8:00 a.m.'
        }
    }

    def course_info_lookup(course_number, course_info, recursion_counter):

        if course_number in course_info:
            
            print(f"\033[1;4;33m Course information for {course_number}\033[0m")
            for info in course_info[course_number]:
                print(f"\033[94m    {info}: {course_info[course_number].get(info)}\033[0m")
        else:
            recursion_counter += 1
            print(f"\033[91m Course number {course_number} not found.\033[0m")

            print(recursion_counter)
            if recursion_counter < 3:
                course_number = input('Enter a valid course number: ').strip().upper()
                course_info_lookup(course_info=course_info, course_number=course_number, recursion_counter=recursion_counter)
            else:
                print("\033[1;31m\nMax tries reached. Program exiting.\033[0m")
                sys.exit()
    
    course_number = input('Enter a course number: ').strip().upper()
    course_info_lookup(course_number, course_info, recursion_counter=0)
    
if __name__ == "__main__":
    main()