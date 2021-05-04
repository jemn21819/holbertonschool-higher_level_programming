#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  for (const actor of JSON.parse(body).characters) {
    request(actor, function (error, response, body2) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body2).name);
    });
  }
});
