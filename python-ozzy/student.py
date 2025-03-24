
def student_capture():
    details = {input('Enter your key: '): input('Enter the value: ') for _ in range(2)}

    Average_test = ((int(details['Test_1_marks']) + int(details['Test_2_marks']))/2)*0.4
    print(f'The average marks of test 1 and test 2 with reference to the 40% is {Average_test}')
    

print(student_capture())