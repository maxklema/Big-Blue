
// TODO: load JSON file
const fs = require('fs')

var fileData = fs.readFileSync('test.json','utf8')
var jsonData = JSON.parse(fileData);
							
// FUNCTION: calculates the THRU of a player and updates it
function updateThru(player){
  //iterate backwards through each hole until something other than 0 comes up
  var thru = parseInt(jsonData["matchInfo"]["numberHoles"]);
  while(thru>0){
    if (jsonData["players"][player]["scores"][thru] != 0) {
      break;
    }
    thru--;
  }
  //through = last hole with non 0
  return thru;
  
}

// FUNCTION: calculate relation to par of the person
function calculateRelationToPar(player){
  var thru = updateThru(player);
  var currentRelation = 0;
  var currentPar;
  var currentScore;
  for (let i = 1; i <= thru; i++){
    currentPar = jsonData["matchInfo"]["pars"][i];
    currentScore = jsonData["players"][player]["scores"][i];
    currentRelation += currentScore-currentPar;
  }
  return currentRelation;
  
}
//console.log(calculateRelationToPar("Dominic"))

// FUNCTION: Calculates the status of the match between people
function calculateMatchStatus(player1, player2){
  var thru = updateThru(player1);
  var currentPlayer1 = 0;
  var currentPlayer2 = 0; 
  var currentStatus = 0;
  for (let i = 1; i<=thru;i++){
    currentPlayer1 = jsonData["players"][player1]["scores"][i];
    currentPlayer2 = jsonData["players"][player2]["scores"][i];
    if (currentPlayer1 - currentPlayer2 > 0){
      currentStatus += 1;
    } else if (currentPlayer2 - currentPlayer1 > 0){
      currentStatus -= 1;
    }
    
    // positive = player 2 up, negative = player 1 up;
  }
  if (currentStatus == 0){
    return "All Square thru " + thru;
  } else if(currentStatus > 0){
    if (jsonData["matchInfo"]["numberHoles"] - thru == 0){
      return player2.concat(" wins ").concat(currentStatus.toString() + " up")
      
    }else if (currentStatus > jsonData["matchInfo"]["numberHoles"] - thru){
      return player2.concat(" wins ").concat(currentStatus.toString() + "&" + (jsonData["matchInfo"]["numberHoles"] - thru).toString());
    } else {
      return player2.concat(" is up ").concat(currentStatus.toString() + " thru " + thru);
    }
  } else {
    if (jsonData["matchInfo"]["numberHoles"] - thru == 0){
      return player1.concat(" wins ").concat(Math.abs(currentStatus).toString() + " up")
      
    }else if (Math.abs(currentStatus) > jsonData["matchInfo"]["numberHoles"] - thru){
      return player1.concat(" wins ").concat(Math.abs(currentStatus).toString() + "&" + (jsonData["matchInfo"]["numberHoles"] - thru).toString());
    } else {
      return player1.concat(" is up ").concat(Math.abs(currentStatus).toString() + " thru " + thru);
    }
  }
}
console.log(calculateMatchStatus("Nick","Dominic"));
