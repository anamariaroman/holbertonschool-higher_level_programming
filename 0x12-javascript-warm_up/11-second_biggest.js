#!/usr/bin/node
const nArray = process.argv.slice(2);
const lenghtArray = nArray.length;
if ((lenghtArray) < 2) {
  console.log('0');
} else {
  nArray.sort((x, y) => x - y);
  console.log(nArray[lenghtArray - 2]);
}
