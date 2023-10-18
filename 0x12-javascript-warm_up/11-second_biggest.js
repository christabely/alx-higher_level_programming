#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const maxsecond = argv.sort(function (a, b) { return b - a; })[3];
  console.log(maxsecond);
}
