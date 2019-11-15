from random import randint

class Grandpytalk:



    def intro_message(self):
        """Return a random introduction phrase told by grandpy"""

        liste_intro_phrase = [
            "Que veux-tu savoir mon petit?",
            "Ravi de te voir mon enfant. Je peux t'aider?",
            "J'ai tant de souvenirs à partager, dis-moi ce que veux entendre?",
            "Puis-je faire quelque chose pour toi mon petit?",
            "Dans ma folle jeunesse, j'ai visite plein de lieux. Dis-moi le lieu que tu voudrais me voir te raconter!"
        ]

        random_number = randint(0, len(liste_intro_phrase))

        return liste_intro_phrase[random_number]