

function OpenDelete(elementId){
    const deleteButton = document.getElementById('deleteButton' + elementId)
    const deleteForm = document.getElementById('deleteForm' + elementId)
    const updateButton = document.getElementById('updateButton' + elementId)
    

    if (deleteForm.style.display === 'none'){
        deleteForm.style.display = 'inline'
        deleteButton.style.display = 'none'
        updateButton.style.display = 'none'
    }else{
        deleteButton.style.display = 'inline-block'
        updateButton.style.display = 'inline-block'
    }
}

function closeDelete(elementId){
    const closeDelete = document.getElementById('cancel' + elementId)
    const deleteButton = document.getElementById('deleteButton' + elementId)
    const deleteForm = document.getElementById('deleteForm' + elementId)
    const updateButton = document.getElementById('updateButton' + elementId)

    updateButton.style.display = 'inline-block'
    deleteButton.style.display = 'inline-block',
    deleteForm.style.display = 'none'
}