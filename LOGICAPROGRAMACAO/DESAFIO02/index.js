var playerList = [
    [110, 91],
    [14, 4],
    [104, 1],
    [71, 15],
    [50, 21],
    [112, 14],
    [126, 38],
];

function main(playerRank) {
    for (let i = 0; i < playerList.length; i++) {
        const playerWins = playerList[i][0];
        const playerLoses = playerList[i][1];
        const numberPlayer = +i;
        var matches = winsOrLoses(playerWins, playerLoses);
        var playerRank = rank(matches);
        console.log(
            "O jogador " + numberPlayer + " está no rank " + playerRank
        );
    }
}

function winsOrLoses(wins, loses) {
    var matches = wins - loses;
    return matches;
}

function rank(matches) {
    var playerRank;
    if (matches <= 10) {
        playerRank = "Ferro";
    } else if (matches >= 11 && matches <= 20) {
        playerRank = "Bronze";
    } else if (matches >= 21 && matches <= 50) {
        playerRank = "Prata";
    } else if (matches >= 51 && matches <= 80) {
        playerRank = "Ouro";
    } else if (matches >= 81 && matches <= 90) {
        playerRank = "Diamante";
    } else if (matches >= 91 && matches <= 100) {
        playerRank = "Lendário";
    } else if (matches >= 101) {
        playerRank = "Imortal";
    }
    return playerRank;
}

main();
