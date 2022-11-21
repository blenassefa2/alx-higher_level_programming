#!/usr/bin/node

const imported = require('./100-data.js').list;
console.log(imported);
console.log(imported.map((x, index) => x * index));
