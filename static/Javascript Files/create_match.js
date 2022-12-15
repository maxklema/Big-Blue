function doSomething()
{
    if (document.getElementById("event-type").value == "Teams"){
        document.getElementById("row-two").style.display = "flex";
        let hometeam = document.getElementById("hometeam");
        let awayteam = document.getElementById("awayteam");

        if (hometeam.value == "n/a"){
            hometeam.value = ""
        }
        if (awayteam.value == "n/a"){
            awayteam.value = ""
        }
        
    } else {
        document.getElementById("row-two").style.display = "none";
        let hometeam = document.getElementById("hometeam");
        hometeam.value = "n/a";

        let awayteam = document.getElementById("awayteam");
        awayteam.value = "n/a";
    }
}

function validateForm(){
    var a = document.getElementById("match-name").value;
    var b = document.getElementById("hometeam").value;
    var c = document.getElementById("awayteam").value;
    var d = document.getElementById("numberspots").value;
    var e = document.getElementById("password-one").value;
    if (((((a == "") || (a == null)) || ((b == "") || (b == null))) || (((c == "") || (c == null)) || ((d == "") || (d == null)))) || ((e == "") || (e == null))) {
        


        let match_name = document.getElementById("match-name");
        if (match_name.value == ""){
           match_name.style.borderColor = "red";
        } else {
            match_name.style.borderColor = "black";
        }


        let hometeam = document.getElementById("hometeam");
        if (hometeam.value == ""){
            hometeam.style.borderColor = "red";
        } else {
            hometeam.style.borderColor = "black";
        }

        
        let awayteam = document.getElementById("awayteam");
        if (awayteam.value == ""){
            awayteam.style.borderColor = "red";
        } else {
            awayteam.style.borderColor = "black";
        }
        
        
        let num_spots = document.getElementById("numberspots");
        if (num_spots.value == "" || num_spots.value < 0){
            num_spots.style.borderColor = "red";
        } else {
            num_spots.style.borderColor = "black";
        }

        let password = document.getElementById("password-one");
        if (password.value == ""){
            password.style.borderColor = "red";
        } else {
            password.style.borderColor = "black";
        }


        return false;
    }

}


function validateFormTwo(){
    var a = document.getElementById("match-name").value;
    var b = document.getElementById("hometeam").value;
    var c = document.getElementById("awayteam").value;
    var d = document.getElementById("numberspots").value;
    var e = document.getElementById("password-one").value;
    var f = document.getElementById("event-type").value;

    if (((((a == "") || (a == null)) || ((b == "") || (b == null))) || (((c == "") || (c == null)) || ((d == "") || (d == null)))) || ((e == "") || (e == null))) {
        


        let match_name = document.getElementById("match-name");
        if (match_name.value == ""){
           match_name.style.borderColor = "red";
        } else {
            match_name.style.borderColor = "black";
        }


        let hometeam = document.getElementById("hometeam");
        if (hometeam.value == ""){
            hometeam.style.borderColor = "red";
        } else {
            hometeam.style.borderColor = "black";
        }

        
        let awayteam = document.getElementById("awayteam");
        if (awayteam.value == ""){
            awayteam.style.borderColor = "red";
        } else {
            awayteam.style.borderColor = "black";
        }
        
        
        let num_spots = document.getElementById("numberspots");
        if ((num_spots.value == "" || num_spots.value < 0) || num_spots.value > 9){
            num_spots.style.borderColor = "red";
        } else {
            num_spots.style.borderColor = "black";
        }

        let password = document.getElementById("password-one");
        if (password.value == ""){
            password.style.borderColor = "red";
        } else {
            password.style.borderColor = "black";
        }


        return false;

    } else if (f == "Singles") {
        let hometeam = document.getElementById("hometeam");
        hometeam.value = "n/a";

        let awayteam = document.getElementById("awayteam");
        awayteam.value = "n/a";


    }
}

function hidename(){
    let match_name = document.getElementById("match-name");
        if (match_name.value == ""){
           match_name.style.borderColor = "red";
        } else {
            match_name.style.borderColor = "black";
        }

}

function hidehometeam(){
    let hometeam = document.getElementById("hometeam");
        if (hometeam.value == ""){
            hometeam.style.borderColor = "red";
        } else {
            hometeam.style.borderColor = "black";
        }
}

function hideawayteam() {
    let awayteam = document.getElementById("awayteam");
        if (awayteam.value == ""){
            awayteam.style.borderColor = "red";
        } else {
            awayteam.style.borderColor = "black";
        }
}

function hidenumberofplayers() {
    let num_spots = document.getElementById("numberspots");
        if (num_spots.value == "" || num_spots.value < 0){
            num_spots.style.borderColor = "red";
        } else {
            num_spots.style.borderColor = "black";
        }
}

function hidepassword() {
    let password = document.getElementById("password-one");
        if (password.value == ""){
            password.style.borderColor = "red";
        } else {
            password.style.borderColor = "black";
        }
}
