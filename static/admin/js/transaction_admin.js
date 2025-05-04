document.addEventListener('DOMContentLoaded', function () {
    const typeField = document.getElementById('id_type');
    const categoryField = document.getElementById('id_category');
    const subcategoryField = document.getElementById('id_subcategory');

    // Функция для обновления списка категорий
    function updateCategories() {
        const typeId = typeField.value;
        const typeName = typeField.options[typeField.selectedIndex]?.text || '';

        // Сохраняем текущее значение категории
        const selectedCategoryId = categoryField.value;

        fetch(`/admin/manager/transaction/filter-categories/?type_id=${typeId}`)
            .then(response => response.json())
            .then(data => {
                categoryField.innerHTML = '';
                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = `${category.name} - ${typeName}`;
                    categoryField.appendChild(option);
                });

                // Восстанавливаем выбранное значение категории, если оно существует в новом списке
                if (data.some(cat => cat.id == selectedCategoryId)) {
                    categoryField.value = selectedCategoryId;
                }

                updateSubcategories();
            });
    }

    // Функция для обновления списка подкатегорий
    function updateSubcategories() {
        const categoryId = categoryField.value;
        const categoryName = categoryField.options[categoryField.selectedIndex]?.text || '';

        // Сохраняем текущее значение подкатегории
        const selectedSubcategoryId = subcategoryField.value;

        if (categoryId) {
            fetch(`/admin/manager/transaction/filter-subcategories/?category_id=${categoryId}`)
                .then(response => response.json())
                .then(data => {
                    subcategoryField.innerHTML = '';
                    data.forEach(subcategory => {
                        const option = document.createElement('option');
                        option.value = subcategory.id;
                        option.textContent = `${subcategory.name} - ${categoryName.split(' - ')[0]}`;
                        subcategoryField.appendChild(option);
                    });

                    // Восстанавливаем выбранное значение подкатегории, если оно существует в новом списке
                    if (data.some(subcat => subcat.id == selectedSubcategoryId)) {
                        subcategoryField.value = selectedSubcategoryId;
                    }
                });
        } else {
            subcategoryField.innerHTML = '';
        }
    }

    // Назначаем обработчики событий
    if (typeField && categoryField) {
        typeField.addEventListener('change', updateCategories);
    }

    if (categoryField && subcategoryField) {
        categoryField.addEventListener('change', updateSubcategories);
    }

    try {
        // Вызываем функции при загрузке страницы, чтобы показать правильные данные по умолчанию
        updateCategories();
        updateSubcategories();
    } catch (error) {
        console.log('Ошибка при загрузке данных:', error);
    }
});