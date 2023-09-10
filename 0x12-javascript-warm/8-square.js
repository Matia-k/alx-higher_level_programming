#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const numb = Number(process.argv[2]);
  for (let i = 0; i < numb; i++) {
    for (let i = 0; i < numb; i++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
