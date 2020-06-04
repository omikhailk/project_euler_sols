// Find the sum of all the multiples of 3 or 5 below 1000.

package project_euler

import "fmt"

func mult_sum_limit(limit int) int {
	// Finds the sum of all of the multiples of 3 and 5
	// which are below `limit`. Returns the sum as an integer.
	var total int
	for i := 1; i < limit; i++ {
		if i%5 == 0 || i%3 == 0 {
			total += i
		}
	}
	return total
}

func Problem001_out() {
	fmt.Println(mult_sum_limit(1000))
}
