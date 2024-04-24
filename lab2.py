#  лаб 2 вариант 6: Түпнұсқаны өзгертпей, жаңа тізімді қайтарып,
#  сандар тізімін сүзуге арналған  таза функцияны іске қосыңыз.

def new_sorted_list(original_list):
    sorted_list = sorted(original_list)
    return sorted_list


numbers = [12,  36, 48, 96, 72, 120, 84]
sorted_numbers = new_sorted_list(numbers)

print("Бастапқы тізім:", numbers)
print("Өңделген тізім:", sorted_numbers)
