#!/usr/bin/node
/*
that returns the number of occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  let match = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      match++;
    }
  }
  return match;
};
