const slides = document.querySelectorAll('.slide'),
      dots = document.querySelectorAll('.slide-counter');
    
let index = 0;

const activeSlide = n => {
    for(i of slides) {
        i.classList.remove('active');
    }
    slides[n].classList.add('active');
}

const activeDot = n => {
    for(i of dots) {
        i.classList.remove('active');
    }
    dots[n].classList.add('active');
}

const prepareCurrentSlide = ind => {
    activeSlide(index);
    activeDot(index);
}

dots.forEach((item, indexDot) => {
    item.addEventListener('click', () => {
        index = indexDot;
        prepareCurrentSlide(index);
    })
})

document.getElementById('back-1').addEventListener('click', function() {
    document.getElementById('slide-2').classList.remove('active');
    document.getElementById('slide-1').classList.add('active');
    activeDot(0);
});

document.getElementById('back-2').addEventListener('click', function() {
    document.getElementById('slide-3').classList.remove('active');
    document.getElementById('slide-2').classList.add('active');
    activeDot(1);
});

//Check if all the inputs are done for the first slide

const slide1_questions = document.querySelectorAll('.ques1');
var missing_input_1 = [];
document.getElementById('next-1').addEventListener('click', function() {
    for(var i = 0; i < slide1_questions.length; i++){
        if (slide1_questions[i].value == '') {
            missing_input_1.push(slide1_questions[i].value)
        }
    console.log(missing_input_1);
    if (missing_input_1.length == 0){
        document.getElementById('next-1').disabled = 'false';
        console.log('Ok!')
        document.getElementById('slide-1').classList.remove('active');
        document.getElementById('slide-2').classList.add('active');
        activeDot(1);
    }else{
        document.getElementById('next-1').disabled = 'true'; // doesn't work for some reason
        console.log('Missing Input!')
        activeDot(0);
        document.getElementById('missing-text-1').innerHTML = "Missing Input!";
        }
    }
});

const slide2_questions = document.querySelectorAll('.ques2');
var missing_input_2 = []; 
document.getElementById('next-2').addEventListener('click', function() {
    for(var i = 0; i < slide2_questions.length; i++){
        if (slide1_questions[i].value == '') {
            missing_input_2.push(slide2_questions[i].value)
        }
    console.log(missing_input_2);
    if (missing_input_2.length == 0){
        document.getElementById('next-1').disabled = 'false';
        console.log('Ok!')
        document.getElementById('slide-2').classList.remove('active');
        document.getElementById('slide-3').classList.add('active');
        activeDot(2);
    }else{
        document.getElementById('next-1').disabled = 'true'; // doesn't work for some reason
        console.log('Missing Input!')
        activeDot(1);
        }
    }
});

