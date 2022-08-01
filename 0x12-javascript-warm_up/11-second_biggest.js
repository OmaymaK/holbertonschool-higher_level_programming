#!/usr/bin/node
const { argv } = require('process');

if (!argv[3]) {
  console.log(0);
} else {
  argv.shift();
  argv.shift();
  const arr = argv.map(x => parseInt(x));
  arr.sort((a, b) => a - b);
  arr.pop();
  console.log(arr[arr.length - 1]);
}
