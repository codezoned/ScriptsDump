// Simple Fibonacci

package main

import (
        "fmt"
)

func main() {
        var x = fib(10)
        fmt.Println(x)
}

func fib(number int) int {
  if number == 0 || number == 1{
        return number
  }

  return fib(number - 2) + fib(number - 1)
}
