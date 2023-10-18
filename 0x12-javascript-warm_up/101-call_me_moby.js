#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
