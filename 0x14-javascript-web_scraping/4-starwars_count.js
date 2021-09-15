#!/usr/bin/node
/* Prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    let count = 0;
    const content = JSON.parse(body).results;
    for (const i in content) {
      for (const j in content[i].characters) {
        if (content[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
