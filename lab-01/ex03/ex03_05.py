def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
world_list =input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(world_list)
print("Số lần xuất hiện của các phần từ:", so_lan_xuat_hien)