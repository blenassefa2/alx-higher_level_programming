#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  return a + b;
}

const n1 = Number(argv[2]);
const n2 = Number(argv[3]);
if (n1 && n2) {
  console.log(add(n1, n2));
} else {
  console.log(NaN);
}
