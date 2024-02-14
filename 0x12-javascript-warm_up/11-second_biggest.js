#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Parse arguments as integers

if (args.length <= 1) { // If no arguments or only one argument
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Sort integers in descending order
  console.log(args[1]); // Print the second element (second biggest integer)
}

