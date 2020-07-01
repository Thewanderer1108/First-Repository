# This program allows a user to insert student data(ID and the respective marks secured in a subject)
# which is then later use to calculate the percentage of all the students.


def get_student_data():
    student_data = {}
    while True:
        s_id = input("Enter Student ID: ")
        s_marks = input("Enter marks obtain by this student separated by comma: ")
        if s_id in student_data:
            print("Student ID and details already exist.")
        else:
            student_data[s_id] = s_marks.split(",")
        s_more = input("Want to add more Students(y/n)?: ")
        if s_more.lower() == "no" or s_more.lower() == "n":
            break
        else:
            print("Please continue entering Students marks")

    return student_data


def get_average(data):
    marks_dict = {}
    for keys in data:
        m_list = data[keys]     # this will extract the list in a specific dictionary key
        s = 0
        for marks in m_list:
            s += int(marks)
        marks_dict[keys] = s/len(m_list)

    # printing the avg marks got by each student in a formatted manner
    for i in marks_dict:
        print("Student ID: {}, Avg Marks: {}".format(i, marks_dict[i]))


if __name__ == "__main__":
    s_data = get_student_data()
    get_average(s_data)
