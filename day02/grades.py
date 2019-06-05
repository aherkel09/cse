def add_grade(grades=[], total=0):
    new_grade = input('Please enter a test grade (type "done" to exit): ')

    if new_grade == 'done':
        print('Grades:', grades, '\nTotal:', total, '\nAverage', total/len(grades))
    else:
        try:
            new_grade = abs(float(new_grade)) # try converting to float, use abs to ensure new_grade is positive
            grades += [new_grade]
            total += new_grade
        except:
            print('Error: please enter only numbers\n')
        finally:
            return add_grade(grades, total) # always ask user for another grade       

if __name__ == '__main__':
    add_grade()
