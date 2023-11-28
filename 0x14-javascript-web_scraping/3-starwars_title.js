#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
