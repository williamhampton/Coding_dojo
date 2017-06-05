// create a function the locates the minimum value in a linked
// list and moves it to the front of the list and returns the new list

function Listnode(value){
  this.value = value;
  this.next = null;
  this.new = function(val){
    runner = this;
    while (runner.next != null){
      runner = runner.next
    }
    runner.next = new Listnode(val)
    runner = this;
  }
  this.contains = function(val){
    runner = this
    while(runner != null){
      if(runner.value == val){
        return true;
      }
      else{
        runner = runner.next;
      }
    }
    return false
  }
  this.length = function(){
    var len = 0;
    runner = this
    while (runner != null){
      len++;
      runner = runner.next
    }
    return(len)
  }
  this.display = function(){
    runner = this;
    while(runner != null){
      console.log(runner.value)
      runner = runner.next
    }
  }
  this.max = function(){
    runner = this;
    var x = runner.value
    while(runner != null){
        if (runner.value > x){
          x = runner.value
          runner = runner.next
        }
        else{
          runner = runner.next
        }
    }
    return(x)
  }
  this.min = function(){
    runner = this;
    var x = runner.value
    while(runner != null){
        if (runner.value < x){
          x = runner.value
          runner = runner.next
        }
        else{
          runner = runner.next
        }
    }
    return(x)
  }
  this.average = function(){
    runner = this
    x = 0
    y = 0
    while (runner != null){
      x += runner.value
      y += 1
      runner = runner.next
    }
    runner = new Listnode(x/y)
    return runner.value
  }
  this.back = function(){
    runner = this;
    while (runner.next != null){
      runner = runner.next
    }
    return runner.value
  }
  this.minfront = function(){
    runner = this
    runner2 = this
    var x = runner.value
    while (runner != null){
      if (runner.value<x){
        x = runner.value
        runner = runner.next
      }
      else {
        runner = runner.next
      }
    }
    var newlist = new Listnode(x)
    while(runner2 != null){
      if (runner2.value == x){
        runner2 = runner2.next
      }
      else{
        newlist.new(runner2.value)
        runner2 = runner2.next
      }
    }
    newlist.display()

    return newlist
  }
}
var list = new Listnode(1);
list.next = new Listnode(4);
list.next.next = new Listnode(7);
list.next.next.next = new Listnode(111);
list.next.next.next.next = new Listnode(2);

var list2 = new Listnode(7);
list2.new(2)
list2.new(3)
list2.new(4)

list2.minfront()
