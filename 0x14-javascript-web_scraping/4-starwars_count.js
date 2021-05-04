#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let times = 0;
    const movies = JSON.parse(body).results;
    for (const actor in movies) {
      const character = movies[actor].characters;
      for (const i in character) {
        if (character[i].includes('18')) {
          times++;
        }
      }
    }
    console.log(times);
  }
});
