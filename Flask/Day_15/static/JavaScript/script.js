
document.addEventListener("DOMContentLoaded", function () {

    /* ==============================
       1. Navbar Active Link Highlight
    ============================== */
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentLocation) {
            link.classList.add("active");
        }
    });


    /* ==============================
       2. Login / Signup Form Validation
    ============================== */
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function (event) {

            let isValid = true;

            const inputs = form.querySelectorAll("input[required]");

            inputs.forEach(input => {
                if (input.value.trim() === "") {
                    isValid = false;
                    input.classList.add("is-invalid");
                } else {
                    input.classList.remove("is-invalid");
                }
            });

            // Email validation
            const emailField = form.querySelector("input[type='email']");
            if (emailField) {
                const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
                if (!emailField.value.match(emailPattern)) {
                    isValid = false;
                    emailField.classList.add("is-invalid");
                }
            }

            if (!isValid) {
                event.preventDefault();
                alert("Please fill all required fields correctly.");
            }
        });
    });


    /* ==============================
       3. Flash Message Auto Hide
    ============================== */
    const alerts = document.querySelectorAll(".alert");

    if (alerts.length > 0) {
        setTimeout(() => {
            alerts.forEach(alert => {
                alert.style.display = "none";
            });
        }, 3000); // 3 seconds
    }


    /* ==============================
       4. Confirm Before Delete (Optional)
    ============================== */
    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("Are you sure you want to delete this item?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

});
