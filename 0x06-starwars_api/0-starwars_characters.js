#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const movieURL = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(movieURL, async (err, response, body) => {
    if (err) {
      console.log(err);
    }
    for (const characterId of JSON.parse(body).characters) {
      await new Promise((resolve, reject) => {
        request(characterId, (err, response, body) => {
          if (err) {
            reject(err);
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
