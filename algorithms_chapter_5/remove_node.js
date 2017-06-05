// create a function that romoves the node with a given value ie fun(list, val)

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

function removeat(x, val){
  runner = x
  if(x.contains(val) != true){
    x.display()
    return x
  }
  if(x.value == val){
    x.removefront()
    x.display()
    return x
  }
  newlist = new Listnode(x.value)
  x = x.next
  while(x != null){
    if(x.next == null){
      newlist.new(x.value)
      newlist.display()
      return newlist
    }
    if(x.next.value == val){
      newlist.new(x.value)
      newlist.new(x.next.next.value)
      x = x.next.next.next
    }
    else{
      newlist.new(x.value)
      x = x.next
    }
  }
  newlist.display()
  return newlist
}
var list = new Listnode(1)
list.new(2)
list.new(3)
list.new(4)
list.new(5)
removeat(list, 3)
