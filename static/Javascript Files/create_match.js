function doSomething()
{
    if (document.getElementById("event-type").value == "Teams"){
        document.getElementById("row-two").style.display = "flex";
    } else {
        document.getElementById("row-two").style.display = "none";
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
        if (num_spots.value == ""){
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
        if (num_spots.value == ""){
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
        hometeam.value = "";

        let awayteam = document.getElementById("awayteam");
        awayteam.value = "";


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
        if (num_spots.value == ""){
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
