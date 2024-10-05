// feedback song 
const form = document.getElementById("mailForm");
form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const form_data = new FormData(form);
    form.reset();
    const response = await fetch("/mail_view", {
        method: 'POST',
        body: form_data
    });
    const data = await response.json();
    console.log(data);
    // alert(`${data.message}`);
    const show = await showTopBar(`${data.message}`);

});

//  Show top bar 
async function showTopBar(param) {
    const topBar = document.getElementById('topBar');
    topBar.textContent = `${param}`;
    topBar.classList.add('show'); // Show the top bar
    topBar.textContent = `${param}`;

    // Hide the top bar after 5 seconds
    setTimeout(() => {
        topBar.classList.remove('show');
    }, 5000);
}

// Them button 

(function () {
    [...document.querySelectorAll(".control")].forEach(button => {
        button.addEventListener("click", function() {
            document.querySelector(".active-btn").classList.remove("active-btn");
            this.classList.add("active-btn");
            document.querySelector(".active").classList.remove("active");
            document.getElementById(button.dataset.id).classList.add("active");
        })
    });
    document.querySelector(".theme-btn").addEventListener("click", () => {
        document.body.classList.toggle("light-mode");
    })
})();
