// crate a function that creates a singly linked list by prompting
// for imput, returns the list when user hits cancel


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
  this.removefront = function(){
    runner = this.next
    var newlist = new Listnode(runner)
    while (runner != null){
      runner = runner.next
      newlist.new(runner)
    }
    return(newlist)
  }
  this.contains = function(val){
    runner = this
    while(runner != null){
      if(runner.value == val){
        return('true')
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
  this.maxback = function(){
    runner = this
    runner2 = this
    var x = runner.value
    while (runner != null){
      if (runner.value>x){
        x = runner.value
        runner = runner.next
      }
      else {
        runner = runner.next
      }
    }
    var newlist = new Listnode()
    runner3 = this
    if (runner3.value == x){
      runner3 = runner3.next
      var newlist = new Listnode(runner3.value)
    }
    else{
      var newlist = new Listnode(runner3.value)
      }

    while(runner2 != null){
      if (runner2.value == x){
        runner2 = runner2.next
      }
      if(runner2.value == runner3.value){
        runner2 = runner2.next
      }
      else{
        newlist.new(runner2.value)
        runner2 = runner2.next
      }
    }
    newlist.new(x)
    newlist.display()
    return(newlist)
  }
}
function promlist(){
  var y = prompt('enter a value')
  newlist = new Listnode(y)
  while(y != null ){
  var y = prompt('enter a value')
  newlist.new(y)
  }
  newlist.display()
  return newlist
}
promlist()
