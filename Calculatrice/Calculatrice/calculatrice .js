let btn = document.querySelectorAll('button');
let input = document.querySelector('input');

btn.forEach(function(button) {
    button.addEventListener("click", function() {
        if (this.textContent === "=") {
            input.value = eval(input.value);
        } else if (this.textContent === "C") {
            input.value = "";
        } else {
            input.value += this.textContent;
        }
    });
});