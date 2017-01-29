//create function that swaps first and last, and third and third from last
function swap(arr){
  arr.push(arr[0])
  arr[0]=arr[arr.length-2]
  arr[arr.length-2] = arr[arr.length-1]
  arr[arr.length-1]=arr[2]
  arr[2]=arr[arr.length-4]
  arr[arr.length-4]=arr[arr.length-1]
  arr.pop()
  console.log(arr)
}
array = [1,2,3,4,5,6,7,8]
swap(array)
