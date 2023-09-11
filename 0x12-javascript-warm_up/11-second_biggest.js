#!/usr/bin/node
let big = 0;
let n = 0;
const length = process.argv.length;
if (length === 2 || length === 3) console.log(0);
else {
  for (let i = 2; i < length; i++) {
    if (Number(process.argv[i]) > big) big = Number(process.argv[i]);
  }

  for (let i = 2; i < length; i++) {
    if (Number(process.argv[i]) === big) continue;
    if (Number(process.argv[i]) > n) n = Number(process.argv[i]);
  }
  console.log(n);
}
