def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int,input_list.split(",")))
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược là:", list_dao_nguoc)