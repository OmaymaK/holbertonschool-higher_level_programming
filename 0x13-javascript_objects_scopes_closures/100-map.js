#!/usr/bin/node
let arr = require('./100-data.js').list;
console.log(arr);
arr = arr.map((x, y) => x * y);
console.log(arr);
