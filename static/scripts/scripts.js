function handleSubmit(event) {
    event.preventDefault();
    console.log('START handleSubmit');
    var selectedRadioValue = getSelectedRadioValue();

    document.getElementById('message').textContent = 'טוען...';
    var mainField = document.getElementById('main_field').value;
    var webField = document.getElementById('web_field').value;
    var csField = document.getElementById('cs_field').value;
    var ckField = document.getElementById('ck_field').value;

    console.log('selectedRadioValue');
    console.log(selectedRadioValue);
    fetch('/success', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "main_field": mainField,
            "main_field": mainField,
            "web_field": webField,
            "cs_field": csField,
            "ck_field": ckField,
            "selectedRadioValue": selectedRadioValue,
        })
    })
        // .then(response => response.json())
        .then(data => {
            console.log(data)
            if (selectedRadioValue == 0) {
                document.getElementById('message').textContent =
                    'המוצר נוסף בהצלחה!'
            } else {
                document.getElementById('message').textContent =
                    '30 מוצרים נוספו בהצלחה!'
            }
        })
}

function handleFindCategory() {
    console.log('START handleFindCategory');

    document.getElementById('message').textContent = 'טוען...';
    var mainField = document.getElementById('main_field').value;
    var webField = document.getElementById('web_field').value;
    var csField = document.getElementById('cs_field').value;
    var ckField = document.getElementById('ck_field').value;
    

    fetch('/get_category', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "main_field": mainField,
            "web_field": webField,
            "cs_field": csField,
            "ck_field": ckField,
        })
    })

        // routes.py /get_category
        .then(response => response.json()) // Parse the JSON of the response
        .then(data => {
            console.log('data');
            console.log(data);
            {document.getElementById('message').textContent = JSON.stringify(data);}

            // Clear existing content
            var messageElement = document.getElementById('message');
            messageElement.innerHTML = '';

            // Create radio buttons
            data.forEach(category => {
                var label = document.createElement('label');
                label.innerHTML = category.name;

                var radioButton = document.createElement('input');
                radioButton.type = 'radio';
                radioButton.name = 'category';
                radioButton.value = category.id;

                label.prepend(radioButton);

                messageElement.appendChild(label);
                messageElement.appendChild(document.createElement('br'));
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function getSelectedRadioValue() {

    console.log("getSelectedRadioValue")
    var sValue = document.querySelector('input[name="category"]:checked');
    if (sValue != null) {
        sValue = sValue.value
        console.log("sValue")
        console.log(sValue)
        return sValue;
    }
    return 0;

    // var radioButtons = document.getElementsByName('category');
    // console.log(radioButtons)
    // for (var radioButton of radioButtons) {console.log(radioButton)
    //     if (radioButton.checked) {return radioButton.value;}}
}

function checkInput() {
    var mainField = document.getElementById('main_field');
    var webField = document.getElementById('web_field');
    var ckField = document.getElementById('ck_field');
    var csField = document.getElementById('cs_field');
    var start_button = document.getElementById('start_button');
    var cat_button = document.getElementById('cat_button');
    start_button.disabled = !mainField.value.trim() || !webField.value.trim() || !ckField.value.trim() || !csField.value.trim();
    cat_button.disabled = !webField.value.trim() || !ckField.value.trim() || !csField.value.trim();

    localStorage.setItem('web_field', webField.value);
    localStorage.setItem('cs_field', csField.value);
    localStorage.setItem('ck_field', ckField.value);

}

// Call checkInput on page load in case the text field is pre-filled
window.onload = checkInput;

function initializeConfig() {
    console.log('START: initializeConfig()')

    var web_field = localStorage.getItem('web_field');
    var ck_field = localStorage.getItem('ck_field');
    var cs_field = localStorage.getItem('cs_field');

    console.log(web_field)
    console.log(ck_field)
    console.log(cs_field)

    document.getElementById('web_field').value = web_field;
    document.getElementById('ck_field').value = ck_field;
    document.getElementById('cs_field').value = cs_field;


    if (web_field != null && ck_field != null && cs_field != null){
        handleFindCategory();
    }

}

window.onload = initializeConfig;


function showWooSettings() {
    var infoDiv = document.getElementById("infoText");
    if (infoDiv.style.display === "none") {
        infoDiv.style.display = "block";
    } else {
        infoDiv.style.display = "none";
    }
}