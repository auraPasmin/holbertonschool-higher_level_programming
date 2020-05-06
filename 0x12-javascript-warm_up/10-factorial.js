#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (x) {
  if (process.argv.length <= 2 || x === 0) {
    return 1;
  }
  return (x * factorial(x - 1));
}
console.log(factorial(num));
