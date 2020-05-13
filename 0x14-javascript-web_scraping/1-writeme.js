#!/usr/bin/node
/*
   string to write
*/
const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3]);
} catch (error) {
  console.log(error);
}
