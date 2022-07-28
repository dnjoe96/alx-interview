#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const baseUrl = 'https://swapi-api.hbtn.io/api/';

request(`${baseUrl}films/`, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const result = body.results;

  for (const one of result) {
    if (one.episode_id === Number(id)) {
      listActors(one.characters);
    }
  }
});

function listActors (listOfLinks) {
  for (const characterUrl of listOfLinks) {
    request(`${characterUrl}`, { json: true }, (err, res, body) => {
      if (err) { return console.log(err); }
      console.log(body.name);
    });
  }
}
