def merging(list1, list2,return_list):
    i = j = 0
    while i+j < len(return_list):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):
            return_list[i+j] = list1[i]
            i+=1
        else:
            return_list[i+j] = list2[j]
            j+=1
    return return_list


def merge_sort(list):
    length = len(list)
    if length < 2:
        return
    mid = length//2
    list_1 = list[0:mid]
    list_2 = list[mid:length]
    merge_sort(list_1)
    merge_sort(list_2)
    return merging(list_1,list_2,list)

print(merge_sort([1,2,4,6,7,19,68,2345,90,100,1230]))