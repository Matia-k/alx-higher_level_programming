#!/usr/bin/node
const fin = require('fileC');
const fa = fin.readFileSync(process.argv[2], 'utf8');
const fb = fin.readFileSync(process.argv[3], 'utf8');
fin.writeFileSync(process.argv[4], fa + fb);
