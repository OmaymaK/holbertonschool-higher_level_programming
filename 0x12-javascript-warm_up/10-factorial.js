#!/usr/bin/node
const { argv } = require('process');

if ((isNaN(argv[2]) || !argv[2]) || (parseInt(argv[2]) === 0)) {
  console.log(1);
} else {
  const num = parseInt(argv[2]);
  console.log(factorial(num));
}
function factorial (num) {
  if (num !== 1) {
    return num * factorial(num - 1);
  }
  if (num === 1) {
    return num;
  }
}
