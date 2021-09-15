#!/usr/bin/node
/* Reads and prints the content of a file. */
const fs = require('fs');
const thefile = process.argv[2];

fs.readFile(thefile, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
