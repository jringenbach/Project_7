from random import randint

class Grandpytalk:



    def intro_message(self):
        """Return a random introduction phrase told by grandpy"""

        liste_intro_phrase = [
            "Que veux-tu savoir mon petit?",
            "Ravi de te voir mon enfant. Je peux t'aider?",
            "J'ai tant de souvenirs à partager, dis-moi ce que veux entendre?",
            "Puis-je faire quelque chose pour toi mon petit?",
            "Dans ma folle jeunesse, j'ai visite plein de lieux. Dis-moi le lieu que tu voudrais me voir te raconter!",
            "C'est une belle journée pour te parler du monde, n'est-ce pas? De quoi veux-tu que je te parle?"
        ]

        random_number = randint(0, len(liste_intro_phrase)-1)

        print(liste_intro_phrase[random_number])


    def error_message(self):
        """Return a random error message if what the user has written couldn't be parsed"""

        liste_error_phrase = [
            "Je n'ai pas bien compris ta question mon petit. Peux-tu la répéter?",
            "Désolé, je me fais un peu vieux, je n'ai pas bien entendu ta question.",
            "Pardonne mon vieil âge, mais je n'ai pas compris ce que tu m'as dit.",
            "Je n'ai pas entendu ta question, mon enfant. Peux-tu la répéter?",
            "Quelle est ta question? Je n'ai pas bien saisi, pardonne-moi!"
        ]

        random_number = randint(0, len(liste_error_phrase)-1)

        print(liste_error_phrase[random_number])