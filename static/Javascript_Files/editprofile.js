function SelectUserBanner(userBanner) {
    //array of all banners
    banner_list=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    banner_image_list=[document.getElementById("banner-one").value, document.getElementById("banner-two").value, document.getElementById("banner-three").value, document.getElementById("banner-four").value, document.getElementById("banner-five").value, document.getElementById("banner-six").value, document.getElementById("banner-seven").value, document.getElementById("banner-eight").value, document.getElementById("banner-nine").value, document.getElementById("banner-ten").value]

    //checks radiobutton onclick
    for (i = 0; i < banner_list.length; i++){
        if (userBanner == banner_image_list[i]){
            radioButton = document.getElementById("banner-"+banner_list[i]);
            radioButton.checked=true;

            //gets image by ID and changes background and border color
            bannerImage = document.getElementById("banner-img-"+banner_list[i]);
            bannerImage.style.borderColor="#408aed";
            bannerImage.style.backgroundColor="#9bbce8";
        }
    }
}


function bannerselect(banner) {
    //array of all banners
    banner_list=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    //checks radiobutton onclick
    for (i = 0; i < banner_list.length; i++){
        if (banner == banner_list[i]){
            radioButton = document.getElementById("banner-"+banner);
            radioButton.checked=true;

            //gets image by ID and changes background and border color
            bannerImage = document.getElementById("banner-img-"+banner);
            bannerImage.style.borderColor="#408aed";
            bannerImage.style.backgroundColor="#9bbce8";


        } else if (banner != banner_list[i]) {
            radioButton = document.getElementById("banner-"+banner_list[i]);
            radioButton.checked=false;

            //gets image by ID and changes background and border color
            bannerImage = document.getElementById("banner-img-"+banner_list[i]);
            bannerImage.style.borderColor="#c0c0c0";
            bannerImage.style.backgroundColor="#f3f3f391";
        }
    }






}

function validateForm() {
    var a = document.forms["Form"]["name"].value;
    var b = document.forms["Form"]["email"].value;
    var c = document.forms["Form"]["team"].value;
    var d = document.forms["Form"]["bio"].value;
    if (((a == null || a == "") || (b == null || b == "")) || ((c == null || c == "") || (d == null || d == ""))) {
        

        //checks full name
        let full_name = document.getElementById("name");
        if (full_name.value == ""){
            full_name.style.borderColor = "red";
        } else {
            full_name.style.borderColor = "black";
        }

        
        //checks email
        let email = document.getElementById("email");
        if (email.value == ""){
            email.style.borderColor = "red";
        } else {
            email.style.borderColor = "black";
        }

        
        //checks team
        let team = document.getElementById("team");
        if (team.value == ""){
            team.style.borderColor = "red";
        } else {
            team.style.borderColor = "black";
        }

        
        //checks bio
        let bio = document.getElementById("bio");
        if (bio.value == ""){
            bio.style.borderColor = "red";
        } else {
            bio.style.borderColor = "black";
        }

        return false;

        

    }
}

function myFunction() {
    document.getElementById("profile-picture-form").style.display = "block";
    document.getElementById("info-form").style.display = "none";
    document.getElementById("profile-banner-form").style.display = "none";
}

function myFunctionTwo() {
    document.getElementById("profile-picture-form").style.display = "none";
    document.getElementById("profile-banner-form").style.display = "none";
    document.getElementById("info-form").style.display = "block";
}

function myFunctionThree() {
    document.getElementById("profile-picture-form").style.display = "none";
    document.getElementById("info-form").style.display = "none";
    document.getElementById("profile-banner-form").style.display = "block";
}

function checkFullName(){
    let full_name = document.getElementById("name");
    if (full_name.value == ""){
        full_name.style.borderColor = "red";
    } else {
        full_name.style.borderColor = "black";
    }
}


function checkEmails() {
    let email = document.getElementById("email");
    if (email.value == ""){
        email.style.borderColor = "red";
    } else {
        email.style.borderColor = "black";
    }
}

function checkTeam() {
    let team = document.getElementById("team");
    if (team.value == ""){
        team.style.borderColor = "red";
    } else {
        team.style.borderColor = "black";
    }
}

function checkBio() {
    let bio = document.getElementById("bio");
    if (bio.value == ""){
        bio.style.borderColor = "red";
    } else {
        bio.style.borderColor = "black";
}

}