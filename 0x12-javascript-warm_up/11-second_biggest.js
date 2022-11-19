#!/usr/bin/node
const { argv } = require('process');
const collection = argv;

collection.shift();
collection.shift();

collection.sort();
collection.reverse();
if (collection.length < 2) {
  console.log(0);
} else {
  console.log(collection[1]);
}
