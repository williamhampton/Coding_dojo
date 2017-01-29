function thislen(num1, num2) {
	if(num1 == num2) { //use !== for value and type
    console.log("Jinx!");
  }
    else{
      var arr = [];
		  for(var i = 0; i < num1; i++) {
			     arr.push(num2);
		  }
	   }
	//console.log(arr);
  return(arr);
}

thislen(1,1);
thislen(7,2,3,4,5,6,7);
