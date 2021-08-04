#!/usr/bin/node
const converter = require('./10-converter').converter;

const myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
