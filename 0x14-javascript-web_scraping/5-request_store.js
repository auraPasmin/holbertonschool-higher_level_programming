#!/usr/bin/node
/*
  Loripsum
*/
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, request, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      fs.writeFileSync(process.argv[3], body, 'utf-8');
    } catch (error) {
      console.log(error);
    }
  }
});
