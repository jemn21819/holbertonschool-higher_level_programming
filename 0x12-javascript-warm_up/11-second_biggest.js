#!/usr/bin/node
const numList = process.argv.slice(2);
let secBig = 0;
if (numList.length > 1) {
  numList.sort();
  secBig = numList[numList.length - 2];
}
console.log(secBig);
