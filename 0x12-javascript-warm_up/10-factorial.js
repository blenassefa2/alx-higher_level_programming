#!/usr/bin/node
const { argv } = require('process');

function factorial (number) {
  if (number === 0 || number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}
const n = Number(argv[2]);
if (!n) {
  console.log(1);
} else {
  console.log(factorial(n));
}
