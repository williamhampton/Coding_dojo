//make a fucnction that returns coin change from a number of american cents

function generateCoinChange(num){
  var x = num
  var quarter = 0
  var dime = 0
  var nickel = 0
  var penny = 0
  while (x>0){
    while(x>=25){
      x = x-25
      quarter+=1}
    while(x>=10){
      x = x -10
      dime +=1}
    while (x>=5){
      x = x-5
      nickel +=1}
    while (x>0){
      x=x-1
      penny +=1}
    }
  console.log("Quarters: "+quarter + "  Dimes: "+dime+ "  Nickels: "+nickel+"  Pennies: "+penny)
}
generateCoinChange(50)
generateCoinChange(86)
generateCoinChange(91)
