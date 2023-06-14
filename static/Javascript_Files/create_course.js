function onload(){
    hideparholes();
}


function validateForm(){
    //all input boxes
    var a = document.getElementById("course-name").value;
    var b = document.getElementById("number-holes").value;
    var c = document.getElementById("city").value;
    var d = document.getElementById("holepar1").value;
    var e = document.getElementById("holepar2").value;
    var f = document.getElementById("holepar3").value;
    var g = document.getElementById("holepar4").value;
    var h = document.getElementById("holepar5").value;
    var i = document.getElementById("holepar6").value;
    var j = document.getElementById("holepar7").value;
    var k = document.getElementById("holepar8").value;
    var l = document.getElementById("holepar9").value;
    var m = document.getElementById("holepar10").value;
    var n = document.getElementById("holepar11").value;
    var o = document.getElementById("holepar12").value;
    var p = document.getElementById("holepar13").value;
    var q = document.getElementById("holepar14").value;
    var r = document.getElementById("holepar15").value;
    var s = document.getElementById("holepar16").value;
    var t = document.getElementById("holepar17").value;
    var u = document.getElementById("holepar18").value;

    var inputBoxes = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u];
    if (b == "18")
        for (var i = 0; i < inputBoxes.length; i++){
            if (inputBoxes[i] == "" || inputBoxes[i] == null){
                let num_holes = document.getElementById("number-holes");
                if (num_holes.value == ""){
                    num_holes.style.borderColor = "red";
                } else {
                    num_holes.style.borderColor = "black";
                }
        
                let city = document.getElementById("city");
                if (city.value == ""){
                    city.style.borderColor = "red";
                } else {
                    city.style.borderColor = "black";
                }
        
                
                let course_name = document.getElementById("course-name");
                if (course_name.value == ""){
                    course_name.style.borderColor = "red";
                } else {
                    course_name.style.borderColor = "black";
                }
                
                
                let parone = document.getElementById("holepar1");
                if (parone.value == ""){
                    parone.style.borderColor = "red";
                } else {
                    parone.style.borderColor = "black";
                }
        
                let partwo = document.getElementById("holepar2");
                if (partwo.value == ""){
                    partwo.style.borderColor = "red";
                } else {
                    partwo.style.borderColor = "black";
                }
        
                let parthree = document.getElementById("holepar3");
                if (parthree.value == ""){
                    parthree.style.borderColor = "red";
                } else {
                    parthree.style.borderColor = "black";
                }
        
                let parfour = document.getElementById("holepar4");
                if (parfour.value == ""){
                    parfour.style.borderColor = "red";
                } else {
                    parfour.style.borderColor = "black";
                }
        
                let parfive = document.getElementById("holepar5");
                if (parfive.value == ""){
                    parfive.style.borderColor = "red";
                } else {
                    parfive.style.borderColor = "black";
                }
        
                let parsix = document.getElementById("holepar6");
                if (parsix.value == ""){
                    parsix.style.borderColor = "red";
                } else {
                    parsix.style.borderColor = "black";
                }
        
                let parseven = document.getElementById("holepar7");
                if (parseven.value == ""){
                    parseven.style.borderColor = "red";
                } else {
                    parseven.style.borderColor = "black";
                }
        
                let pareight = document.getElementById("holepar8");
                if (pareight.value == ""){
                    pareight.style.borderColor = "red";
                } else {
                    pareight.style.borderColor = "black";
                }
        
                let parnine = document.getElementById("holepar9");
                if (parnine.value == ""){
                    parnine.style.borderColor = "red";
                } else {
                    parnine.style.borderColor = "black";
                }
        
                let parten = document.getElementById("holepar10");
                if (parten.value == ""){
                    parten.style.borderColor = "red";
                } else {
                    parten.style.borderColor = "black";
                }
        
                let pareleven = document.getElementById("holepar11");
                if (pareleven.value == ""){
                    pareleven.style.borderColor = "red";
                } else {
                    pareleven.style.borderColor = "black";
                }
        
                let partwelve = document.getElementById("holepar12");
                if (partwelve.value == ""){
                    partwelve.style.borderColor = "red";
                } else {
                    partwelve.style.borderColor = "black";
                }
        
                let parthirteen = document.getElementById("holepar13");
                if (parthirteen.value == ""){
                    parthirteen.style.borderColor = "red";
                } else {
                    parthirteen.style.borderColor = "black";
                }
        
                let parfourteen = document.getElementById("holepar14");
                if (parfourteen.value == ""){
                    parfourteen.style.borderColor = "red";
                } else {
                    parfourteen.style.borderColor = "black";
                }
        
                let parfifteen = document.getElementById("holepar15");
                if (parfifteen.value == ""){
                    parfifteen.style.borderColor = "red";
                } else {
                    parfifteen.style.borderColor = "black";
                }
        
                let parsixteen = document.getElementById("holepar16");
                if (parsixteen.value == ""){
                    parsixteen.style.borderColor = "red";
                } else {
                    parsixteen.style.borderColor = "black";
                }
        
                let parseventeen = document.getElementById("holepar17");
                if (parseventeen.value == ""){
                    parseventeen.style.borderColor = "red";
                } else {
                    parseventeen.style.borderColor = "black";
                }
        
                let pareightteen = document.getElementById("holepar18");
                if (pareightteen.value == ""){
                    pareightteen.style.borderColor = "red";
                } else {
                    pareightteen.style.borderColor = "black";
                }
        
                return false;
            
        }
    } else if (b == "9"){
        for (var i = 0; i < 12; i++){
            if (inputBoxes[i] == "" || inputBoxes[i] == null){
                let num_holes = document.getElementById("number-holes");
                if (num_holes.value == ""){
                    num_holes.style.borderColor = "red";
                } else {
                    num_holes.style.borderColor = "black";
                }
        
        
                let city = document.getElementById("city");
                if (city.value == ""){
                    city.style.borderColor = "red";
                } else {
                    city.style.borderColor = "black";
                }
        
                
                let course_name = document.getElementById("course-name");
                if (course_name.value == ""){
                    course_name.style.borderColor = "red";
                } else {
                    course_name.style.borderColor = "black";
                }
                
                
                let parone = document.getElementById("holepar1");
                if (parone.value == ""){
                    parone.style.borderColor = "red";
                } else {
                    parone.style.borderColor = "black";
                }
        
                let partwo = document.getElementById("holepar2");
                if (partwo.value == ""){
                    partwo.style.borderColor = "red";
                } else {
                    partwo.style.borderColor = "black";
                }
        
                let parthree = document.getElementById("holepar3");
                if (parthree.value == ""){
                    parthree.style.borderColor = "red";
                } else {
                    parthree.style.borderColor = "black";
                }
        
                let parfour = document.getElementById("holepar4");
                if (parfour.value == ""){
                    parfour.style.borderColor = "red";
                } else {
                    parfour.style.borderColor = "black";
                }
        
                let parfive = document.getElementById("holepar5");
                if (parfive.value == ""){
                    parfive.style.borderColor = "red";
                } else {
                    parfive.style.borderColor = "black";
                }
        
                let parsix = document.getElementById("holepar6");
                if (parsix.value == ""){
                    parsix.style.borderColor = "red";
                } else {
                    parsix.style.borderColor = "black";
                }
        
                let parseven = document.getElementById("holepar7");
                if (parseven.value == ""){
                    parseven.style.borderColor = "red";
                } else {
                    parseven.style.borderColor = "black";
                }
        
                let pareight = document.getElementById("holepar8");
                if (pareight.value == ""){
                    pareight.style.borderColor = "red";
                } else {
                    pareight.style.borderColor = "black";
                }
        
                let parnine = document.getElementById("holepar9");
                if (parnine.value == ""){
                    parnine.style.borderColor = "red";
                } else {
                    parnine.style.borderColor = "black";
                }

                return false;
            }
        }
    }

}

function hidecity(){
    let city = document.getElementById("city");
    if (city.value == ""){
        city.style.borderColor = "red";
    } else {
        city.style.borderColor = "black";
    }
}

function hidename(){
    let course_name = document.getElementById("course-name");
    if (course_name.value == ""){
        course_name.style.borderColor = "red";
    } else {
        course_name.style.borderColor = "black";
    }
}

function hideparone(){
    let parone = document.getElementById("holepar1");
    if (parone.value == ""){
        parone.style.borderColor = "red";
    } else {
        parone.style.borderColor = "black";
    }
}

function hidepartwo(){
    let partwo = document.getElementById("holepar2");
    if (partwo.value == ""){
        partwo.style.borderColor = "red";
    } else {
        partwo.style.borderColor = "black";
    }
}

function hideparthree(){
    let parthree = document.getElementById("holepar3");
    if (parthree.value == ""){
        parthree.style.borderColor = "red";
    } else {
        parthree.style.borderColor = "black";
    }
}

function hideparfour(){
    let parfour = document.getElementById("holepar4");
    if (parfour.value == ""){
        parfour.style.borderColor = "red";
    } else {
        parfour.style.borderColor = "black";
    }
}

function hideparfive(){
    let parfive = document.getElementById("holepar5");
    if (parfive.value == ""){
        parfive.style.borderColor = "red";
    } else {
        parfive.style.borderColor = "black";
    }
}

function hideparsix(){
    let parsix = document.getElementById("holepar6");
    if (parsix.value == ""){
        parsix.style.borderColor = "red";
    } else {
        parsix.style.borderColor = "black";
    }
}

function hideparseven(){
    let parseven = document.getElementById("holepar7");
    if (parseven.value == ""){
        parseven.style.borderColor = "red";
    } else {
        parseven.style.borderColor = "black";
    }
}

function hidepareight(){
    let pareight = document.getElementById("holepar8");
    if (pareight.value == ""){
        pareight.style.borderColor = "red";
    } else {
        pareight.style.borderColor = "black";
    }
}

function hideparnine(){
    let parnine = document.getElementById("holepar9");
    if (parnine.value == ""){
        parnine.style.borderColor = "red";
    } else {
        parnine.style.borderColor = "black";
    }
}

function hideparten(){
    let parten = document.getElementById("holepar10");
    if (parten.value == ""){
        parten.style.borderColor = "red";
    } else {
        parten.style.borderColor = "black";
    } 
}

function hidepareleven(){
    let pareleven = document.getElementById("holepar11");
    if (pareleven.value == ""){
        pareleven.style.borderColor = "red";
    } else {
        pareleven.style.borderColor = "black";
    }
}

function hidepartwelve(){
    let partwelve = document.getElementById("holepar12");
    if (partwelve.value == ""){
        partwelve.style.borderColor = "red";
    } else {
        partwelve.style.borderColor = "black";
    }
}

function hideparthirteen(){
    let parthirteen = document.getElementById("holepar13");
    if (parthirteen.value == ""){
        parthirteen.style.borderColor = "red";
    } else {
        parthirteen.style.borderColor = "black";
    }
}

function hideparfourteen(){
    let parfourteen = document.getElementById("holepar14");
    if (parfourteen.value == ""){
        parfourteen.style.borderColor = "red";
    } else {
        parfourteen.style.borderColor = "black";
    }
}

function hideparfifteen(){
    let parfifteen = document.getElementById("holepar15");
    if (parfifteen.value == ""){
        parfifteen.style.borderColor = "red";
    } else {
        parfifteen.style.borderColor = "black";
    }
}

function hideparsixteen(){
    let parsixteen = document.getElementById("holepar16");
    if (parsixteen.value == ""){
        parsixteen.style.borderColor = "red";
    } else {
        parsixteen.style.borderColor = "black";
    }

}

function hideparseventeen(){
    let parseventeen = document.getElementById("holepar17");
    if (parseventeen.value == ""){
        parseventeen.style.borderColor = "red";
    } else {
        parseventeen.style.borderColor = "black";
    }
}

function hidepareightteen(){
    let pareightteen = document.getElementById("holepar18");
    if (pareightteen.value == ""){
        pareightteen.style.borderColor = "red";
    } else {
        pareightteen.style.borderColor = "black";
    }
}






function hideparholes(){
    var value = document.getElementById("number-holes").value
    
    if (value != "18"){
        
        
        document.getElementById("holepar10").value = "";
        document.getElementById("holepar10").style.display = "none";
        document.getElementById("label-10").style.display = "none";

        document.getElementById("holepar11").value = "";
        document.getElementById("holepar11").style.display = "none";
        document.getElementById("label-11").style.display = "none";

        document.getElementById("holepar12").value = "";
        document.getElementById("holepar12").style.display = "none";
        document.getElementById("label-12").style.display = "none";

        document.getElementById("holepar13").value = "";
        document.getElementById("holepar13").style.display = "none";
        document.getElementById("label-13").style.display = "none";

        document.getElementById("holepar14").value = "";
        document.getElementById("holepar14").style.display = "none";
        document.getElementById("label-14").style.display = "none";

        document.getElementById("holepar15").value = "";
        document.getElementById("holepar15").style.display = "none";
        document.getElementById("label-15").style.display = "none";

        document.getElementById("holepar16").value = "";
        document.getElementById("holepar16").style.display = "none";
        document.getElementById("label-16").style.display = "none";

        document.getElementById("holepar17").value = "";
        document.getElementById("holepar17").style.display = "none";
        document.getElementById("label-17").style.display = "none";

        document.getElementById("holepar18").value = "";
        document.getElementById("holepar18").style.display = "none";
        document.getElementById("label-18").style.display = "none";

        document.getElementById("row-eight").style.display = "none";
        document.getElementById("row-nine").style.display = "none";
        document.getElementById("row-ten").style.display = "none";
        document.getElementById("row-eleven").style.display = "none";

        document.getElementById("inner-div").style.display = "none";
        document.getElementById("inner-divTwo").style.display = "none";


    } else if (document.getElementById("number-holes").value == "18"){
        document.getElementById("holepar10").style.display = "";
        document.getElementById("label-10").style.display = "";

        //document.getElementById("holepar11").value = "";
        document.getElementById("holepar11").style.display = "";
        document.getElementById("label-11").style.display = "";

        //document.getElementById("holepar12").value = "";
        document.getElementById("holepar12").style.display = "";
        document.getElementById("label-12").style.display = "";

        //document.getElementById("holepar13").value = "";
        document.getElementById("holepar13").style.display = "";
        document.getElementById("label-13").style.display = "";

        //document.getElementById("holepar14").value = "";
        document.getElementById("holepar14").style.display = "";
        document.getElementById("label-14").style.display = "";

        //document.getElementById("holepar15").value = "";
        document.getElementById("holepar15").style.display = "";
        document.getElementById("label-15").style.display = "";

        //document.getElementById("holepar16").value = "";
        document.getElementById("holepar16").style.display = "";
        document.getElementById("label-16").style.display = "";

        //document.getElementById("holepar17").value = "";
        document.getElementById("holepar17").style.display = "";
        document.getElementById("label-17").style.display = "";

        //document.getElementById("holepar18").value = "";
        document.getElementById("holepar18").style.display = "";
        document.getElementById("label-18").style.display = "";

        document.getElementById("row-eight").style.display = "flex";
        document.getElementById("row-nine").style.display = "flex";
        document.getElementById("row-ten").style.display = "flex";
        document.getElementById("row-eleven").style.display = "flex";
        
        document.getElementById("inner-div").style.display = "";
        document.getElementById("inner-divTwo").style.display = "";
    }
    
    
}

function hideparholes_handicap(){
    var value = document.getElementById("number-holes").value
    
    if (value != "18"){
        
        
        document.getElementById("holepar10").value = "";
        document.getElementById("holepar10").style.display = "none";
        document.getElementById("label-10").style.display = "none";

        document.getElementById("holepar11").value = "";
        document.getElementById("holepar11").style.display = "none";
        document.getElementById("label-11").style.display = "none";

        document.getElementById("holepar12").value = "";
        document.getElementById("holepar12").style.display = "none";
        document.getElementById("label-12").style.display = "none";

        document.getElementById("holepar13").value = "";
        document.getElementById("holepar13").style.display = "none";
        document.getElementById("label-13").style.display = "none";

        document.getElementById("holepar14").value = "";
        document.getElementById("holepar14").style.display = "none";
        document.getElementById("label-14").style.display = "none";

        document.getElementById("holepar15").value = "";
        document.getElementById("holepar15").style.display = "none";
        document.getElementById("label-15").style.display = "none";

        document.getElementById("holepar16").value = "";
        document.getElementById("holepar16").style.display = "none";
        document.getElementById("label-16").style.display = "none";

        document.getElementById("holepar17").value = "";
        document.getElementById("holepar17").style.display = "none";
        document.getElementById("label-17").style.display = "none";

        document.getElementById("holepar18").value = "";
        document.getElementById("holepar18").style.display = "none";
        document.getElementById("label-18").style.display = "none";

        document.getElementById("row-twelve").style.display = "none";
        document.getElementById("row-thirteen").style.display = "none";
        document.getElementById("row-fourteen").style.display = "none";
        document.getElementById("row-fifteen").style.display = "none";
        document.getElementById("row-sixteen").style.display = "none";
        document.getElementById("row-seventeen").style.display = "none";
        document.getElementById("row-eighteen").style.display = "none";
        document.getElementById("row-nineteen").style.display = "none";
        document.getElementById("row-twenty").style.display = "none";

        document.getElementById("row-eleven").style.marginBottom = "40px";

        document.getElementById("inner-div").style.display = "none";
        document.getElementById("inner-divTwo").style.display = "none";


    } else if (document.getElementById("number-holes").value == "18"){
        document.getElementById("holepar10").style.display = "";
        document.getElementById("label-10").style.display = "";

        //document.getElementById("holepar11").value = "";
        document.getElementById("holepar11").style.display = "";
        document.getElementById("label-11").style.display = "";

        //document.getElementById("holepar12").value = "";
        document.getElementById("holepar12").style.display = "";
        document.getElementById("label-12").style.display = "";

        //document.getElementById("holepar13").value = "";
        document.getElementById("holepar13").style.display = "";
        document.getElementById("label-13").style.display = "";

        //document.getElementById("holepar14").value = "";
        document.getElementById("holepar14").style.display = "";
        document.getElementById("label-14").style.display = "";

        //document.getElementById("holepar15").value = "";
        document.getElementById("holepar15").style.display = "";
        document.getElementById("label-15").style.display = "";

        //document.getElementById("holepar16").value = "";
        document.getElementById("holepar16").style.display = "";
        document.getElementById("label-16").style.display = "";

        //document.getElementById("holepar17").value = "";
        document.getElementById("holepar17").style.display = "";
        document.getElementById("label-17").style.display = "";

        //document.getElementById("holepar18").value = "";
        document.getElementById("holepar18").style.display = "";
        document.getElementById("label-18").style.display = "";

        document.getElementById("row-twelve").style.display = "flex";
        document.getElementById("row-thirteen").style.display = "flex";
        document.getElementById("row-fourteen").style.display = "flex";
        document.getElementById("row-fifteen").style.display = "flex";
        document.getElementById("row-sixteen").style.display = "flex";
        document.getElementById("row-seventeen").style.display = "flex";
        document.getElementById("row-eighteen").style.display = "flex";
        document.getElementById("row-nineteen").style.display = "flex";
        document.getElementById("row-twenty").style.display = "flex";

        document.getElementById("row-eleven").style.marginBottom = "0px";
        
        document.getElementById("inner-div").style.display = "";
        document.getElementById("inner-divTwo").style.display = "";
    }
    
    
}