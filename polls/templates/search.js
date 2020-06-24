const charactersList = document.getElementById('charactersList');
const searchBar = document.getElementById('searchBar');
let hpCharacters = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredCharacters = hpCharacters.filter((character) => {
        return (
            character.user_id.toLowerCase().includes(searchString) ||
            character.name.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters);
});

const loadCharacters = async () => {
    try {
        const res = await fetch('https://sport-resources-booking-api.herokuapp.com/notreturnedHistory');
        hpCharacters = await res.json();
        displayCharacters(hpCharacters);
    } catch (err) {
        console.error(err);
    }
};

const displayCharacters = (characters) => {
    const htmlString = characters
        .map((character) => {
            return `
            <li class="character">
                <div class="card bg-light">
                <div class="card-body">
        
                <button class="btn btn-circle btn-outline-danger pull-right" aria-hidden="true" style="border-radius: 20px; height: 40px; width: 40px; margin-top: 6px; margin-left: 10px;"><i class="fa fa-bell" aria-hidden="true"></i></button>
                <button class="btn btn-danger pull-right" style="border-radius: 20px; height: 40px; margin-top: 6px;" onclick=acceptResource(${character.user_id})>Not returned</button>
                <div class="h3 d-inline">${character.resource_name}</div>
                <div class="small">${character.name} - ${character.user_id}</div>
                
                </div>
                </div>
            </li>
        `;
        })
        .join('');
    charactersList.innerHTML = htmlString;
};

loadCharacters();