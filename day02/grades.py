def add_grade(grades, total):
    new_grade = input('Please enter a test grade (type "done" to exit): ')

    if new_grade == 'done' and len(grades): # make sure there are grades to print
       return print(
           '\nGrades:', grades,
           '\nTotal:', total,
           '\nAverage', total/len(grades)
           )
    elif new_grade == 'done':
        return print('No grades were entered.')
    else:
        try:
            new_grade = abs(float(new_grade)) # try converting to float, use abs to ensure new_grade is positive
            grades += [new_grade]
            total += new_grade
        except:
            print('Error: please enter only numbers\n')
        finally:
            return add_grade(grades, total) # ask user for another grade       

if __name__ == '__main__':
    add_grade([], 0)
