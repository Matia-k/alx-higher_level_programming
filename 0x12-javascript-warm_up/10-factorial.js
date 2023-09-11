#!/usr/bin/node
const x = Number(process.argv[2]);
console.log(factorial(x));

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
