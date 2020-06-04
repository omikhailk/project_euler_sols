// By considering the terms in the Fibonacci sequence whose values do not
// exceed four million, find the sum of the even-valued terms.

package project_euler

import "fmt"

func fib(n int) int {
	// Recursive fibonacci function

	if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	} else {
		return fib(n-1) + fib(n-2)
	}
}

func even_fib_vals(limit int) int {
	// Finds all of the even valued fibonacci terms
	// which are below `limit`. Then returns their sum.

	var total, term int = 0, 1
	for {
		if total <= limit {
			if fib(term)%2 == 0 {
				total += term
			}
			term += 1
		} else {
			break
		}
	}
	return total
}

func Problem002_out() {
	fmt.Println(even_fib_vals(4000000))
}
