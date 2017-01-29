// create a positive integer that is less than 4000 amd return
//a string containing that value in roman numerals
// I = 1 V = 5 X = 10 L =50 C = 100 D = 500

function roman(int){
  arr = []
  i = 0
  while(int>=500){
    int = int - 500
    arr[i] = 'D'
    i++
  }
  while( int>= 100){
    int = int - 100
    arr[i] = 'C'
    i++
  }
  while( int>= 50){
    int = int-50
    arr[i] = 'L'
    i++
  }
  while(int>= 10){
    int = int-10
    arr[i] = 'X'
    i++
  }
  while(int>=5){
    int = int -5
    arr[i] = 'V'
    i++
  }
  while(int>0){
    int = int - 1
    arr[i] = 'I'
    i++
  }
  console.log(arr.join(''))
}
roman(1666)
