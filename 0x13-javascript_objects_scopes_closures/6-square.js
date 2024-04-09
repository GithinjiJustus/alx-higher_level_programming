#!/usr/bin/node
// 6-square.js

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
    constructor(size) {
        super(size); // Call the constructor of Square
    }

    charPrint(c = 'X') {
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = SquareWithCharPrint;
