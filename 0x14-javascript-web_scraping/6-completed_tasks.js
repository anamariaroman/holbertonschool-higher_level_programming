#!/usr/bin/node
/* Computes the number of tasks completed by user id. */
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    const completed = {};
    for (const row of content) {
      if (row.completed === true) {
        if (completed[row.userId] === undefined) {
          completed[row.userId] = 0;
        }
        completed[row.userId] += 1;
      }
    }
    console.log(completed);
  } else {
    console.log(err);
  }
});
