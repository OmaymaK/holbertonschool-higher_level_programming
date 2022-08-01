#!/usr/local/bin/node
const { argv } = require('process');

if ((isNaN(argv[2]) || !argv[2]) || (parseInt(argv[2]) === 0)) {
  console.log(1);
} else {
  const num = parseInt(argv[2]);
  factorial(num, 1);
}
function factorial (num, fact) {
  fact *= num;
  if (num !== 2) {
    factorial(num - 1, fact);
  }
  if (num === 2) {
    console.log(fact);
  }
}
