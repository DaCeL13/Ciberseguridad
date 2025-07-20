document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('searchButton').addEventListener('click', buscarPokemon);
});

async function buscarPokemon() {
    const nombre = document.getElementById('pokemonName').value.trim().toLowerCase();
    const resultadoDiv = document.getElementById('pokemonResult');
    const errorMsg = document.getElementById('searchErrorMessage');
    resultadoDiv.innerHTML = '';
    errorMsg.textContent = '';
    errorMsg.style.display = 'none';

    if (!nombre) {
        errorMsg.textContent = 'Por favor, ingresa un nombre de Pokémon.';
        errorMsg.style.display = 'block';
        return;
    }

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${nombre}`);
        if (!response.ok) throw new Error('Pokémon no encontrado');
        const data = await response.json();

        const imagen = data.sprites.front_default;
        const nombrePokemon = data.name;
        const tipo = data.types.map(t => t.type.name).join(', ');
        const altura = data.height / 10 + ' m';
        const peso = data.weight / 10 + ' kg';

        resultadoDiv.innerHTML = `
            <div class="pokemon-card">
                <img src="${imagen}" alt="${nombrePokemon}">
                <h3>${nombrePokemon.charAt(0).toUpperCase() + nombrePokemon.slice(1)}</h3>
                <p><strong>Tipo:</strong> ${tipo}</p>
                <p><strong>Altura:</strong> ${altura}</p>
                <p><strong>Peso:</strong> ${peso}</p>
            </div>
        `;
        resultadoDiv.style.display = 'block';
    } catch (error) {
        errorMsg.textContent = 'Pokémon no encontrado. Intenta con otro nombre.';
        errorMsg.style.display = 'block';
    }
}