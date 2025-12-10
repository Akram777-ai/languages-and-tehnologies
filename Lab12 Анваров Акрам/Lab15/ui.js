export function render(listElem, data, removeFn) {
    listElem.innerHTML = '';

    data.forEach((item, index) => {
        const li = document.createElement('li');
        li.textContent = `${item.amount}₸ — ${item.category}`;

        const btn = document.createElement('button');
        btn.textContent = "Удалить";
        btn.onclick = () => removeFn(index);

        li.appendChild(btn);
        listElem.appendChild(li);
    });
}