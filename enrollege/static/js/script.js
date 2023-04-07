// Nav bar visibility toggle
$(document).ready(function () {
    $(".navbar-toggler").click(function () {
        $(".dropdown-content").toggle();
    });
});


// Close flash message on keypress
function onButtonPress() {
    $('.alert').alert('close')
}

// Change value when slider moves

let slider = document.querySelector("input[type='range']");
let output = document.getElementById("tuition_value");
output.value = slider.value;

slider.oninput = function () {
    output.value = this.value;
}

// Change slider when value changes
output.oninput = function () {
    slider.value = this.value;
}

// Customize form number type input
jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
jQuery('.quantity').each(function () {
    var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find('.quantity-up'),
        btnDown = spinner.find('.quantity-down'),
        min = input.attr('min'),
        max = input.attr('max');

    btnUp.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue >= max) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });

    btnDown.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });

});

// Ensure form number type input  does not exceed limit
