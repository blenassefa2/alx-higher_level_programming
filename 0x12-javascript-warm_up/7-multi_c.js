#!/usr/bin/node
const { argv } = require('process');
const toPrint = 'C is fun';
let x = Number(argv[2]);
if (x) {
  while (x > 0) {
    console.log(toPrint);
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
