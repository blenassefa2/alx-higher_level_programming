#!/usr/bin/node
const { argv } = require('process');
const converted = Number(argv[2]);
if (converted) {
  console.log('My number:', converted);
} else {
  console.log('Not a number');
}
