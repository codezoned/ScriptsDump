package main

import (
	"algoutils"
	"fmt"
)

func swap(myArray []int, i, j int) {
	tmp := myArray[j]
	myArray[j] = myArray[i]
	myArray[i] = tmp
}

func bubbleSort(myArray []int) {

	swapped := true
	for swapped {
		swapped = false
		for i := 0; i < len(myArray)-1; i++ {
			if myArray[i+1] < myArray[i] {
				algoutils.Swap(myArray, i, i+1)
				swapped = true
			}
		}
	}
}

func main() {

	myArray := []int{3, 6, 8, 5, 9}
	fmt.Println("Unsorted array: ", myArray)
	bubbleSort(myArray)
	fmt.Println("Sorted array: ", myArray)
}
