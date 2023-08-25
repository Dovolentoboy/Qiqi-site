const selectCategory = document.getElementById('select-category')

selectCategory.addEventListener('change', (event) => {
    const categoryId = event.target.value

    if (categoryId != '' & categoryId != 'Покажи мне всё'){
        window.location.href = 'http://127.0.0.1:8000/commands/commands/category/' + categoryId
        console.log('Увидел это условие (пустая строка)')
    }else if (categoryId === 'Покажи мне всё'){
        window.location.href = 'http://127.0.0.1:8000/commands/commands/'
        console.log('Увидел это условие (все категории)')
    }
    
})