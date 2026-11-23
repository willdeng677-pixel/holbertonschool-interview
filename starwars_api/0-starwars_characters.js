#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi.dev' + '/api/films/' + movieId + '/';

function printCharacters(urls, index) {
  if (index >= urls.length) {
    return;
  }

  request(urls[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(urls, index + 1);
    }
  });
}

request(filmUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    printCharacters(film.characters, 0);
  }
});
