#!/usr/bin/node

function factorial(n) {
  // Base case: if n is 0 or 1, factorial is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: factorial(n) = n * factorial(n - 1)
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (!isNaN(num)) {
  // Compute the factorial and print the result
  console.log(factorial(num));
} else {
  // If argument is not a valid integer, print factorial of NaN which is 1
  console.log(1);
}

