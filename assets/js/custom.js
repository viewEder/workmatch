document.addEventListener("DOMContentLoaded", function () {
    const customDropdown = document.querySelector(".nav-item .custom-dropdown");

    if (customDropdown) {
        const navItem = document.querySelector(".nav-item");

        navItem.addEventListener("click", function () {
            if (customDropdown.style.display === "block") {
                customDropdown.style.display = "none";
            } else {
                customDropdown.style.display = "block";
            }
        });

        const dropdownItems = customDropdown.querySelectorAll("li");
        dropdownItems.forEach(function (item) {
            item.addEventListener("click", function () {
                dropdownItems.forEach(function (otherItem) {
                    otherItem.classList.remove("active");
                });

                item.classList.add("active");
            });
        });

        document.addEventListener("click", function (event) {
            if (!navItem.contains(event.target)) {
                customDropdown.style.display = "none";
            }
        });
    }

    let goTopBtn = document.getElementById("go-top");

    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        goTopBtn.style.display = "block";
    } else {
        goTopBtn.style.display = "none";
    }
    }
});

const changeHref = (id) => {
    const path = document.getElementById("id-"+id).value;
    document.getElementById("anchorbtn").href = path;
}

const topFunction = () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}