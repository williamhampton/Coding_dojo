//assume you have a text field 75 spaces wide, print stars in patters:
//left right and cemter

function drawleftstars(num){
    console.log("*".repeat(num))
}
drawleftstars(10)

function drawrightstars(num){
  console.log(" ".repeat(75-num)+"*".repeat(num))
}
drawrightstars(10)

function drawcenterstars(num){
  console.log(" ".repeat(75/2-num/2)+ "*".repeat(num)+ " ".repeat(75/2-num/2))
}
drawcenterstars(10)
