#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
