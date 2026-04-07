// Wait until page loads
document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("addBtn").addEventListener("click", addStudent);
    document.getElementById("loadBtn").addEventListener("click", loadStudents);

});

function addStudent() {
    let name = document.getElementById("name").value.trim();
    let company = document.getElementById("company").value.trim();

    if (name === "" || company === "") {
        alert("Please enter both fields!");
        return;
    }

    let li = document.createElement("li");
    li.textContent = name + " - " + company;

    document.getElementById("studentList").appendChild(li);

    document.getElementById("name").value = "";
    document.getElementById("company").value = "";
}

function loadStudents() {
    fetch("data.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Cannot load JSON file");
            }
            return response.json();
        })
        .then(data => {
            let list = document.getElementById("studentList");

            data.forEach(student => {
                let li = document.createElement("li");
                li.textContent = student.name + " - " + student.company;
                list.appendChild(li);
            });
        })
        .catch(error => {
            alert("Error loading data.json\n\n Run using Live Server!");
            console.error(error);
        });
}