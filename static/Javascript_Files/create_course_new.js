var tee_name_counter = 0;

function addGolfTee() {
    
    //Golf Tee Name
    var container = document.getElementById("golfTeeContainer");
    
    //creates new tee div inside golfTeeContainer
    var tee_name_div = document.createElement("div")
    tee_name_counter++;
    tee_name_div.id="tee-" + (tee_name_counter);
    container.appendChild(tee_name_div);

    //new container is that div from above
    container = document.getElementById("tee-" + (tee_name_counter));

    //creates new tee name div
    var actual_name_of_tee_div = document.createElement("div");
    actual_name_of_tee_div.id="actual-tee-name-" + (tee_name_counter);
    container.appendChild(actual_name_of_tee_div);

    //new new container is that div from above
    container = document.getElementById("actual-tee-name-" + (tee_name_counter));

    //creates tee name and label inside div
    var newTeeLabel = document.createElement("label")
    newTeeLabel.innerHTML = "Tee " + (tee_name_counter) + " Name";
    newTeeLabel.for = "Tee-" + tee_name_counter + "-name-input";
    var newTeeName = document.createElement("input");
    newTeeName.id = "Tee-" + tee_name_counter + "-name-input";
    newTeeName.type = "text";
    newTeeName.name = "Tee-" + tee_name_counter + "-name-input";
    newTeeName.placeholder = "EX: Red";

    //appends the tee name and label to tee div container
    container.appendChild(newTeeLabel);
    container.appendChild(document.createElement("br"))
    container.appendChild(newTeeName);

    //Slope Rating and Course Rating
    container = document.getElementById("tee-" + (tee_name_counter));
    var slope_and_course_rating = document.createElement("div");
    slope_and_course_rating.id = "Tee-" + (tee_name_counter) + "-slope_and_course_rating";
    container.appendChild(slope_and_course_rating);

    //sets container to slope/course div created above
    container = document.getElementById("Tee-" + (tee_name_counter) + "-slope_and_course_rating");
    var slope_rating_div = document.createElement("div");
    slope_rating_div.id = "slope-rating-tee-" + (tee_name_counter) + "-div";
    container.appendChild(slope_rating_div);

    //sets container to slope_rating div to help w/ flex display
    container = document.getElementById("slope-rating-tee-" + (tee_name_counter) + "-div");
    
    
    var slope_rating_label = document.createElement("label");
    slope_rating_label.innerHTML = "Tee " + (tee_name_counter) + " Slope Rating";
    slope_rating_label.for = "tee-" + (tee_name_counter) + "-slope-rating";
    var slope_rating_input = document.createElement("input");
    slope_rating_input.type = "number";
    slope_rating_input.id = "tee-" + (tee_name_counter) + "-slope-rating";
    slope_rating_input.name = "tee-" + (tee_name_counter) + "-slope-rating";
    slope_rating_input.placeholder = "EX: 141"

    container.appendChild(slope_rating_label);
    container.appendChild(document.createElement("br"));
    container.appendChild(slope_rating_input);

    container = document.getElementById("Tee-" + (tee_name_counter) + "-slope_and_course_rating");

    //creates course_rating div to help w/ flex display
    var course_rating_div = document.createElement("div");
    course_rating_div.id = "course-rating-tee-" + (tee_name_counter) + "-div";
    container.appendChild(course_rating_div);

    container = document.getElementById("course-rating-tee-" + (tee_name_counter) + "-div");

    var course_rating_label = document.createElement("label");
    course_rating_label.innerHTML = "Tee " + (tee_name_counter) + " Course Rating";
    course_rating_label.for = "tee-" + (tee_name_counter) + "-course-rating";
    var course_rating_input = document.createElement("input");
    course_rating_input.type = "number";
    course_rating_input.id = "tee-" + (tee_name_counter) + "-course-rating";
    course_rating_input.name = "tee-" + (tee_name_counter) + "-course-rating";
    course_rating_input.placeholder = "EX: 77.1"

    container.appendChild(course_rating_label);
    container.appendChild(document.createElement("br"));
    container.appendChild(course_rating_input);


    //Golf Tee Holes, Handicaps, Yardage
    
    var course_holes = document.getElementById("number-holes").value;
    var parent_container = document.getElementById("tee-" + (tee_name_counter));
    var i = 1;

    //for the number of holes the course has, that number of rows (divs) are created.

    while (i <= course_holes) {
        
        //add new Div for each hole
        var div_input = document.createElement("div")
        div_input.id = "golfTee-" + tee_name_counter + "Row-" + i;
        parent_container.appendChild(div_input)

        //for each new Div, add par, yardage, and handicap inputs
        var new_div_container = document.getElementById("golfTee-" + tee_name_counter + "Row-" + i);
        
        var hole_par_label = document.createElement("label");
        var hole_yardage_label = document.createElement("label");
        var hole_handicap_label = document.createElement("label");

        hole_par_label.innerHTML = "Hole " + i + " Par"
        hole_par_label.for = "hole_" + i + "_par_at_tee_" + tee_name_counter;

        hole_yardage_label.innerHTML = "Hole " + i + " Yardage"
        hole_yardage_label.for = "hole_" + i + "_yardage_at_tee_" + tee_name_counter;
        
        hole_handicap_label.innerHTML = "Hole " + i + " Handicap"
        hole_handicap_label.for = "hole_" + i + "_handicap_at_tee_" + tee_name_counter;
        
        var hole_par = document.createElement("input");
        var hole_yardage = document.createElement("input");
        var hole_handicap = document.createElement("input");
        
        
        hole_par.id = "hole_" + i + "_par_at_tee_" + tee_name_counter;
        hole_par.name = "hole_" + i + "_par_at_tee_" + tee_name_counter;
        hole_par.type = "number";
        hole_par.step = "1";
        hole_par.maxlength = "1";

        hole_yardage.id = "hole_" + i + "_yardage_at_tee_" + tee_name_counter;
        hole_yardage.name = "hole_" + i + "_yardage_at_tee_" + tee_name_counter;
        hole_yardage.type = "number";
        hole_yardage.maxlength = "1";

        hole_handicap.id = "hole_" + i + "_handicap_at_tee_" + tee_name_counter;
        hole_handicap.name = "hole_" + i + "_handicap_at_tee_" + tee_name_counter;
        hole_handicap.type = "number";
        hole_handicap.maxlength = "1";

        var hole_par_container = document.createElement("div")
        hole_par_container.id = "holeParContainer-" + tee_name_counter + "-Row-" + i;
        new_div_container.appendChild(hole_par_container)

        new_div_container = document.getElementById("holeParContainer-" + tee_name_counter + "-Row-" + i);

        new_div_container.appendChild(hole_par_label);
        new_div_container.appendChild(document.createElement("br"));
        new_div_container.appendChild(hole_par);

        new_div_container = document.getElementById("golfTee-" + tee_name_counter + "Row-" + i);

        var hole_yardage_container = document.createElement("div")
        hole_yardage_container.id = "holeYardageContainer-" + tee_name_counter + "-Row-" + i;
        new_div_container.appendChild(hole_yardage_container)

        new_div_container = document.getElementById("holeYardageContainer-" + tee_name_counter + "-Row-" + i);
        
        new_div_container.appendChild(hole_yardage_label);
        new_div_container.appendChild(document.createElement("br"));
        new_div_container.appendChild(hole_yardage);

        new_div_container = document.getElementById("golfTee-" + tee_name_counter + "Row-" + i);

        var hole_handicap_container = document.createElement("div")
        hole_handicap_container.id = "holeHandicapContainer-" + tee_name_counter + "-Row-" + i;
        new_div_container.appendChild(hole_handicap_container)

        new_div_container = document.getElementById("holeHandicapContainer-" + tee_name_counter + "-Row-" + i);

        new_div_container.appendChild(hole_handicap_label);
        new_div_container.appendChild(document.createElement("br"));
        new_div_container.appendChild(hole_handicap);

        new_div_container = document.getElementById("golfTee-" + tee_name_counter + "Row-" + i);

        i++;

    }
    
}
