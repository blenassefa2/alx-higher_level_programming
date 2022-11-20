#!/usr/bin/node
const { argv } = require('process');
const collection = argv;

collection.shift();
collection.shift();

for (let i = 0; i < collection.length; i++) {
  collection[i] = Number(collection[i]);
}

collection.sort(function (a, b) { return a - b; });
collection.reverse();

if (collection.length < 2) {
  console.log(0);
} else {
  console.log(collection[1]);
}
