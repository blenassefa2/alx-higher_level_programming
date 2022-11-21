#!/usr/bin/node

const dict = require('./101-data.js').dict;

const dict2 = {};

for (const key in dict) {
  const key2 = dict[key];
  if (!dict2[key2]) {
    dict2[key2] = [key];
  } else {
    dict2[key2].push(key);
  }
}
console.log(dict2);
