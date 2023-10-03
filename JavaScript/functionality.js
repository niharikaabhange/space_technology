function searchAnimal() {
    var searchInput = document.getElementById('searchbar').value.toLowerCase();

    var listItems = document.getElementsByClassName('animals');

    for (var i = 0; i < listItems.length; i++) {
        var listItem = listItems[i];
        var text = listItem.textContent || listItem.innerText;

        text = text.toLowerCase();

        if (text.includes(searchInput)) {
            listItem.style.display = 'block';  // Display the matching item
        } else {
            listItem.style.display = 'none';   // Hide the non-matching item
        }
    }
}

function edmundfunc(event){
event.preventDefault()
document.getElementById("hc").style.display = "none";
document.getElementById("hc").style.display = "block";

}