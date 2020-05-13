#!/usr/bin/node
/*
   string to write
*/
const request = require('request');
request(process.argv[2], function (error, Response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + Response.statusCode);
  }
});
