#!/usr/bin/node

function callMeMoby (number, theFunction) {
  while (number > 0) {
    theFunction();
    number--;
  }
}
module.exports = { callMeMoby };
