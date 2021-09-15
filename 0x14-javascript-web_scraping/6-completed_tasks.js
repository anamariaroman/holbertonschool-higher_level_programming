#!/usr/bin/node
/* Computes the number of tasks completed by user id. */
const request = require('request');
const url = process.argv[2]
request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    const taskscomplete = {};
    for (const row of content) {
      if (row.complete === true) {
        if (taskscomplete[take.userId] === undefined) {
          taskscomplete[take.userId] = 0;
        }
        taskscomplete[take.userId] += 1;
      }
    }
    console.log(taskscomplete);
  } else {
    console.log(err);
  }
});
