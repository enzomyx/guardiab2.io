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