#!/usr/bin/node
exports.converter = function (base) {
  function ForConverter (numb) {
    return numb.toString(base);
  }
  return ForConverter;
};
