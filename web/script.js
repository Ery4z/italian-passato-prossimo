// Define the verbs array
const verbs = [
    ['accendere', 'acceso', 'allumer'],
 ['aggiungere', 'aggiunto', 'ajouter'],
 ['aprire', 'aperto', 'ouvrir'],
 ['attendere', 'atteso', 'attendre'],
 ['chiedere', 'chiesto', 'demander'],
 ['chiudere', 'chiuso', 'fermer'],
 ['connettersi', 'connesso', 'se connecter'],
 ['correggere', 'corretto', 'corriger'],
 ['cuocere', 'cotto', 'cuire'],
 ['decidere', 'deciso', 'décider'],
 ['descrivere', 'descritto', 'décrire'],
 ['dire', 'detto', 'dire'],
 ['esprimere', 'espresso', 'exprimer'],
 ['essere', 'stato', 'être'],
 ['fare', 'fatto', 'faire'],
 ['friggere', 'fritto', 'frire'],
 ['leggere', 'letto', 'lire'],
 ['mettere', 'messo', 'mettre'],
 ['morire', 'morto', 'mourir'],
 ['muovere', 'mosso', 'mouvoir'],
 ['nascere', 'nato', 'naître'],
 ['nascondere', 'nascosto', 'cacher'],
 ['offrire', 'offerto', 'offrir'],
 ['perdere', 'perso', 'perdre'],
 ['piangere', 'pianto', 'pleurer'],
 ['prendere', 'preso', 'prendre'],
 ['promettere', 'promesso', 'promettre'],
 ['proporre', 'proposto', 'proposer'],
 ['raccogliere', 'raccolto', 'recueillir'],
 ['ridere', 'riso', 'rire'],
 ['rimanere', 'rimasto', 'rester'],
 ['rispondere', 'risposto', 'répondre'],
 ['rompere', 'rotto', 'casser'],
 ['scegliere', 'scelto', 'choisir'],
 ['scoprire', 'scoperto', 'découvrir'],
 ['scrivere', 'scritto', 'écrire'],
 ['smettere', 'smesso', 'cesser'],
 ['sorridere', 'sorriso', 'sourire'],
 ['spegnere', 'spento', 'éteindre'],
 ['spendere', 'speso', 'dépenser'],
 ['succedere', 'successo', 'arriver'],
 ['togliere', 'tolto', 'enlever'],
 ['tradurre', 'tradotto', 'traduire'],
 ['trascorrere', 'trascorso', 'passer'],
 ['vedere', 'visto', 'voir'],
 ['venire', 'venuto', 'venir'],
 ['vincere', 'vinto', 'gagner'],
 ['vivere', 'vissuto', 'vivre']
    // ... other verbs
];

// Function to find similar words (stub - you need to implement the logic or use a library)
function findSimilarWords(wordsList, targetWord, randomness = 0) {
    // This function should calculate Levenshtein distance
    // and return similar words. You can use a library for the distance calculation.
    // For simplicity, this example returns the list as is.
    return wordsList;
}

// Function to run a single quiz round
function runQuizRound(roundNum, nSimilar) {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = ''; // Clear previous content

    // Randomly choose a verb
    const chosenVerb = verbs[Math.floor(Math.random() * verbs.length)];

    // Randomly decide the form to present
    const presentFormIndex = Math.floor(Math.random() * 3);
    const presentForm = chosenVerb[presentFormIndex];

    // Create question text
    const questionText = document.createElement('p');
    questionText.textContent = `Round ${roundNum}: What are the other forms of '${presentForm}'?`;
    questionText.className = 'question';
    quizContainer.appendChild(questionText);

    // Generate options for the remaining forms
    const options = [];
    for (let i = 0; i < 3; i++) {
        if (i !== presentFormIndex) {
            const similarWords = findSimilarWords(verbs.map(v => v[i]), chosenVerb[i], 1).slice(0, nSimilar);
            options.push({ formType: i, words: similarWords, correct: chosenVerb[i] });
        }
    }

    // Create options in the DOM
    options.forEach((option, index) => {
        const optionContainer = document.createElement('div');

        option.words.forEach(word => {
            const optionButton = document.createElement('button');
            optionButton.textContent = word;
            optionButton.onclick = () => checkAnswer(word, option.correct, optionContainer);
            optionContainer.appendChild(optionButton);
        });

        quizContainer.appendChild(optionContainer);
    });
}

// Function to check the user's answer
function checkAnswer(selectedWord, correctWord, optionContainer) {
    const result = document.createElement('p');
    if (selectedWord === correctWord) {
        result.textContent = 'Correct!';
        result.className = 'correct';
    } else {
        result.textContent = `Incorrect. The correct answer was: ${correctWord}`;
        result.className = 'incorrect';
    }
    optionContainer.appendChild(result);
}

// Function to start the quiz
function startQuiz(rounds, nSimilar) {
    for (let i = 0; i < rounds; i++) {
        runQuizRound(i + 1, nSimilar);
    }
}

// Start the quiz with 30 rounds and 5 similar words
startQuiz(30, 5);
