#!/usr/bin/node
let count = 0;
exports.logMe = function (Item) {
  console.log(count + ': ' + Item);
  count += 1;
};
