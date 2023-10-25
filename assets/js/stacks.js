document.addEventListener("DOMContentLoaded", function () {
    const btnGroup = document.querySelector(".btn-group-toggle");

    const createBtn = element => {
        let label = document.createElement("label");
        label.classList.add("btn");
        label.setAttribute("data-bs-toggle", "tooltip");
        label.setAttribute("data-bs-placement", "bottom");
        label.setAttribute("data-bs-html", "true");
        label.title = "<ul>"
        element.tools.forEach(tool => {
            label.title += "<li>" + tool + "</li>";
        });
        label.title += "</ul>"
        let input = document.createElement("input");
        input.type = "checkbox";
        input.name = "stack";
        input.value = element.stack;
        input.classList.add("visually-hidden");
        input.setAttribute("autocomplete", "off");
        if (stacks.includes(element.stack)) {
            label.classList.add("btn-primary");
            input.checked = true;
        }
        let inputText = document.createTextNode(element.stack);
        label.appendChild(input);
        label.appendChild(inputText);
        return label;
    }

    const eventsBtn = () => {
        const labels = document.querySelectorAll('label.btn');
        labels.forEach(label => {
            label.addEventListener('click', function (e) {
                e.stopPropagation();
                const input = this.querySelector('input');
                input.checked = !input.checked;

                if (input.checked) {
                    this.classList.add('btn-primary');
                } else {
                    this.classList.remove('btn-primary');
                }
            });
        });
    }

    const tooltips = () => {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl, { trigger: 'hover' })
        })
    }

    fetch('/assets/js/stacks.json')
        .then(response => response.json())
        .then(data => {
            data.forEach(element => {
                btnGroup.appendChild(createBtn(element));
            });
            eventsBtn();
            tooltips();
        })
        .catch(error => {
            console.error("Error loading JSON file: " + error);
        });
});