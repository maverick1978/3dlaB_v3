function openLoginPopup() {
    document.getElementById('loginPopup').style.display = 'block';
}

function closeLoginPopup() {
    document.getElementById('loginPopup').style.display = 'none';
}

// Cerrar el popup cuando el usuario hace clic fuera del mismo
window.onclick = function(event) {
    var popup = document.getElementById('loginPopup');
    if (event.target == popup) {
        popup.style.display = 'none';
    }
}
