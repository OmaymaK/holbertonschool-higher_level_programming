#!/usr/bin/node
const { process } = require('process');
if (process.length === 2) {
  console.log('No argument');
} else if (process.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
