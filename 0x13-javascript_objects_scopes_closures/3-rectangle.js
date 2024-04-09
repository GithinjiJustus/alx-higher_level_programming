#!/usr/bin/node
// 3-rectangle.js

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return {}; // Return an empty object if either width or height is not valid
        }
        this.width = w;
        this.height = h;
    }

    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }
}

module.exports = Rectangle;
