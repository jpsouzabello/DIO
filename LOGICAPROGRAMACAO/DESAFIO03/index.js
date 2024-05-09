class hero {
    constructor(name, age, type) {
        this.name = name;
        this.age = age;
        this.type = type;
    }
    story() {
        var atack;
        if (this.type === "Guerreiro") {
            atack = "espada";
            console.log(
                `O ${this.type} ${this.name} de ${this.age} anos atacou usando ${atack}.`
            );
        } else if (this.type === "Mago") {
            atack = "mágica";
            console.log(
                `O ${this.type} ${this.name} de ${this.age} anos atacou usando ${atack}.`
            );
        } else if (this.type === "Ninja") {
            atack = "shuriken";
            console.log(
                `O ${this.type} ${this.name} de ${this.age} anos atacou usando ${atack}.`
            );
        } else if (this.type === "Monge") {
            atack = "artes maciais";
            console.log(
                `O ${this.type} ${this.name} de ${this.age} anos atacou usando ${atack}.`
            );
        } else {
            console.log("Resposta inválida.");
        }
    }
}

var ninja = new hero("John", "22", "Ninja");
var mago = new hero("Gustavo", "25", "Mago");
var monge = new hero("Mathias", "19", "Monge");
var guerreiro = new hero("Nascimento", "37", "Guerreiro");

var heroList = [ninja, mago, monge, guerreiro];

for (i in heroList) {
    heroList[i].story();
}
