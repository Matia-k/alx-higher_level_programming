#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (C === undefined) this.print();
    else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) process.stdout.write(C);
        console.log();
      }
    }
  }
};
