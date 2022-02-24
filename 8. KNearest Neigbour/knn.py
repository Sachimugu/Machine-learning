#k nearest neigbour class
from statistics import mode
class Knn():
    
    #select distance metrics which could either be eclucidean or manhattan
    def __init__(self, distance_metrics='euclidean', k=0):
        
        #initialize parameter
        self.distance_metrics = distance_metrics
        self.k = k
        
    #get distance between two points
    def get_points(self, train_points, X_test):
        
        #euclidean equation
        import numpy as np
        if self.distance_metrics == 'euclidean':
            distance = 0
            for i in range(len(train_points)-1):
                distance = distance + (train_points[i]-X_test[i]) **2
                euclidean = np.sqrt(distance)
            return euclidean
        
        #manhattan equation
        elif self.distance_metrics == 'manhattan':
            distance = 0
            for i in range(len(train_points)-1):
                manhattan = distance + abs(train_points[i]-X_test[i])
                #manhattan = distance
            return manhattan
        
        
    #get the distance for all point and sort in accending order
    def nearestN(self, X_train, X_test):
        
        distance_list = []
        
        for train_points in X_train:
            
            distance = self.get_points(train_points, X_test)
            distance_list.append((train_points, distance))
                
        distance_list.sort(key=lambda x: x[1]) # sort in accending order
        
        neigbour_list = []
                
        # get the top k shotest distance
        for j in range(self.k):
               neigbour_list.append(distance_list[j][0])
                
        return neigbour_list
        
        
    def predict(self, X_train, X_test):
        
        neigbours = self.nearestN(X_train, X_test)

        labels=[]
        for data in neigbours:
            #labels=[]
            labels.append(data[-1])

        predicted = mode(labels)
        
        return predicted
        
    def predictAll(self, X_train, X_test):
        Alabels= []
        #X_train = X_train.to_numpy()
        #X_test = X_test.to_numpy()

        for i in range(len(X_test)):
            Alabel = self.predict(X_train, X_test[i])
            Alabels.append(Alabel)
        
        return Alabels
        
        
            
                
        