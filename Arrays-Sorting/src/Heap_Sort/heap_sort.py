def heapify(arr, n, i):
	largest = i
	l = 2 *i + 1
	r = 2 *i + 2

	if l < n and arr[l] > arr[largest]:
		largest = l

	if r < n and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[largest], arr[i] = arr[i], arr[largest]
		heapify(arr, n, largest)


def build_heap(arr):
	arr_len = len(arr)
	for i in range(arr_len//2 - 1, -1, -1):
		heapify(arr, arr_len, i)


def heap_sort(arr):
	build_heap(arr)
	for i in range(len(arr) - 1, -1, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)


def main():
	arr = [9.7, 1.3, -2, 1, 0]
	print("Before: ", arr)
	heap_sort(arr)
	assert arr == [-2, 0, 1, 1.3, 9.7]
	print("After: ", arr)


if __name__ == '__main__':
	main()
