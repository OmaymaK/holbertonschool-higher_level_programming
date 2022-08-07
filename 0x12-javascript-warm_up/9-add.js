#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2]) && isNaN(argv[3]) && !argv[2] && !argv[3]) {
  console.log('NaN');
} else {
  const a = parseInt(argv[2]);
  const b = parseInt(argv[3]);
  add(a, b);
}
function add (a, b) {
  console.log(a + b);
}
