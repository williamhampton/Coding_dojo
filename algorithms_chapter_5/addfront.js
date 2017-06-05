//given a pointer to the first listnode and a value create
// a new node, assign it to the list head and return a pointer to new head node

function Listnode(value){
  this.value = value;
  this.next = null;
}
var Rudy = new Listnode('val1')
console.log(Rudy.value)
