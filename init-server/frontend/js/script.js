// La función se define para ser llamada directamente por onclick
// function register(event) {
//     event.preventDefault(); // Previene el envío por defecto del formulario
//     const username = document.getElementById('username').value;
//     const password = document.getElementById('password').value;
//     // Si tienes un elemento para mostrar errores, descomenta la siguiente línea y añade el elemento en el HTML
//     // const errorMessage = document.getElementById('errorMessage');

//     const validUsers = {
//         "admin": "admin",
//         "danielc": "1234"
//     };

//     if (validUsers[username] && validUsers[username] === password) {
//         alert('Login exitoso. Bienvenido ' + username + '!');
//         // if (errorMessage) errorMessage.textContent = '';
//         window.location.href = 'pokemon.html';
//     } else {
//         alert('Usuario o contraseña incorrectos.');
//         // if (errorMessage) errorMessage.textContent = 'Usuario o contraseña incorrectos.';
//     }
// }

// function onSubmit(token) {
//     document.getElementById("loginForm").submit();
// }

// document.getElementById('loginForm').addEventListener('submit', register);

// Ejemplo simple en tu script.js
// document.getElementById('loginForm').addEventListener('submit', function(event) {
//     if (grecaptcha.getResponse() === "") {
//         event.preventDefault();
//         alert("Por favor, verifica el captcha.");
//     }
// });

// function onSubmit(e) {
//     e.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

//     // Aquí puedes agregar la lógica para manejar el envío del formulario
//     const form = document.getElementById('loginForm');
//     const formData = new FormData(form);

//     fetch(form.action, {
//         method: 'POST',
//         body: formData,
//         headers: {
//             'Accept': 'application/json'
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Éxito:', data);
//         // Aquí puedes manejar la respuesta del servidor
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }   
document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Previene el envío por defecto del formulario
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Aquí puedes agregar la lógica para manejar el envío del formulario
    fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    })
    .then(response => {
        console.log('Respuesta del servidor:', response);
        return response.json()
    })
    .then(data => {
        console.log('Éxito:', data);
        alert(data.message); // Muestra el mensaje de éxito
        // Aquí puedes redirigir o realizar otras acciones según la respuesta del servidor
        if (data.success) {
            window.location.href = 'pokemon.html';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error al iniciar sesión.'); // Muestra un mensaje de error
    });
});