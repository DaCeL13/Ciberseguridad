// La función se define para ser llamada directamente por onclick
function register(event) {
    event.preventDefault(); // Previene el envío por defecto del formulario
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Si tienes un elemento para mostrar errores, descomenta la siguiente línea y añade el elemento en el HTML
    // const errorMessage = document.getElementById('errorMessage');

    const validUsers = {
        "admin": "admin",
        "danielc": "1234"
    };

    if (validUsers[username] && validUsers[username] === password) {
        alert('Login exitoso. Bienvenido ' + username + '!');
        // if (errorMessage) errorMessage.textContent = '';
        window.location.href = 'pokemon.html';
    } else {
        alert('Usuario o contraseña incorrectos.');
        // if (errorMessage) errorMessage.textContent = 'Usuario o contraseña incorrectos.';
    }
}

document.getElementById('loginForm').addEventListener('submit', register);