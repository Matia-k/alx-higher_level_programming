#!/usr/bin/node
const numb = Math.floor(Number(process.argv[2]));
if (isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numb);
}
