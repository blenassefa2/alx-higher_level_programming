#!/usr/bin/node
const { argv } = require('process');
const is = 'is';
const undefined_ = 'undefined';
if (argv[2] === undefined) {
  argv[2] = undefined_;
}
if (argv[3] === undefined) {
  argv[3] = undefined_;
}
console.log(argv[2], is, argv[3]);
