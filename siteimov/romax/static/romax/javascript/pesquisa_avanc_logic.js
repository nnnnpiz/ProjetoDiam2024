//////////////////wc

const minWcInput = document.getElementById("minwc");
const maxWcInput = document.getElementById("maxwc");


minWcInput.addEventListener("input", function() {

    const minWc = parseInt(minWcInput.value);
    const maxWc = parseInt(maxWcInput.value);


    if (minWc > maxWc) {
        maxWcInput.value = minWcInput.value;
    }
});


maxWcInput.addEventListener("input", function() {

    const minWc = parseInt(minWcInput.value);
    const maxWc = parseInt(maxWcInput.value);


    if (maxWc < minWc) {

        minWcInput.value = maxWcInput.value;
    }
});


//////////////quartos:

const minQuartosInput = document.getElementById("minquartos");
const maxQuartosInput = document.getElementById("maxquartos");


minQuartosInput.addEventListener("input", function() {
    // Parse values to integers
    const minQuartos = parseInt(minQuartosInput.value);
    const maxQuartos = parseInt(maxQuartosInput.value);


    if (minQuartos > maxQuartos) {

        maxQuartosInput.value = minQuartosInput.value;
    }
});


maxQuartosInput.addEventListener("input", function() {

    const minQuartos = parseInt(minQuartosInput.value);
    const maxQuartos = parseInt(maxQuartosInput.value);


    if (maxQuartos < minQuartos) {

        minQuartosInput.value = maxQuartosInput.value;
    }
});

/////area

const minAreaInput = document.getElementById("minarea");
const maxAreaInput = document.getElementById("maxarea");


minAreaInput.addEventListener("input", function() {
    // Parse values to integers
    const minArea = parseInt(minAreaInput.value);
    const maxArea = parseInt(maxAreaInput.value);

    // Check if minarea > maxarea
    if (minArea > maxArea) {
        // Set maxarea value to minarea value
        maxAreaInput.value = minAreaInput.value;
    }
});


maxAreaInput.addEventListener("input", function() {

    const minArea = parseInt(minAreaInput.value);
    const maxArea = parseInt(maxAreaInput.value);


    if (maxArea < minArea) {

        minAreaInput.value = maxAreaInput.value;
    }
});



////////////////////////preco
const minInput = document.getElementById("minpreco");
const maxInput = document.getElementById("maxpreco");

minInput.addEventListener("input", function() {
    const minPrice = parseInt(minInput.value);
    const maxPrice = parseInt(maxInput.value);

    if (minPrice > maxPrice) {
        maxInput.value = minInput.value;
    }
});

maxInput.addEventListener("input", function() {
    const minPrice = parseInt(minInput.value);
    const maxPrice = parseInt(maxInput.value);

    if (maxPrice < minPrice) {
        minInput.value = maxInput.value;
    }
});