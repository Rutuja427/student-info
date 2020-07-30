import csv


def write_info_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])
        writer.writerow(info_list)
            
        
if __name__=='__main__':
    condition=True
    student_num=1

    while(condition):
        student_info=input("Enter student #{} information in the following format(Name Age Contact_number Email-ID):".format(student_num))

        student_info_list=student_info.split(' ')

        print("\n The entered information is-\nNmae:{}\n Age:{}\n Contact number:{}\n E-mail ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is entered information is correct(Yes/no):")

        if choice_check=="yes":
            write_info_csv(student_info_list)

            condition_check=input("enter (yes or no)if you want to enter information for another student:")
            if condition_check=="yes":
                condition=True
                student_num+=1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\nPlease re-enter the information!")
