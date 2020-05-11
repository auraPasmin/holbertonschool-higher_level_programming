#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle
If w or h is equal to 0 or not a positive integer,
create an empty object
Create an instance method called print()
that prints the rectangle using the character X
rotate() that exchanges the width and the height of the rectangle
double() that multiples " " " " " " " "by 2
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

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
