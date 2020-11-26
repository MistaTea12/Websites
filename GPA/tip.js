function calculateTip() {
    var total = 10;

    var cost = Number(document.getElementById("cost").value);
    var tip = Number(document.getElementById("tip").value);
    var persons = Number(document.getElementById('people').value);
    tip = (tip/100)*cost;
    total = cost + tip;
    if (total > 0) {
    
        document.getElementById('resultTip').innerHTML = "$" + tip;
        document.getElementById('total').innerHTML = "$" + total;
        document.getElementById('perPerson').innerHTML = "$" + total/persons;
    }

    else {
        alert("No values entered. Make sure a value is entered for cost and tip.");
        
    }

}