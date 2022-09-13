#!/usr/bin/node
const axios = require('axios').default;
const inp = process.argv[2];
const Url = `https://swapi-api.hbtn.io/api/films/${inp}`;
axios.get(Url)
  .then(function (response) {
    console.log('%s', response.data.title);
  });
