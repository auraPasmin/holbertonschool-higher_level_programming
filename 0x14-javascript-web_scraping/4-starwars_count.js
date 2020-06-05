#!/usr/bin/node
/*
  Star wars Wedge Antilles
*/
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let cnt = 0;
    JSON.parse(body).results.forEach(character => {
      character.characters.forEach(link => {
        if (link.endsWith('/18/')) {
          cnt++;
        }
      });
    });
    console.log(cnt);
  }
});
