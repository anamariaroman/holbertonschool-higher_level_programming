#!/usr/bin/node
/* writes a string to a file. */
const fs = require('fs');
const thefile = process.argv[2];
const content = process.argv[3];
fs.writeFile(thefile, content, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
