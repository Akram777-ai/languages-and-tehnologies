export function saveData(list) {
    localStorage.setItem('expenses', JSON.stringify(list));
}

export function loadData() {
    return JSON.parse(localStorage.getItem('expenses')) || [];
}