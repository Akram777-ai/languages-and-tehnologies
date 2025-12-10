import { filterByCategory } from './utils.js';

test("Фильтр по категории", () => {
    const sample = [
        { amount: 100, category: "еда" },
        { amount: 200, category: "транспорт" }
    ];

    const res = filterByCategory(sample, "еда");
    expect(res.length).toBe(1);
});