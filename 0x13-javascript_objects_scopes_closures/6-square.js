#!/usr/bin/node

const Square_ = require('./5-square');

module.exports = class Square extends Square_ {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row = row + c;
        }
        console.log(row);
      }
    }
  }
};
