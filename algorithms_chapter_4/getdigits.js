// create a function that given a string returns the integer made from the strings
//digits so 1k3k4kjj5k1k24 should return 1345124
function digits(str){
  console.log(str.match(/\d+/g).join([]))
}
string = "1m2m3m4m5m6"
digits(string)
