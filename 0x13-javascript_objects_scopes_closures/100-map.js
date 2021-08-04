#!/usr/bin/node
const list = require('./100-data.js').list;
let indx = 0;
const array = list.map(i => i * indx++);
console.log(list);
console.log(array);
