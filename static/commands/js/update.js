function openUpdate(elementId) {
    const updateForm = document.getElementById('updateForm' + elementId)
    const line = document.getElementById('line' + elementId)

    if (updateForm.style.display === 'none' & line.style.display === 'none'){
        updateForm.style.display = 'block'
        line.style.display = 'block'
    }else{
        line.style.display = 'none'
        updateForm.style.display = 'none'
    }
}