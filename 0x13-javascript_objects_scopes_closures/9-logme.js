#!/usr/bin/node
/*
printed and the new argument value. (see example below)
*/
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
