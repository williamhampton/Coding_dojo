// create a function that given a string, returns all of the strings contents without
// blanks

function skip(str){
str = str.replace(/\s/g, '');
console.log(str)
  }

skip(' this is a test of skip')
