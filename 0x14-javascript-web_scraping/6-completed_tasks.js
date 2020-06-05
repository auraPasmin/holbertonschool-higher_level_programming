#!/usr/bin/node
/*
  How many completed?
*/
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (dict[element.userId]) {
          dict[element.userId] = dict[element.userId] + 1;
        } else {
          dict[element.userId] = 1;
        }
      }
    });
    console.log(dict);
  }
});
