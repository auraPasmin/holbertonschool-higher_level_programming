#!/usr/bin/node
/*
  unction that returns the reversed version of a list:
*/
exports.esrever = function (list) {
  const list2 = [];
  for (let i = list.length - 1; i >= 0; i--) {
    list2.push(list[i]);
  }
  return list2;
};
