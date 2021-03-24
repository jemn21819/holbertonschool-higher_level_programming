#!/usr/bin/node
let secBig = 0;
const numList = process.argv.slice(2);
if (numList.length > 1) {
  numList.sort();
  secBig = numList[numList.length - 2];
}
console.log(secBig);
