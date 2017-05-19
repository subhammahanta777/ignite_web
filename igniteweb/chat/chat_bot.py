# -*- coding: UTF-8 -*-
import numpy
import json
import os.path
import sys
from sklearn.feature_extraction.text import CountVectorizer # countvectoriser creats tokens for each data set
import numpy.linalg as LA #importing the linear algebra module
# from nltk.corpus import stopwords

dict_11_15 = {
    '1':{
        'what is binomial distribution?':'A binomial random variable is the number of successes x in n repeated trials of a binomial experiment. The probability distribution of a binomial random variable is called a binomial distribution. Suppose we flip a coin two times and count the number of heads (successes).',
        'what is a random sample?':'In statistics, a simple random sample is a subset of individuals (a sample) chosen from a larger set (a population). ... The principle of simple random sampling is that every object has the same probability of being chosen.',
        'formula for mean':'The symbol \'σ\' represents the population standard deviation. The term \'sqrt\' used in this statistical formula denotes square root. The term \'Σ ( Xi - μ )2\' used in the statistical formula represents the sum of the squares of the deviation of the variables from their population mean.'
    },
    '2':{
        'What is probability distribution table?': 'Probability Distribution table is used to represent the probability of set of data in a tabular form in which probability of every outcome is written in a much simplified way.',
        'What does expected value of a variable signifies?': 'Expected value of any random variable can be defined as the long-run average value of repetitions of the experiment it represents',
        'What do we mean by equally likely?': 'If all the variables in a particular set of data are having equal possibility of occurrence, then the variables are set to be equally likely.',
        'How to find the value of k for equal roots?': 'Let f(x)  = ax2 + bx + c, then if D = 0, the function f(x) will have equal roots.Here D = (b2 – 4ac)',
        'How to find the value of k for no roots?': 'Let f(x)  = ax2 + bx + c, then if D < 0, the function f(x) will have no roots (no real roots).Here D = (b2 – 4ac)',
        'What do we mean by random variable': 'If a set of data is having all the items with equal probability of occurrence, then choosing any of the item from the set of data will give same outcome (ultimate result). In that case, any value can be selected as a random variable',
        'How do  you find conditional probability?':'Start with Multiplication Rule 2. Divide both sides of equation by P(A). Cancel P(A)s on right-hand side of equation. We have derived the formula for conditional probability.',
        'what do you mean by dependent probability?':'Two events aredependent if the outcome or occurrence of the first affects the outcome or occurrence of the second so that the probability is changed.',
        'what is P(A|B)?':'If the event of interest is A and the event B is known or assumed to have occurred, "the conditional probability of A given B", or "the probability of A under the conditionB", is usually written as P(A. | B), or sometimes PB(A).',
        'what is a random variable?':'A random variable, usually written X, is a variable whose possible values are numerical outcomes of a randomphenomenon. There are two types of random variables, discrete and continuous',
        'what is a probability distribution?':'a function of a discrete variable whose integral over any interval is the probability that the variate specified by it will lie within that interval.'

    },
    '3':{
        'What is probability distribution table?': 'Probability Distribution table is used to represent the probability of set of data in a tabular form in which probability of every outcome is written in a much simplified way.',
        'What does expected value of a variable signifies?': 'Expected value of any random variable can be defined as the long-run average value of repetitions of the experiment it represents',
        'What do we mean by equally likely?': 'If all the variables in a particular set of data are having equal possibility of occurrence, then the variables are set to be equally likely.',
        'How to find the value of k for equal roots?': 'Let f(x)  = ax2 + bx + c, then if D = 0, the function f(x) will have equal roots.Here D = (b2 – 4ac)',
        'How to find the value of k for no roots?': 'Let f(x)  = ax2 + bx + c, then if D < 0, the function f(x) will have no roots (no real roots).Here D = (b2 – 4ac)',
        'What do we mean by random variable': 'If a set of data is having all the items with equal probability of occurrence, then choosing any of the item from the set of data will give same outcome (ultimate result). In that case, any value can be selected as a random variable',
        'How do  you find conditional probability?':'Start with Multiplication Rule 2. Divide both sides of equation by P(A). Cancel P(A)s on right-hand side of equation. We have derived the formula for conditional probability.',
        'what do you mean by dependent probability?':'Two events aredependent if the outcome or occurrence of the first affects the outcome or occurrence of the second so that the probability is changed.',
        'what is P(A|B)?':'If the event of interest is A and the event B is known or assumed to have occurred, "the conditional probability of A given B", or "the probability of A under the conditionB", is usually written as P(A. | B), or sometimes PB(A).',
        'what is a random variable?':'A random variable, usually written X, is a variable whose possible values are numerical outcomes of a randomphenomenon. There are two types of random variables, discrete and continuous',
        'what is a probability distribution?':'a function of a discrete variable whose integral over any interval is the probability that the variate specified by it will lie within that interval.'

    },
    '4':{
        'What is a hypothesis?': 'It can be termed as a supposition or proposed explanation made on the basis of limited evidence as a starting point for further investigation.',
        'What is choosing a random variable without replacement?': 'Choosing a random variable without replacement means the size of sample space will remain the same even if some of the variable have already participated in the experiment',
        'How to denote the expected value?': 'The expected value of X can be denoted as E (X)',
        'What is a Poisson distribution?': 'It can be termed as a discrete frequency distribution which gives the probability of a number of independent events occurring in a fixed time.',
        'What is least possible value for a variable?': 'Least possible value for a variable means the minimum value that a variable can attain within all the possible outcomes in the sample space.',
        'what is a sample?':'A visual representation of selecting a simple randomsample. In statistics and quantitative research methodology, a data sample is a set of data collected and/or selected from a statistical population by a defined procedure. The elements of a sample are known as sample points, sampling units or observations.',
        'what is the chi square test ?':'a statistical method assessing the goodness of fit between a set of observed values and those expected theoretically.',
        'what is a null hypothesis?':'the hypothesis that there is no significant difference between specified populations, any observed difference being due to sampling or experimental error.',
        'what do you mean by degrees of freedom?':'In statistics, the number of degrees of freedom is the number of values in the final calculation of a statistic that are free to vary. The number of independent ways by which a dynamic system can move, without violating any constraint imposed on it, is called number of degrees of freedom',
        'when do you accept a hypothesis?':'Let\'s return finally to the question of whether we reject or fail to reject the nullhypothesis. If our statistical analysis shows that the significance level is below the cut-off value we have set (e.g., either 0.05 or 0.01), we reject the null hypothesisand accept the alternative hypothesis.',
        'what is  χ2?':'A chi-squared test, also written as χ2 test, is any statistical hypothesis test wherein the sampling distribution of the test statistic is a chi-squared distribution when the null hypothesis is true. Without other qualification, \'chi-squared test\' often is used as short for Pearson\'s chi-squared test.'

    },
    '5':{
        'What are tree Diagrams?': 'Tree diagram allow us to see all the possible outcomes of an event and calculate their probability. Each branch in a tree diagram represents a possible outcome. If two events are independent, the outcome of one has no effect on the outcome of the other',
        'what do the numbers on the branches signify?': 'they signify the probability'
    },
    '6':{
        'What are tree Diagrams?': 'Tree diagram allow us to see all the possible outcomes of an event and calculate their probability. Each branch in a tree diagram represents a possible outcome. If two events are independent, the outcome of one has no effect on the outcome of the other',
        'what do the numbers on the branches signify?': 'they signify the probability'
    },
    '7':{
        'what is a venn diagram?':'a diagram representing mathematical or logical sets pictorially as circles or closed curves within an enclosing rectangle (the universal set), common elements of the sets being represented by intersections of the circles',
        'what do you mean by an element?' :'Element is the content of a set',
        'what does it mean by a region?':'The area enclosed by the circle is know as the region',
        'what is a set?':'sets are the region enclosed by the closed curves',
        'what is the diffrence between A and A\'?':'A represents set A and A\' is its complement.',
        'what does U stand for?':'it stands for Union',
        'What does ∩ stand for?':'it stands for intersection',
        'what is the diffrence between neither-nor and either-or?':'Either is always paired with or, and neither is always paired with nor. If you are matching either and nor, I hate to break it to you, but you\'re doing it wrong. Additionally, nor is generally not used where neither is not also used.',
        'can you explain what A ∩ Y’ means In english?':'A intersection Y-compliment',
        'what do you mean by a universal set?':'the set containing all objects or elements and of which all other sets are subsets',
        'how do you represent AND in venn diagram?':'we represent it with an intersection',
        'do we multiply the probabilities when and is specified?':'yes',
        'when should we multiply and whan should we add probabilities?':'multiply when the probabilities used with AND. Add when the probablities are mentioned woth OR.'
    },
    '8':{
        'what is binomial distribution?':'A binomial random variable is the number of successes x in n repeated trials of a binomial experiment. The probability distribution of a binomial random variable is called a binomial distribution. Suppose we flip a coin two times and count the number of heads (successes).',
        'what is a random sample?':'In statistics, a simple random sample is a subset of individuals (a sample) chosen from a larger set (a population). ... The principle of simple random sampling is that every object has the same probability of being chosen.',
        'formula for mean':'The symbol \'σ\' represents the population standard deviation. The term \'sqrt\' used in this statistical formula denotes square root. The term \'Σ ( Xi - μ )2\' used in the statistical formula represents the sum of the squares of the deviation of the variables from their population mean.'
    },
    '9':{
        'What is probability distribution table?': 'Probability Distribution table is used to represent the probability of set of data in a tabular form in which probability of every outcome is written in a much simplified way.',
        'What does expected value of a variable signifies?': 'Expected value of any random variable can be defined as the long-run average value of repetitions of the experiment it represents',
        'What do we mean by equally likely?': 'If all the variables in a particular set of data are having equal possibility of occurrence, then the variables are set to be equally likely.',
        'How to find the value of k for equal roots?': 'Let f(x)  = ax2 + bx + c, then if D = 0, the function f(x) will have equal roots.Here D = (b2 – 4ac)',
        'How to find the value of k for no roots?': 'Let f(x)  = ax2 + bx + c, then if D < 0, the function f(x) will have no roots (no real roots).Here D = (b2 – 4ac)',
        'What do we mean by random variable': 'If a set of data is having all the items with equal probability of occurrence, then choosing any of the item from the set of data will give same outcome (ultimate result). In that case, any value can be selected as a random variable',
        'How do  you find conditional probability?':'Start with Multiplication Rule 2. Divide both sides of equation by P(A). Cancel P(A)s on right-hand side of equation. We have derived the formula for conditional probability.',
        'what do you mean by dependent probability?':'Two events aredependent if the outcome or occurrence of the first affects the outcome or occurrence of the second so that the probability is changed.',
        'what is P(A|B)?':'If the event of interest is A and the event B is known or assumed to have occurred, "the conditional probability of A given B", or "the probability of A under the conditionB", is usually written as P(A. | B), or sometimes PB(A).',
        'what is a random variable?':'A random variable, usually written X, is a variable whose possible values are numerical outcomes of a randomphenomenon. There are two types of random variables, discrete and continuous',
        'what is a probability distribution?':'a function of a discrete variable whose integral over any interval is the probability that the variate specified by it will lie within that interval.'

    },
    '10':{
        'What is probability distribution table?': 'Probability Distribution table is used to represent the probability of set of data in a tabular form in which probability of every outcome is written in a much simplified way.',
        'What does expected value of a variable signifies?': 'Expected value of any random variable can be defined as the long-run average value of repetitions of the experiment it represents',
        'What do we mean by equally likely?': 'If all the variables in a particular set of data are having equal possibility of occurrence, then the variables are set to be equally likely.',
        'How to find the value of k for equal roots?': 'Let f(x)  = ax2 + bx + c, then if D = 0, the function f(x) will have equal roots.Here D = (b2 – 4ac)',
        'How to find the value of k for no roots?': 'Let f(x)  = ax2 + bx + c, then if D < 0, the function f(x) will have no roots (no real roots).Here D = (b2 – 4ac)',
        'What do we mean by random variable': 'If a set of data is having all the items with equal probability of occurrence, then choosing any of the item from the set of data will give same outcome (ultimate result). In that case, any value can be selected as a random variable',
        'How do  you find conditional probability?':'Start with Multiplication Rule 2. Divide both sides of equation by P(A). Cancel P(A)s on right-hand side of equation. We have derived the formula for conditional probability.',
        'what do you mean by dependent probability?':'Two events aredependent if the outcome or occurrence of the first affects the outcome or occurrence of the second so that the probability is changed.',
        'what is P(A|B)?':'If the event of interest is A and the event B is known or assumed to have occurred, "the conditional probability of A given B", or "the probability of A under the conditionB", is usually written as P(A. | B), or sometimes PB(A).',
        'what is a random variable?':'A random variable, usually written X, is a variable whose possible values are numerical outcomes of a randomphenomenon. There are two types of random variables, discrete and continuous',
        'what is a probability distribution?':'a function of a discrete variable whose integral over any interval is the probability that the variate specified by it will lie within that interval.'

    },
    '11':{
        'What is a hypothesis?': 'It can be termed as a supposition or proposed explanation made on the basis of limited evidence as a starting point for further investigation.',
        'What is choosing a random variable without replacement?': 'Choosing a random variable without replacement means the size of sample space will remain the same even if some of the variable have already participated in the experiment',
        'How to denote the expected value?': 'The expected value of X can be denoted as E (X)',
        'What is a Poisson distribution?': 'It can be termed as a discrete frequency distribution which gives the probability of a number of independent events occurring in a fixed time.',
        'What is least possible value for a variable?': 'Least possible value for a variable means the minimum value that a variable can attain within all the possible outcomes in the sample space.',
        'what is a sample?':'A visual representation of selecting a simple randomsample. In statistics and quantitative research methodology, a data sample is a set of data collected and/or selected from a statistical population by a defined procedure. The elements of a sample are known as sample points, sampling units or observations.',
        'what is the chi square test ?':'a statistical method assessing the goodness of fit between a set of observed values and those expected theoretically.',
        'what is a null hypothesis?':'the hypothesis that there is no significant difference between specified populations, any observed difference being due to sampling or experimental error.',
        'what do you mean by degrees of freedom?':'In statistics, the number of degrees of freedom is the number of values in the final calculation of a statistic that are free to vary. The number of independent ways by which a dynamic system can move, without violating any constraint imposed on it, is called number of degrees of freedom',
        'when do you accept a hypothesis?':'Let\'s return finally to the question of whether we reject or fail to reject the nullhypothesis. If our statistical analysis shows that the significance level is below the cut-off value we have set (e.g., either 0.05 or 0.01), we reject the null hypothesisand accept the alternative hypothesis.',
        'what is  χ2?':'A chi-squared test, also written as χ2 test, is any statistical hypothesis test wherein the sampling distribution of the test statistic is a chi-squared distribution when the null hypothesis is true. Without other qualification, \'chi-squared test\' often is used as short for Pearson\'s chi-squared test.'

    },
    '12':{
        'What are tree Diagrams?': 'Tree diagram allow us to see all the possible outcomes of an event and calculate their probability. Each branch in a tree diagram represents a possible outcome. If two events are independent, the outcome of one has no effect on the outcome of the other',
        'what do the numbers on the branches signify?': 'they signify the probability'
    },
    '13':{
        'What are tree Diagrams?': 'Tree diagram allow us to see all the possible outcomes of an event and calculate their probability. Each branch in a tree diagram represents a possible outcome. If two events are independent, the outcome of one has no effect on the outcome of the other',
        'what do the numbers on the branches signify?': 'they signify the probability'
    },
    '14':{
        'what is a venn diagram?':'a diagram representing mathematical or logical sets pictorially as circles or closed curves within an enclosing rectangle (the universal set), common elements of the sets being represented by intersections of the circles',
        'what do you mean by an element?' :'Element is the content of a set',
        'what does it mean by a region?':'The area enclosed by the circle is know as the region',
        'what is a set?':'sets are the region enclosed by the closed curves',
        'what is the diffrence between A and A\'?':'A represents set A and A\' is its complement.',
        'what does U stand for?':'it stands for Union',
        'What does ∩ stand for?':'it stands for intersection',
        'what is the diffrence between neither-nor and either-or?':'Either is always paired with or, and neither is always paired with nor. If you are matching either and nor, I hate to break it to you, but you\'re doing it wrong. Additionally, nor is generally not used where neither is not also used.',
        'can you explain what A ∩ Y’ means In english?':'A intersection Y-compliment',
        'what do you mean by a universal set?':'the set containing all objects or elements and of which all other sets are subsets',
        'how do you represent AND in venn diagram?':'we represent it with an intersection',
        'do we multiply the probabilities when and is specified?':'yes',
        'when should we multiply and whan should we add probabilities?':'multiply when the probabilities used with AND. Add when the probablities are mentioned woth OR.'
    },
    '15':{
        'what is a venn diagram?':'a diagram representing mathematical or logical sets pictorially as circles or closed curves within an enclosing rectangle (the universal set), common elements of the sets being represented by intersections of the circles',
        'what do you mean by an element?' :'Element is the content of a set',
        'what does it mean by a region?':'The area enclosed by the circle is know as the region',
        'what is a set?':'sets are the region enclosed by the closed curves',
        'what is the diffrence between A and A\'?':'A represents set A and A\' is its complement.',
        'what does U stand for?':'it stands for Union',
        'What does ∩ stand for?':'it stands for intersection',
        'what is the diffrence between neither-nor and either-or?':'Either is always paired with or, and neither is always paired with nor. If you are matching either and nor, I hate to break it to you, but you\'re doing it wrong. Additionally, nor is generally not used where neither is not also used.',
        'can you explain what A ∩ Y’ means In english?':'A intersection Y-compliment',
        'what do you mean by a universal set?':'the set containing all objects or elements and of which all other sets are subsets',
        'how do you represent AND in venn diagram?':'we represent it with an intersection',
        'do we multiply the probabilities when and is specified?':'yes',
        'when should we multiply and whan should we add probabilities?':'multiply when the probabilities used with AND. Add when the probablities are mentioned woth OR.'
    }
}


def model(train_dataset,new_data):
    # new = [str(input())]
    # print(type(new))
    new = [new_data]
    ques_list = list(train_dataset.keys())
    # print(type(ques_list))
    vectorizer, trainVectorizerArray = train_func(ques_list)
    new_test = vectorizer.transform(new).toarray()  # creating a token for the new input data
    # to see what the new token looks like
    # COSINE SIMILARITY algorithm
    # print(new)
    cx = lambda a, b: round(numpy.inner(a, b) / (LA.norm(a) * LA.norm(b)), 3)

    for testV in new_test:  # selecting the new token that was created for the input question
        cos = 0.0
        ans = ''
        for n, vector in enumerate(trainVectorizerArray):  # selecting the first token
            cosine = cx(vector, testV)  # finding the cosine similarity between the selected token and the new token
            ###########FINDING THE HIGHEST SMILARITY###########3
            if cosine > cos:
                cos = cosine
                # print(type(train_dataset))
                a = ques_list[n]
                ans = train_dataset[a]
        if ans == '':
            return ('Sorry! I couldn\'t understand that. Be more specific')
        else:
            return(ans)
            # print("------------------------------")

def train_func(train):
    # stopWords = stopwords.words('english')
    stopWords = ['the', 'is', 'are', 'were', 'a', 'an', 'was', 'has', 'had', 'have','to','do','of','on','my','any','be','by'] #the words that should be ignored by countvectoriser
    vectorizer = CountVectorizer(stop_words=stopWords)  # adding the words list to countvectoriser
    # training data
    train_set = train # creating the training set
    trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()  # creating tokens froms the trainng set, This is a 2D array
    # print(trainVectorizerArray)  # just to help us debbug
    return vectorizer,trainVectorizerArray

# def update_training_set(train,question,ans):
#     train.append((question[0],ans))
#     pass


# def admin_answer(ques,ans):
#     print 'For question :' , ques
#     print 'Answer given was :', ans
#     print 'type 1 for the answer to remain same and 0 to change the answer'
#     inp = int(raw_input('>>'))
#     if inp == 0:
#         print 'Enter you answer'
#         new_answer = str(raw_input('>>'))
#         return (new_answer)
#     elif inp == 1:
#         return ans
#     else:
#         print 'invalid input'
#         admin_answer(ques,ans)
def main_bot(question_id, user_query):                  # question_id - string, user_query
    question_dict = dict_11_15[question_id]
    answer = model(question_dict, user_query)
    # print(answer)
    return (answer)

