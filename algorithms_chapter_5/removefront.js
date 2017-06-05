//create a function that removes the head node and makes the next node the head


function Listnode(value){
  this.value = value;
  this.next = null;
}
var list = new Listnode('value1')
list.next = new Listnode('value2')
list.next.next = new Listnode('value3')
function removefront(runner){
  runner.value = runner.next.value;
  runner.next = runner.next.next

  console.log(runner)
}
removefront(list)
