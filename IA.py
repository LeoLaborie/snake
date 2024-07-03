import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import random



class Serpent:
    def __init__(self, name="NoName"):
        self.name = name
        self.score = 0
        self.model = Sequential()
        self.model.add(keras.Input(shape=(10,)))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(4, activation="softmax"))
        self.model.compile(loss = 'mean_squared_error',  optimizer = 'sgd', metrics = [keras.metrics.categorical_accuracy])
        try: #load previous model
            
            self.model.load_weights(f"models/snake_model_weights{random.randint(0,9)}.h5")
            
            weights = self.model.get_weights()
            for x,arr in enumerate(weights):
                for y, arr2 in enumerate(arr):
                    try:
                        for z, number in enumerate(arr2):
                            weights[x][y, z] =  weights[x][y, z] *random.uniform(0.98, 1.02)
                    
                    except:
                        weights[x][y] =  weights[x][y] *random.uniform(0.98, 1.02)

                
            


            self.model.set_weights(weights)
            

        except Exception as e: #create a new model
            print("ERROR !", e)
            
            
            


    def choose_an_action(self, plateau):
        flattened_data = [0 for _ in range(10)]
        head = plateau.snake.get_file()[-1]
        if head[0] == 0 or plateau.grille[head[0]-1][head[1]] > 0:
            flattened_data[0] = 1
        if head[0] == 9 or plateau.grille[head[0]+1][head[1]] > 0:
            flattened_data[1] = 1
        if head[1] == 0 or plateau.grille[head[0]][head[1]-1] > 0:
            flattened_data[2] = 1
        if head[1] == 9 or plateau.grille[head[0]][head[1]+1] > 0:
            flattened_data[3] = 1
        
    

        pomme = plateau.pomme
        if pomme[1] == head[1]:
            flattened_data[4] = 1
        if pomme[0] == head[0]:
            flattened_data[5] = 1
        if pomme[1] < head[1]:
            flattened_data[6] = 1
        elif pomme[1] > head[1]:
            flattened_data[7] = 1
        if pomme[0] < head[0]:
            flattened_data[8] = 1
        elif pomme[0] > head[0]:
            flattened_data[9] = 1

        flattened_data = np.array([flattened_data])

        prediction = self.model.predict(flattened_data, verbose=0)
        prediction = np.ndarray.tolist(prediction)
        prediction = prediction[0]
        liste_move = ["haut", "bas", "gauche", "droite"]
        


        flattened_data = np.array(np.ndarray.tolist(flattened_data)[0])
        return liste_move[np.argmax(prediction)]
        nbr_rdm = random.uniform(0,0.99)
        sum_to_one = 0
        for i in range(4):
            sum_to_one+=prediction[i]
            if nbr_rdm <= sum_to_one:
                
                
                return liste_move[i], flattened_data, i
        
        

class Generation:
    def __init__(self) -> None:
        self.liste_serpent = [Serpent(str(i)) for i in range(200)]

    def get_average(self):
        somme = 0
        for serpent in self.liste_serpent:
            somme += serpent.score
        return somme/len(self.liste_serpent)

    def save_best_model(self):
        self.liste_serpent.sort(key=lambda x: x.score)
        self.liste_serpent.reverse()
        print("le meilleur serpent a eu un score de:", self.liste_serpent[0].score)

        print("saving models...")
        
        for i,snake_model in enumerate(self.liste_serpent[:10]):
            snake_model.model.save_weights(f"models/snake_model_weights{i}.h5")
        print("saving done !")
