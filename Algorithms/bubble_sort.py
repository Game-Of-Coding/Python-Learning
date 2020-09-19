import random

def generateRandomList(bound):
    random_arr = []
    for _ in range(bound):
        random_arr.append(random.randint(0, bound))
    return random_arr

def sortList(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def main():
    bound = 20
    random_arr = generateRandomList(bound)
    print(f'INPUT: {random_arr}')
    sorted_list = sortList(random_arr)
    print(f'OUPUT: {random_arr}')

if __name__ == '__main__':
    main()

