#!/usr/bin/node
// 2-rectangle.js

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return {}; // Return an empty object if either width or height is not valid
        }
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;
