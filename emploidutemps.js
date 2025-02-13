let currentWeek = 1;
const startDate = new Date('2022-09-19');

function changeWeek(direction) {
    currentWeek += direction;
    const newStartDate = new Date(startDate);
    newStartDate.setDate(startDate.getDate() + (currentWeek - 1) * 7);
    updateWeekDisplay(newStartDate);
}

function updateWeekDisplay(date) {
    const options = { day: '2-digit', month: 'short' };
    document.getElementById('week-display').innerText = `Semaine Q${currentWeek}`;
    document.getElementById('date-display').innerText = `du ${date.toLocaleDateString('fr-FR', options)} au ${new Date(date.getTime() + 4 * 24 * 60 * 60 * 1000).toLocaleDateString('fr-FR', options)}`;
    const days = ['lun.', 'mar.', 'mer.', 'jeu.', 'ven.'];
    for (let i = 0; i < 5; i++) {
        document.getElementById(`day-${i}`).innerText = `${days[i]} ${new Date(date.getTime() + i * 24 * 60 * 60 * 1000).toLocaleDateString('fr-FR', options)}`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateWeekDisplay(startDate);
});