import { saveData, loadData } from './storage.js';
import { render } from './ui.js';
import { filterByCategory } from './utils.js';

let data = loadData();

const amount = document.getElementById('amount');
const category = document.getElementById('category');
const listElem = document.getElementById('list');
const search = document.getElementById('search');

function update() {
    saveData(data);
    render(listElem, data, removeItem);
}

function removeItem(index) {
    data.splice(index, 1);
    update();
}

document.getElementById('addBtn').onclick = () => {
    const a = Number(amount.value);
    const c = category.value.trim();

    if (!a || !c) return;

    data.push({ amount: a, category: c });
    amount.value = '';
    category.value = '';
    update();
};

document.getElementById('searchBtn').onclick = () => {
    const text = search.value.trim();
    const filtered = filterByCategory(data, text);
    render(listElem, filtered, removeItem);
};

update();