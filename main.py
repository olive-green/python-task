def merge_lists(list1, list2):
    merged_list = []
    # Create a dictionary to store the student information by id
    student_dict = {}
    # Iterate over list1 and add each student's information to the dictionary
    for student in list1:
        student_dict[student["id"]] = student
    # Iterate over list2 and update the dictionary with the additional information
    for student in list2:
        if student["id"] in student_dict:
            student_dict[student["id"]].update(student)
        else:
            student_dict[student["id"]] = student
    # Append each student's information from the dictionary to the merged list
    for student in student_dict.values():
        merged_list.append(student)
    return merged_list


list1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

merged_list = merge_lists(list1, list2)
print(merged_list)
