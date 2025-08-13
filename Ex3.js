function helloNalios() {
    // Je vais me baser sur la doc ASCII ( trouvé sur Google. )
    const codes = [
        72, 101, 108, 108, 111, 44, 32, // "Hello, "
        78, 97, 108, 105, 111, 115, 32, // "Nalios "
        33 // "!"
    ];

    const message = codes.map(c => String.fromCharCode(c)).join(''); // N'étant pas familier avec la doc Javascript, je suis partit voir sur Google pour un bout cette fonction. Cependant, l'idée ne provient que de moi et aucune IA n'a été utilisé.
    console.log(message);
}

helloNalios();