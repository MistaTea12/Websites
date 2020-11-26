function calculateGPA() {
    var gpa = 0;
    for (var x = 1; x < 8; x++) {

        var elements = document.getElementById(x).elements;
        var result = 0;
        var grades = 0;
        var weight = 0;

        for (var i = 0, element; element = elements[i++];) {
            if ((Number(element.value) > 0) && (element.id !== "weight")) {
                result += Number(element.value);
                grades += 1;
            }
            if (element.id === "weight") {
                weight = Number(element.value);
            }
            

        }
        if (result > 0) {
            gpa += (((result) / grades) * (weight / 100));
            document.getElementById('result' + x.toString()).innerHTML = ((result) / grades) + " Weighted: " + (((result) / grades) * (weight / 100));
            document.getElementById('gpa').innerHTML = gpa;
        }

    }
    if (gpa === 0){
        alert("No values entered. Make sure at least one grade is entered and related weight.");
        
    }

}