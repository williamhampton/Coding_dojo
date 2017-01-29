//from drawstars create function that draws an item x number of times

function drawleftchar(num,char){
    console.log((char).repeat(num))
}
drawleftchar(10,"*")

function drawrightchar(num,char){
  console.log(" ".repeat(75-num)+(char).repeat(num))
}
drawrightchar(10,"3")

function drawcenterchar(num,char){
  console.log(" ".repeat(75/2-num/2)+ (char).repeat(num)+ " ".repeat(75/2-num/2))
}
drawcenterchar(10,"4")
