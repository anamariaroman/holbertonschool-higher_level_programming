#!/usr/bin/node
exports.esrever = function (list) {
  const temporalList = [];
  for (const i of list) {
    temporalList.unshift(i);
  }
  return temporalList;
};
