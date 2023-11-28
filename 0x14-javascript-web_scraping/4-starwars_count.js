#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const results = JSON.parse(body).results;
  let count = 0;

  for (const result of results) {
    for (const char of result.characters) {
      if (char.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
