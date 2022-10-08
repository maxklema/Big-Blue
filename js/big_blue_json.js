//import JSON;

const playerNames = ["Nick","Dominic","Isaac","Levi", "Max"];
const pars = [4,4,5,4,3,4,3,4,5]
const courseName = "Cherry Hill";
const numHoles = 9;

function createDict(playerNames,pars,courseName,numHoles){
  var matchInfo= {pars:{}, courseName : "", numberHoles:0};
  matchInfo["numberHoles"] = numHoles;
  matchInfo["courseName"] = courseName;
  for(let k = 0; k < pars.length; k++){
    matchInfo["pars"][k+1] = pars[k];
  }
  
  var dict = {"players":{}, "matchInfo":matchInfo};
  
  var defScores = {scores:{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}, thru : 0};
  
  for(let i = 0; i < playerNames.length; i++){
    dict["players"][playerNames[i]] = defScores;
  }
  return dict;
}
//console.log();
var dictstring = JSON.stringify(createDict(playerNames,pars,courseName,numHoles));

var fs = require('fs');

fs.appendFile("test2.json", dictstring, (err) => { 
  if (err) { 
    console.log(err); 
  } 
});

