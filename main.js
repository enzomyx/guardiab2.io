let currentWeek = 1; // Numéro de la semaine actuelle
const startDate = new Date('2022-09-19'); // Date de départ de référence

// Fonction pour changer de semaine
function changeWeek(direction) {
    currentWeek += direction;
    const newStartDate = new Date(startDate);
    newStartDate.setDate(startDate.getDate() + (currentWeek - 1) * 7);
    updateWeekDisplay(newStartDate);
}

// Fonction pour mettre à jour l'affichage de la semaine
function updateWeekDisplay(date) {
    const options = { day: '2-digit', month: 'short' };
    document.getElementById('week-display').innerText = `Semaine ${currentWeek}`;
    document.getElementById('date-display').innerText = `du ${date.toLocaleDateString('fr-FR', options)} au ${new Date(date.getTime() + 6 * 24 * 60 * 60 * 1000).toLocaleDateString('fr-FR', options)}`;
}

// Fonction pour appliquer le mode sombre depuis le localStorage
function applyDarkModeFromLocalStorage() {
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}



// Fonction pour basculer le mode sombre
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');

    // Enregistrer l'état actuel dans le localStorage
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
}

// Initialisation du mode sombre au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    // Appliquez le mode sombre si nécessaire
    applyDarkModeFromLocalStorage();

    // Ajoutez l'écouteur pour le bouton de mode sombre
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', (e) => {
            e.preventDefault();
            toggleDarkMode();
        });
    }
});

function deleteStudent(studentId) {
    fetch(`/delete_student/${studentId}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();  // Recharge la page après suppression
        }
    });
}

document.querySelectorAll(".status").forEach((statusCell) => {
    statusCell.addEventListener("click", function () {
        let newStatus = prompt("Entrez le nouveau statut (Présent, Absent, En retard) :");
        if (newStatus) {
            let studentId = this.getAttribute("data-id");
            fetch("/update_status", {
                method: "POST",
                body: new URLSearchParams({ id: studentId, status: newStatus }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            }).then(response => response.json()).then(data => {
                if (data.success) location.reload();
            });
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Supprimer un élève
    document.querySelectorAll(".remove-btn").forEach(button => {
        button.addEventListener("click", function () {
            let studentId = this.getAttribute("data-id");
            if (confirm("Voulez-vous vraiment supprimer cet élève ?")) {
                fetch("/delete_student", {
                    method: "POST",
                    body: new URLSearchParams({ id: studentId }),
                    headers: { "Content-Type": "application/x-www-form-urlencoded" }
                }).then(response => response.json()).then(data => {
                    if (data.success) location.reload();
                });
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("addStudentForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Empêche le rechargement de la page

        let studentName = document.getElementById("newStudentName").value.trim();
        let studentEmail = document.getElementById("newStudentEmail").value.trim();

        if (studentName === "" || studentEmail === "") {
            alert("Veuillez remplir tous les champs !");
            return;
        }

        fetch("/add_student", {
            method: "POST",
            body: new URLSearchParams({ name: studentName, email: studentEmail }),
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Élève ajouté avec succès !");
                location.reload(); // Recharge la page pour voir l'élève ajouté
            } else {
                alert("Erreur : " + data.message);
            }
        })
        .catch(error => console.error("Erreur:", error));
    });
});
