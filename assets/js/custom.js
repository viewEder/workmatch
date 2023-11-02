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
});
