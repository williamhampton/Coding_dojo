//create a function that returns number in the fibonacci sequence
function fib(num){
  arr = [0,1]
  while (arr.length<=num){
    arr.push(arr[arr.length-1]+arr[arr.length-2])
  }
  console.log (arr[num])
}
fib(3)
fib(8)
