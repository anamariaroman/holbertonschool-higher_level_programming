#!/usr/bin/node
/* Gets the contents of a webpage and stores it in a file. */
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
