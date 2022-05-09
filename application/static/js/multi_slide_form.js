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
        } else if (input.required) {
            input.classList.add("required-question");
            input.required = required;
        }
    }
}

function validate_slide() {
    let form = document.getElementById("multi-slide-form");
    let slide = document.getElementById("slide" + slide_number);
    for (let input of slide.getElementsByTagName("input")) {
        let validity = input.validity;
        let error_message = input.getAttribute("error_message");
        if (!validity.valid) {
            if (error_message != null) {
                input.setCustomValidity(error_message);
            }
            break;
        } else {
            if (error_message != null) {
                input.setCustomValidity("");
            }
        }
    }
    return form.reportValidity();
}

for (let slide of document.getElementsByClassName("slide")) {
    for (let button of slide.getElementsByClassName("slide-change-btn")) {
        if (button.classList.contains("next-slide")) { 
            button.addEventListener("click", function () {
                if (validate_slide()) {
                    slide_number++;
                    update_slide();
                }
            });
        } else if (button.classList.contains("prev-slide")) {
            button.addEventListener("click", function () {
                slide_number--;
                update_slide();
            });
        }
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

for (let input of document.getElementsByClassName("question")) {
    if (input.attributes.getNamedItem("error_message") != null) {
        input.addEventListener("input", () => {
            input.setCustomValidity("");
        });
    }
}

update_slide();