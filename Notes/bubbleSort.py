def bubble__sort(arr):
    array_length: int = 0

    for _ in arr:
        array_length += 1
    
    for i in range(array_length):
        is_swapped = False
        for j in range(array_length - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                is_swapped = True
            
            print_array("Round", i + 1, "Step", j + 1, arr)

        if not is_swapped:
            break
    
    return arr


def print_array(round_text, round_num, step_text, step__num, arr):
    print(f"{round_text} {round_num} {step_text} {step__num}:", end=" ")

    print("[", end=" ")
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i], end=" ")