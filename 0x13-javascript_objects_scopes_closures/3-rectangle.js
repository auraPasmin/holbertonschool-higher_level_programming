#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle
If w or h is equal to 0 or not a positive integer,
create an empty object
Create an instance method called print()
that prints the rectangle using the character X
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
