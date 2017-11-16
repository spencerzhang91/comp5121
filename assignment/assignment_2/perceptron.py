# Naive implementation of a generic perceptron.
import time

class Neuron(object):
    """
    This is a neuron using perceptron algorithm.
    """
    def __init__(self, weightls, learning_rate, threshold):
        self.weightls = weightls
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.converged = False


    def __str__(self):
        return "The trained neuron has properties:\nweights:" + str(self.weightls)


    def train(self, dataset):
        """
        This function trains a perceptron by iteratively modify the weights
        :param dataset: training dataset
        :return: no return
        """
        iteration = 1
        while iteration < 15:  # TODO: ADD AUTO STOP FUNCTIONALITY
            print("ITERATION %d" % iteration)
            print("weightt at this iteration:", self.weightls)
            for row in dataset:
                rsum = self.weightls[0] * 1 # bias, w0 * 1, the interception
                # print("current row -> ", row)
                # print((iteration, rsum))
                for i in range(len(row) - 1):
                    # print("weight * xi: ", " ", self.weightls[i+1], " * ", row[i])
                    rsum += self.weightls[i+1] * row[i]
                t = row[-1] - self.activation_func(rsum) # acutal - predicted
                if t != 0:
                    self.update_weight(row, t)
                    # print("t != 0")

            iteration += 1
            time.sleep(0.5)


    def activation_func(self, tsum):
        """
        The activation function
        :tsum: total sum of the weighted inputs
        :return: True or False.
        """
        # print('\nSUM(weight * xi): ', tsum, '\n')
        return 1 if tsum > self.threshold else 0


    def update_weight(self, curr_row, t):
        """
        This function updates the weight list of neuron
        :curr_row: currently iterating row of data
        :return: set new self.weighls
        """
        new_weightls = []
        new_weightls.append(self.weightls[0] + self.learning_rate * t * 1)
        for i in range(1, len(self.weightls)):
            # print("###### %d + %d * %d * %d" % (self.weightls[i],self.learning_rate,t,curr_row[i-1]))
            new_weightls.append(self.weightls[i] + self.learning_rate * t * curr_row[i-1]) # BUG!
            # print("+++++++", new_weightls)
        self.weightls = new_weightls
        print("updated weights:", self.weightls)




if __name__ == "__main__":

    balance = [[0.08, 0.03, 0],
               [0, 0, 0],
               [0.75, 0.84, 1],
               [1,1,1]]



    neuron = Neuron([0.1, 0.3, 0.2], 0.75, 0.9)
    neuron.train(balance)

    print(neuron)

