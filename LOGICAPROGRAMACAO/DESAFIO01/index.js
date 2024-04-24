const listaPersonagens = [
    ["Jacob", 900],
    ["Evie", 1100],
    ["Arno", 2001],
    ["Shay", 5002],
    ["Connor", 7001],
    ["Edward", 8002],
    ["Ezio", 9500],
    ["Altair", 10100],
];

for (let i = 0; i < listaPersonagens.length; i++) {
    const personagem = listaPersonagens[i][0];
    const xp = listaPersonagens[i][1];
    let level;

    if (xp <= 1000) {
        level = "Ferro";
    } else if (xp <= 2000) {
        level = "Bronze";
    } else if (xp <= 5000) {
        level = "Prata";
    } else if (xp <= 7000) {
        level = "Ouro";
    } else if (xp <= 8000) {
        level = "Platina";
    } else if (xp <= 9000) {
        level = "Ascendente";
    } else if (xp <= 10000) {
        level = "Imortal";
    } else {
        level = "Radiante";
    }

    console.log(personagem + " está no level " + level);
}
