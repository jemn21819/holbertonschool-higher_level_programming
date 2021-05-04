#!/usr/bin/node
const request = require('request');
const taskData = {};
request(process.argv[2], function (err, request, body) {
  if (err) {
    console.log(err);
  }
  for (const user of JSON.parse(body)) {
    if (user.completed === true) {
      if (taskData[user.userId] === undefined) {
        taskData[user.userId] = 0;
      }
      taskData[user.userId]++;
    }
  }
  console.log(taskData);
});
