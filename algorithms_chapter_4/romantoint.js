// given a roman numeral, turn it into an integer

function integer(rom){
  str = rom.split('')
  x = 0
  for(var i =0; i<str.length;i++){
    if(rom[i] == 'D'){
      x+=500
    }
    if(rom[i] == 'C'){
      x+=100
    }
    if(rom[i] == 'L'){
      x+=50
    }
    if(rom[i] == 'X'){
      x+=10
    }
    if (rom[i] == 'V'){
      x+=5
    }
    if(rom[i] == 'I'){
      x+=1
    }
  }
  console.log(x)
}
integer('DDDCLXVI')
