#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((char) => {
    request(char, (err, res, body) => {
      if (err) {
        console.log(err);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  });
});
