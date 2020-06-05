#!/usr/bin/node
/*
  Who was playing in this movie?
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).characters.forEach(element => {
      request(element, function (err, res, bod) {
        if (err) {
          console.log(error);
        } else {
          console.log(JSON.parse(bod).name);
        }
      });
    });
  }
});
