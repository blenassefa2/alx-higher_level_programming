#!/usr/bin/node

const { argv } = require('process');
const { readFile, writeFile } = require('fs');

async function complete () {
  const file1 = readFile(argv[2], 'utf8');
  const file2 = readFile(argv[3], 'utf8');
  console.log(file1.toString());
  await writeFile(argv[4], file1 + file2,()=>{});
}
complete();
