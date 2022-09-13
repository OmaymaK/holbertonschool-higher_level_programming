#!/usr/bin/node
const fs = require('fs');
const content = process.argv[3];

try {
  fs.writeFileSync(process.argv[2], content);
} catch (err) {
  console.log(err);
}
