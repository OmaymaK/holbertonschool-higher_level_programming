#!/usr/bin/node
const axios = require('axios');

axios.get(process.argv[2])
  .then(resp => {
    const content = resp.data;
    const completed = {};
    for (let i = 0; i < content.length; i++) {
      if (content[i].completed) {
        if (completed[content[i].userId] !== undefined) {
          completed[content[i].userId] += 1;
        } else {
          completed[content[i].userId] = 1;
        }
      }
    }
    console.log(completed);
  });
