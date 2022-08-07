#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += 'C';
      }
      for (let j = 0; j < this.height; j++) {
        console.log(str);
      }
    }
  }
};
