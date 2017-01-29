function finalcountdown(pram1,pram2,pram3,pram4){

  while (pram2 < pram3){
    if (pram2 == pram4){
      pram2 +=pram1;
    }
    else{
      console.log(pram2)
        pram2 += pram1;
    }
  }
}
finalcountdown(3,5,17,9);
