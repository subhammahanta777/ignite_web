from __future__ import division
import math
import random
levels = 3
concepts = [
    'counting-',
    'Addition-',
    'Multiplication-',
    'Subtraction-',
    'Division-',
    'Comparing Numbers-',
    'Time-Days of week',
    'Time-Seasons of year',
    'Time-Read a Calendar',
    'Time-Months of year',
    'Time-AM or PM',
    'Time-No. of Days(Month)',
    'Time-Elapsed Time',
    '2D Shapes-Sides',
    '2D Shapes-vertices',
    '2D Shapes-angles',
    '2D Shapes-regular and irregular Polygons',
    '2D Shapes-Classification of triangles and quad',
    '2D Shapes-Lines and line Segments',
    '2D Shapes-Parallel and Perpendicular Lines',
    '2D Shapes-Parts of Circle',
    '3D Shapes-names',
    '3D Shapes-vertices',
    '3D Shapes-Edges',
    '3D Shapes-Faces',
    'Estimation and Rounding -',
    'Money-Coin Values',
    'Money-Making Changes',
    'Patterns-Repeating patterns',
    'Patterns-Growing Patterns',
    'Geometry-2D, 3D figures',
    'Geometry-Polygon',
    'Geometry-Reflection and translation',
    'Geometry-Symmetry',
    'Geometry-Perimeter',
    'Geometry-Area',
    'Geometry-Volume',
    'Geometry-Understanding Shapes',
    'Geometry-Constructions',
    'Geometry-mid-point',
    'Geometry-angle bisector',
    'Geometry-perpendicular lines',
    'Geometry-Types of triangles and properties',
    'Mesurement-units of measurement',
    'Mesurement-Compare size, mass and capacity',
    'Basic Properties-Addition,Sub,Mul and Div',
    'Basic Properties-paranthesis',
    'Basic Properties-Distributive',
    'Division Facts-',
    'Probablity-more,less or equally likely events',
    'Probablity-certain,probable,unlikely and impossible',
    'Probablity-combinations',
    'Probablity-make predictions',
    'Probablity-compound events',
    'Probablity-Theoretical Probablity',
    'Probablity-mutually exclusive',
    'Probablity-simple events',
    'Number Sense-Even or Odd',
    'Number Sense-Number Line',
    'Number Sense-Metric Units(Conversion)',
    'Data and Graphs-Bar Graph',
    'Data and Graphs-Line plots',
    'Data and Graphs-Frequency Charts',
    'Data and Graphs-Histograms',
    'Data and Graphs-Venn Diagrams',
    'Data and Graphs-Stem and Leaf Ploats',
    'Fractions-Simple Fractions',
    'Fractions-Compound Fractions',
    'Fractions-Mixed fractions',
    'Fractions-Add and Subtract Fractions',
    'Decimals-Decimals to fractions',
    'Decimals-Add,Sub ,Mul ,Div of decimals',
    'Geometry-Lines of Symmetry',
    'Geometry-Rotational Symmetry',
    'Whole Numbers-',
    'Roman Numbers-',
    'Integers-Number Line',
    'Integers-Operations with Integers',
    'Number Theory-Divisblity Rules',
    'Number Theory-Prime Numbers',
    'Number Theory-Prime Factorisation',
    'Number Theory-HCF',
    'Number Theory-LCM',
    'Number Theory-Scientific Notation',
    'Exponents and Roots-',
    'Ratios-',
    'Rates -',
    'Proportions-',
    'Percentages-',
    '2D Shapes-Complementry angles',
    '2D Shapes-Supplementary Angles',
    '2D Shapes-Triangle Prop',
    '2D Shapes-Quad Prop',
    '2D Shapes-Adjacent angles',
    'Pytagoras Theorem-',
    'Rational Numbers-',
    'Statsitics-Mean',
    'Statsitics-Median ',
    'Statsitics-Mode ',
    'Statsitics-Range',
    'Coordinate Planes-',
    'Logic-or ',
    'Logic-and ',
    'Logic-not',
    'Logic-At least/ at most /or more / or less',
    'Probablity-Complementry events',
    'Probablity-Sample Space grid',
    'Probablity-Sample Space tree',
    'Data and Graphs-Table of Outcomes',
    'Probablity-Independent Events',
    'Probablity-Dependent Events',
    'Probablity-Sampling without replacement',
    'Probablity-Laws of Probablity',
    'Probablity-Conditional Probablity'

]

# graph that tells the prerequisite concepts for a concept
concepts_graph = {
    0: [],
    1: [0],
    2: [1],
    3: [0],
    4: [1, 3],
    5: [0],
    6: [0],
    7: [],
    8: [0],
    9: [8],
    10: [0],
    11: [0],
    12: [1, 3],
    13: [0],
    14: [0],
    15: [0],
    16: [5, 31],
    17: [13, 15, 16],
    18: [5],
    19: [15],
    20: [15, 18],
    21: [13, 15],
    22: [14],
    23: [13, 15],
    24: [13, 15],
    25: [5],
    26: [0],
    27: [1, 3],
    28: [0, 1, 2, 3, 4],
    29: [0, 1, 2, 3, 4],
    30: [13, 14, 15, 16, 17],
    31: [13, 14, 15],
    32: [2, 15, 19],
    33: [5, 15, 14, 13],
    34: [1, 2, 13, 22, 23],
    35: [1, 2, 13, 22, 23, 24],
    36: [1, 2, 13, 22, 23, 24],
    37: [17],
    38: [0, 13, 14, 15, 18, 19, 20],
    39: [4, 18, 19],
    40: [4, 15, 18],
    41: [4, 15, 18],
    42: [13, 15, 16],
    43: [0, 1, 2, 3, 4, 5],
    44: [0, 1, 2, 3, 4, 5],
    45: [0, 1, 2, 3, 4, 5],
    46: [0, 1, 2, 3, 4, 5],
    47: [1, 2],
    48: [0, 1, 2, 3, 4, 5],
    49: [0, 5],
    50: [0, 5],
    51: [0, 2, 3, 5],
    52: [49, 50, 51],
    53: [0, 2, 4, 5, 51, 49],
    54: [0, 2, 4, 5, 51, 49],
    55: [0, 49, 50, 54],
    56: [0, 1, 49, 50],
    57: [4],
    58: [0, 1],
    59: [0, 1, 2, 3, 4, 5],
    60: [0, 1, 4],
    61: [0, 1, 4, 58],
    62: [0, 1, 4, 58],
    63: [0, 1, 4, 58, 60],
    64: [0, 1, 4, 58, 20],
    65: [0, 1, 4, 58],
    66: [0, 1, 2, 3, 4],
    67: [0, 1, 2, 3, 4, 67],
    68: [0, 1, 2, 3, 4, 67, 68],
    69: [0, 1, 2, 3, 4, 67, 68, 69],
    70: [0, 1, 2, 3, 4, 67],
    71: [0, 1, 2, 3, 4, 70],
    72: [32, 33],
    73: [15, 72],
    74: [1, 2, 3, 4, 5],
    75: [75],
    76: [0, 1, 58],
    77: [74],
    78: [1, 2, 3, 4],
    79: [1, 2, 3, 4, 78],
    80: [79],
    81: [80],
    82: [80],
    83: [1, 2, 3, 4, 25, 84],
    84: [1, 2, 3, 4],
    85: [1, 2, 3, 4],
    86: [1, 2, 3, 4],
    87: [1, 2, 3, 4],
    88: [1, 2, 3, 4, 85],
    89: [1, 15],
    90: [1, 15],
    91: [13, 15, 16],
    92: [13, 15, 16],
    93: [1, 15],
    94: [91, 84],
    95: [67],
    96: [1, 2],
    97: [1, 2, 5],
    98: [5],
    99: [1, 3],
    100: [76],
    101: [0, 1],
    102: [0, 1],
    103: [0, 1, 2],
    104: [0, 1],
    105: [0, 3, 54],
    106: [0, 101, 102],
    107: [0, 101, 102],
    108: [0, 5],
    109: [54, 0, 51, 53],
    110: [0, 51, 54, 53],
    111: [54, 0],
    112: [64, 1, 3, 101, 102, 103],
    113: [112, 64, 4]
}
con_diff = [0] * len(concepts_graph)
k = len(concepts_graph)
# temp=[[0]*k]*k
temp = [[0 for x in range(k)] for y in range(k)]


def func(p, y):
    temp[p][y] = 1
    for x in concepts_graph[y]:
        if (temp[p][x] == 0):
            func(p, x)


# func(4,4)
# print temp[4]
for x in range(k):
    func(x, x)
    for y in range(k):
        con_diff[x] = con_diff[x] + temp[x][y]

diff_level = [0] * len(concepts_graph)
for x in range(len(con_diff)):
    if con_diff[x] <= 3:
        diff_level[x] = 0.25
    elif con_diff[x] <= 7:
        diff_level[x] = 0.5
    else:
        diff_level[x] = 1

# print("Concept and its difficulty(based upon the no. of concepts it is based upon)")
# for x in xrange(len(con_diff)):
#     print("%s - %s : %s" %(x,concepts[x],diff_level[x]))

# database
#
question = [
    ['Question 1 part 1'],
    ['Question 2 part 1', 'Question 2 part 2'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3' ,'Question 2 part 3'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3','Question 2 part 3', 'Question 2 part 3'],
    ['Question 4 part 1', 'Question 4 part 2', 'Question 4 part 3', 'Question 4 part 4', 'Question 4 part 5','Question 2 part 3'],
    ['Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 1 part 1', 'Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 2 part 1', 'Question 2 part 2','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3' ,'Question 2 part 3','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 3 part 1', 'Question 3 part 2', 'Question 3 part 3','Question 2 part 3', 'Question 2 part 3','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 4 part 1', 'Question 4 part 2', 'Question 4 part 3', 'Question 4 part 4', 'Question 4 part 5','Question 2 part 3','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5'],
    ['Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5','Question 5 part 1', 'Question 5 part 2', 'Question 5 part 3', 'Question 5 part 4','Question 2 part 3', 'Question 2 part 3', 'Question 2 part 5','Question 2 part 5']
]
ans = [
    ['1'],
    ['1', '1'],
    ['1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1','1'],
    ['1', '1', '1', '1', '1','1'],
    ['1', '1', '1', '1', '1','1','1'],
    ['1','1', '1', '1', '1', '1','1','1'],
    ['1', '1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1', '1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1', '1','1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1', '1', '1','1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1', '1', '1','1','1','1', '1', '1', '1', '1','1','1'],
    ['1', '1', '1', '1', '1', '1', '1','1','1', '1', '1', '1', '1','1','1']

]

q_graph = {
    0: [1],
    1: [1, 2],
    2: [1, 2, 3],
    3: [1, 2, 3, 4],
    4: [1, 2, 3, 4, 5],
    5: [1, 2, 3, 4, 5, 6],
    6: [1, 2, 3, 4, 5, 6, 7],
    7: [1, 2, 3, 4, 5, 6, 7,8],
    8: [1, 2, 3, 4, 5, 6, 7,8,9],
    9: [1, 2, 3, 4, 5, 6, 7,8,9,10],
    10:[1, 2, 3, 4, 5, 6, 7,8,9,10,11],
    11:[1, 2, 3, 4, 5, 6, 7,8,9,10,11,12],
    12:[1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13],
    13:[1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14],
    14:[1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15]
    }


q_diff = [0] * len(q_graph)
for x in range(len(q_graph)):
    for y in q_graph[list(q_graph.keys())[x]]:
        #         print y
        q_diff[x] = q_diff[x] + diff_level[y]
# to create levels
import copy

# creating levels
q_level = [0] * len(q_graph)
visited = [0] * len(question)
def visited_list(question_id):
    visited[question_id] = 1
def clear_visited_list():
    for i in range(len(question)):
        visited[i]=0

def create_groups(levels):
    c = []
    size = len(q_diff)
    for x in range(size):
        c.append((q_diff[x], x))

    c.sort()
    k = int(math.ceil(size / levels))
    for x in range(size):
        # print (x,k)
        q_level[c[x][1]] = int(x / k)
        # print q_level[c[x][1]]
    return q_level


q_level_list = create_groups(3)


# pick a question in random for the provided level

def get_list(curr_level,tq):
    list_=[]
    num = int(math.ceil(len(question) / levels))
    start_point = num * curr_level
    end_point = start_point + tq - 1
    for x in range (start_point, end_point):
        if(visited[x]==0):
            list_.append(x)
        else:
            pass
    return list_
def random_q(curr_level):
    list=[]
    tq = 0
    #     nq=-1
    for x in q_level:
        #         print x
        if (x == curr_level):
            tq = tq + 1
            #     print tq
    try:
        list_=get_list(curr_level,tq)
    except IndexError:
        return 7
    #     print r
    r=random.choice(list_)
    visited[r]=1
    return r
    # for x in range(len(q_level)):
    #     if (q_level[x] == curr_level):
    #         if (r == 0):
    #             if (visited[x] == 0):
    #                 visited_list(x)
    #                 return x
    #                 r = r - 1

# identify the total no of questions
# def update_correct(question_id):

def total_q(curr_level):
    tq = 0
    #     nq=-1
    for x in q_level:
        #         print x
        if (x == curr_level):
            tq = tq + 1
    return tq


no_of_questions_in_each_level = []
for x in range(levels):
    no_of_questions_in_each_level.append(total_q(x))
correct_list = [0]*len(question)
incorrect_list = [0]*len(question)
def update_correct(question_id):
    correct_list[question_id]=1
def update_incorrect(question_id):
    incorrect_list[question_id]=1


def analysis():
    sum_ = 0
    list_of_weakness=[]
    list_of_strength=[]
    list_of_medium=[]
    for index, element in enumerate(correct_list):
        sum_ = sum_ + ((q_level_list[index] + 1) * (element))
    score = sum_
    master_strong_concept_list = [[]]
    for index1, element1 in enumerate(correct_list):
        if (element1 == 1):
            master_strong_concept_list.append(q_graph[index1])
        else:
            pass
    strong_concept_set = set().union(*master_strong_concept_list)
    # strong_concept_list=list(strong_concept_set)
    master_weak_concept_list = [[]]
    for index1, element1 in enumerate(incorrect_list):
        if (element1 == 1):
            master_weak_concept_list.append(q_graph[index1])
        else:
            pass
    weak_concept_set = set().union(*master_weak_concept_list)
    # weak_concept_list = list(weak_concept_set)
    medium_list = list(strong_concept_set & weak_concept_set)
    strength_list = list(strong_concept_set - weak_concept_set)
    weakness_list = list(weak_concept_set - strong_concept_set)
    for i in range(len(medium_list)):
         list_of_medium.append(concepts[i])
    for i in range(len(weakness_list)):
        list_of_weakness.append(concepts[i])
    for i in range(len(strength_list)):
        list_of_strength.append(concepts[i])
    return score,list_of_strength,list_of_weakness,list_of_medium

def main(question_id, is_correct):
    if(question_id==99999 and is_correct==99999):
        question_id=0
        is_correct=1
        clear_visited_list()
    else:
        pass
    if (is_correct == 1):
        try:
            curr_level = q_level_list[question_id]
        except IndexError:
            curr_level = q_level_list[question_id-1]
        max_level = max(q_level_list)
        next_level = curr_level + 1
        if (next_level <= max_level):
            next_level = next_level
        else:
            next_level = curr_level
        update_correct(question_id)
    else:
        try:
            curr_level = q_level_list[question_id]
        except IndexError:
            curr_level = q_level_list[question_id+1]
        min_level = min(q_level_list)
        next_level = curr_level - 1
        if (next_level >= min_level):
            next_level = next_level
        else:
            next_level = curr_level
        update_incorrect(question_id)
    select_random_question = random_q(next_level)

    if (select_random_question == None):
        select_random_question = question_id
    else:

        pass;

    if(sum(visited)<6):
        score, list_of_strength, list_of_weakness, list_of_medium=analysis()
        return select_random_question,score,list_of_strength,list_of_weakness,list_of_medium
    else:
        score, list_of_strength, list_of_weakness, list_of_medium=analysis()
        return 777,score,list_of_strength,list_of_weakness,list_of_medium