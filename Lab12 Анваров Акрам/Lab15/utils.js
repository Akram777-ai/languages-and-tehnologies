export function filterByCategory(list, category) {
    return list.filter(item => 
        item.category.toLowerCase().includes(category.toLowerCase())
    );
}