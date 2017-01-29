// create a function that shows the clock hand ngeles at a specific time
// measured in seconds...
function clockangles(number){
  var hour= min = seconds = 0
  totaltime = number
  while (totaltime>=43200){
    totaltime = totaltime-43200
  }
  var hourdeg = totaltime/60/60/12*360
  while (totaltime>= 3600){
    totaltime = totaltime-3600
  }
  var mindeg = totaltime/60/60*360
  while (totaltime>=60){
    totaltime= totaltime-60
  }
  var seconddeg = totaltime/60*360
  console.log ("Hour Hand: "+ hourdeg + " | Minuite Hand: "+ mindeg + " | Second hand: "+ seconddeg  )
}

clockangles(119730)
clockangles(3600)
