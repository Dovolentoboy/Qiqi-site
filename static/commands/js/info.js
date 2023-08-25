function showContent(elementId){
    //const hiddenContent = document.getElementById('hiddenContent' + elementId)
    const hiddenContent = document.getElementById('hiddenContent' + elementId)
    const hideOrShowContent = document.getElementById('openInfo' + elementId)

    if(hiddenContent.style.display === 'none' & hideOrShowContent.textContent === 'Развернуть'){
        hiddenContent.style.display = 'block';
        hideOrShowContent.textContent = 'Свернуть';
    }else{
        hideOrShowContent.textContent = 'Развернуть'
        hiddenContent.style.display = 'none';
    }
}