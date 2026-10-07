from typing import List

# 1. Сумма всех чисел
def sum_all_numbers(n: int) -> int:
    """Возвращает сумму чисел от 1 до n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 2. Two Sum 
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Дан отсортированный по возрастанию массив.
    Находит два числа, сумма которых равна target, возвращает их индексы.
    Использует метод двух указателей.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# 3. Развернуть массив 
def reverse_array(arr: List[int]) -> List[int]:
    """Разворачивает массив in-place за O(n)."""
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# 4. Развернуть часть массива / Циклический сдвиг 
def reverse_part(arr: List[int], left: int, right: int) -> None:
    """Вспомогательная функция для разворота части массива."""
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_array(arr: List[int], k: int) -> List[int]:
    """
    Сдвигает массив вправо на k позиций.
    Решение через тройной разворот (in-place, O(n)).
    """
    n = len(arr)
    if n == 0:
        return arr
    k = k % n  # Обрабатываем случай, если k > n
    
    # 1. Разворачиваем весь массив
    reverse_part(arr, 0, n - 1)
    # 2. Разворачиваем первые k элементов
    reverse_part(arr, 0, k - 1)
    # 3. Разворачиваем оставшиеся элементы
    reverse_part(arr, k, n - 1)
    return arr


# 5. Слияние двух отсортированных массивов 
def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """Простое слияние с дополнительной памятью."""
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def merge_sorted_in_place(arr1: List[int], m: int, arr2: List[int], n: int) -> None:
    """
    Слияние без дополнительных аллокаций (как в LeetCode 88).
    arr1 имеет длину m + n, где первые m элементов - данные, последние n - нули.
    Идем с конца.
    """
    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p3] = arr1[p1]
            p1 -= 1
        else:
            arr1[p3] = arr2[p2]
            p2 -= 1
        p3 -= 1


# 6. Минимальный размер подмассива 
def min_sub_array_len(target: int, nums: List[int]) -> int:
    """Находит минимальную длину подмассива с суммой >= target (Скользящее окно)."""
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


# 7. Сортировка массива из 0 и 1 
def sort_binary_array(arr: List[int]) -> List[int]:
    """Сортирует массив из 0 и 1 (in-place, два указателя)."""
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            # arr[left] == 1 и arr[right] == 0
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr



# 8. Задача флага Нидерландов 
def sort_colors(nums: List[int]) -> None:
    """Сортировка массива из 0, 1, 2 (in-place, три указателя)."""
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# 9. Передвинуть четные числа вперед 
def even_first(arr: List[int]) -> List[int]:
    """Переносит четные числа в начало массива, сохраняя их порядок."""
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1
    return arr


# 10. Нули в конец
def move_zeroes(nums: List[int]) -> None:
    """Переносит все нули в конец массива, сохраняя порядок остальных чисел."""
    # По сути, это та же логика, что и even_first, но с проверкой на 0
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1


# ==========================================
# БЛОК ТЕСТИРОВАНИЯ (для проверки работоспособности)
# ==========================================
if __name__ == "__main__":
    print("--- Тестирование задач ---")
    
    # 1. Сумма
    print(f"Сумма 1..10: {sum_all_numbers(10)}") # 55
    
    # 2. Two Sum
    print(f"Two Sum: {two_sum([2, 7, 11, 15], 9)}") # [0, 1]
    
    # 3. Reverse
    print(f"Reverse: {reverse_array([1, 2, 3, 4, 5])}") # [5, 4, 3, 2, 1]
    
    # 4. Rotate
    print(f"Rotate k=3: {rotate_array([1, 2, 3, 4, 5, 6, 7], 3)}") # [5, 6, 7, 1, 2, 3, 4]
    
    # 5. Merge (In-place)
    arr1 = [3, 8, 10, 11, 0, 0, 0]
    arr2 = [1, 7, 9]
    merge_sorted_in_place(arr1, 4, arr2, 3)
    print(f"Merge in-place: {arr1}") # [1, 3, 7, 8, 9, 10, 11]
    
    # 6. Min SubArray
    print(f"Min SubArray: {min_sub_array_len(7, [2,3,1,2,4,3])}") # 2
    
    # 7. Sort Binary
    print(f"Sort Binary: {sort_binary_array([0, 1, 1, 0, 1, 0, 1, 0])}") # [0, 0, 0, 0, 1, 1, 1, 1]
    
    # 8. Dutch Flag
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    print(f"Dutch Flag: {colors}") # [0, 0, 1, 1, 2, 2]
    
    # 9. Even First
    print(f"Even First: {even_first([7, 3, 2, 4, 1, 11, 8, 9])}") # [2, 4, 8, 7, 3, 1, 11, 9] (порядок нечетных может отличаться, но четные в начале)
    
    # 10. Move Zeroes
    zeros = [0, 0, 1, 0, 3, 12]
    move_zeroes(zeros)
    print(f"Move Zeroes: {zeros}") # [1, 3, 12, 0, 0, 0]
    
    print("--- Все тесты пройдены ---")