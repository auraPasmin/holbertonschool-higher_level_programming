#!/usr/bin/node

const arg = process.argv;

if (!parseInt(arg[2])) {
  console.log('Missing size');
} else {
  for (let y = parseInt(arg[2]); y > 0; y--) {
    let size = '';
    for (let x = parseInt(arg[2]); x > 0; x--) {
      size += 'X';
    }
    console.log(size);
  }
}
