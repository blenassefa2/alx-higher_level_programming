#!/usr/bin/node
const { argv } = require('process');
let toPrint = 'No argument';
argv.push(null);
if (argv[2] != null) {
  toPrint = argv[2];
}
console.log(toPrint);
