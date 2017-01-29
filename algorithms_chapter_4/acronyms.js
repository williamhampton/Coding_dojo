// given a string, return the acronym of the string ie:
//" this is a test"==> tiat
function acr(str){
  wordarr = str.split(' ')
  array = []
  for (var i = 0; i<wordarr.length; i++){
    array[i] = (wordarr[i][0])
  }
  console.log(array.join('').toUpperCase())
}
string = 'this is a test to see if it works'
acr(string)
