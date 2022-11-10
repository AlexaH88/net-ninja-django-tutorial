const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');


// take value (val)
const slugify = (val) => {
    // return the value as a string, lower case and trim any whitespaces from the ends
    return val.toString().toLowerCase().trim()
        // create regex to replace symbols with more common usage in urls
        // replace global (g) ampersand with -and-
        .replace(/&/g, '-and-')
        // replace spaces, non word characters and dashes with a single dash
        .replace(/[\s\W-]+/g, '-')
};


// listen for key up (typing) event from the user on titleInput field
// e = event. Callback function takes the event parameter
titleInput.addEventListener('keyup', (e) => {
    // set the slugInput value to the value inputted into titleInput and slugify it
    slugInput.setAttribute('value', slugify(titleInput.value));
});