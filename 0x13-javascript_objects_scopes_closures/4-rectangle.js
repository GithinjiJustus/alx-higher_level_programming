#!/usr/bin/node
// 4-rectangle.js

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

    rotate() {
        // Swap width and height
        [this.width, this.height] = [this.height, this.width];
    }

    double() {
        // Double width and height
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
