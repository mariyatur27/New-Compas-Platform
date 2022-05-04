var slide_number = parseInt(document.getElementsByClassName("first-slide")[0].id.replace("slide", ""));
var max_slide = parseInt(document.getElementsByClassName("last-slide")[0].id.replace("slide", ""));

function update_slide() {
    let slide = document.getElementById("slide" + slide_number);
    slide.classList.add("active");
    toggle_required(slide, true);
    for (var i = 1; i <= max_slide; i++) {
        if (i != slide_number) {
            slide = document.getElementById("slide" + i);
            slide.classList.remove("active");
            toggle_required(slide, false);
        }
    }
}

function toggle_required(slide, required) {
    let inputs = slide.getElementsByTagName("input");
    for (let input of inputs) {
        if (input.classList.contains("required-question")) {
            input.required = required;
        }
    }
}

function validate_slide() {
    return document.getElementById("multi-slide-form").reportValidity();
}

for (let slide of document.getElementsByClassName("slide")) {
    for (let button of slide.getElementsByClassName("next-slide")) {
        button.addEventListener("click", function () {
            if (validate_slide()) {
                slide_number++;
                update_slide();
            }
        });
    }
    for (let button of slide.getElementsByClassName("prev-slide")) {
        button.addEventListener("click", function () {
            slide_number--;
            update_slide();
        });
    }
}

for (let slideCounter of document.getElementsByClassName("slide-counter")) {
    slideCounter.addEventListener("click", function () {
        let new_slide_number = parseInt(this.id.replace("slide-counter", ""));
        if (new_slide_number != slide_number) {
            if (new_slide_number < slide_number || (new_slide_number == slide_number+1 && validate_slide())) {
                slide_number = new_slide_number;
                update_slide();
            }
        }
    });
}

update_slide();