//dropdown list selection for year

dropdown = document.getElementById('yearDropdown');
let defaultOption = document.createElement('option')
defaultOption.text = 'Select an option';
defaultOption.value = 1970;
dropdown.appendChild(defaultOption)
maxYear = 2029;
minYear = 1970;


//loop to create options that appear in dropdown list.
while (minYear <= maxYear){
    let option = document.createElement('option');
    option.value = minYear;
    option.text = minYear;
    dropdown.appendChild(option);
    minYear += 1;
}
