#!/usr/bin/node
function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    console.error('NaN');
  } else {
    console.log(Number(a) + Number(b));
  }
}
add(process.argv[2], process.argv[3]);
