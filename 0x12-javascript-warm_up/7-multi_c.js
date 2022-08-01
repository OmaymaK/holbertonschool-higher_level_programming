#!/usr/bin/node
const { argv } = require('process');
let i = 0;
const x = argv[2];
while (i < x) {
  console.log('C is fun');
  i++;
}
