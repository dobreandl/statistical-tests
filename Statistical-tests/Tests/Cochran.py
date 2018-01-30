import os
import math

critical_value_table_01 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.9999, 0.9950, 0.9794, 0.9586, 0.9373, 0.9172, 0.8988, 0.8823, 0.8674, 0.8539, 0.7949, 0.7067, 0.6062, 0.5000],
[0, 0.9933, 0.9423, 0.8831, 0.8335, 0.7933, 0.7606, 0.7335, 0.7107, 0.6912, 0.6743, 0.6059, 0.5153, 0.4230, 0.3333],
[0, 0.9676, 0.8643, 0.7814, 0.7212, 0.6761, 0.6410, 0.6129, 0.5897, 0.5702, 0.5536, 0.4884, 0.4057, 0.3251, 0.2500],
[0, 0.9279, 0.7885, 0.6957, 0.6329, 0.5875, 0.5531, 0.5259, 0.5037, 0.4854, 0.4697, 0.4094, 0.3351, 0.2644, 0.2000],
[0, 0.8828, 0.7218, 0.6258, 0.5635, 0.5195, 0.4866, 0.4608, 0.4401, 0.4229, 0.4084, 0.3529, 0.2858, 0.2229, 0.1667],
[0, 0.8376, 0.6644, 0.5685, 0.5080, 0.4659, 0.4347, 0.4105, 0.3911, 0.3751, 0.3616, 0.3105, 0.2494, 0.1929, 0.1429],
[0, 0.7945, 0.6152, 0.5209, 0.4627, 0.4226, 0.3932, 0.3704, 0.3522, 0.3373, 0.3248, 0.2779, 0.2214, 0.1700, 0.1250],
[0, 0.7544, 0.5727, 0.4810, 0.4251, 0.3870, 0.3592, 0.3378, 0.3207, 0.3067, 0.2950, 0.2514, 0.1992, 0.1521, 0.1111],
[0, 0.7175, 0.5358, 0.4469, 0.3934, 0.3572, 0.3308, 0.3106, 0.2945, 0.2813, 0.2704, 0.2297, 0.1811, 0.1376, 0.1000]
]

critical_value_table_05 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.9985, 0.9750, 0.9392, 0.9057, 0.8772, 0.8534, 0.8332, 0.8159, 0.8010, 0.7880, 0.7341, 0.6602, 0.5813, 0.5000],
[0, 0.9669, 0.8709, 0.7977, 0.7457, 0.7071, 0.6771, 0.6530, 0.6333, 0.6167, 0.6025, 0.5466, 0.4748, 0.4031, 0.3333],
[0, 0.9065, 0.7679, 0.6841, 0.6287, 0.5895, 0.5598, 0.5365, 0.5175, 0.5017, 0.4884, 0.4366, 0.3720, 0.3093, 0.2500],
[0, 0.8412, 0.6838, 0.5981, 0.5441, 0.5065, 0.4783, 0.4564, 0.4387, 0.4241, 0.4118, 0.3645, 0.3066, 0.2513, 0.2000],
[0, 0.7808, 0.6161, 0.5321, 0.4803, 0.4447, 0.4184, 0.3980, 0.3817, 0.3682, 0.3568, 0.3135, 0.2612, 0.2119, 0.1667],
[0, 0.7271, 0.5612, 0.4800, 0.4307, 0.3974, 0.3726, 0.3535, 0.3384, 0.3259, 0.3154, 0.2756, 0.2278, 0.1833, 0.1429],
[0, 0.6798, 0.5157, 0.4377, 0.3910, 0.3595, 0.3362, 0.3185, 0.3043, 0.2926, 0.2829, 0.2462, 0.2022, 0.1616, 0.1250],
[0, 0.6385, 0.4775, 0.4027, 0.3584, 0.3286, 0.3067, 0.2901, 0.2768, 0.2659, 0.2568, 0.2226, 0.1820, 0.1446, 0.1111],
[0, 0.6020, 0.4450, 0.3733, 0.3311, 0.3029, 0.2823, 0.2666, 0.2541, 0.2439, 0.2353, 0.2032, 0.1655, 0.1308, 0.1000]
]

# Calculate and return the sum of values in the list
def get_sum(data):
    _sum = 0.00
    for _value in data:
        _sum = _sum + float(_value)
        
    return _sum
    
# Return the critical value from given table
def get_critical_value(table, row, col):
    if (table == 0.01):
        #print "Row: ", row
        #print "Col: ", col
        return critical_value_table_01[row][col]
    
    return critical_value_table_05[row][col]

    

# Calculate and return the variance of data
def get_variance(data):
    _sum = 0.00;
    _variance = 0.00
    
    # Step 1. Add up all values
    for _value in data:
        # print _value
        _sum = _sum + float(_value);
    
    # Step 2. Square the sum and divide by the number of items
    _sum2 = _sum**2 / len(data)
    
    # Step 3. Sum the square of each value
    _sum3 = 0.00
    for _value in data:
        _val = float(_value)
        _sum3 = _sum3 + _val**2
        
    # Step 4. Substract 
    _sum4 = _sum3 - _sum2
    
    # Step 5. Calculate the degrees of freedom
    _upsilon = len(dataset) - 1

    # Step 6. Calculate the variance
    _variance = _sum4 / _upsilon
        
    return _variance;

# set the working directory
_data_path = 'D:\Projects\Python\Statistics'
os.chdir(_data_path)
print os.getcwd()

print "========================================================================================="
print "Cochran's test for variance outliers"
print "=========================================================================================\n"
print "The NULL HYPOTESIS: The large variance does not differ significantly from the others.\n"

# get the data file name
_filename = raw_input("Enter the data file name: ")

# open the data file
#file = open('heights.csv', 'rb')
file = open(_filename, 'rb')
#print file.read()

# read the data
dataset = file.read().split("\n")
#print dataset

# get the number of populations K in the dataset
_tmp = raw_input('Enter the number of populations: ')
K = int(_tmp);

# calculate the variance for each population
n = 10
variance_list = []
#_chunk_size = len(dataset) / K
for i in range(K):
    #left_index = i * _chunk_size
    left_index = i * n
    #right_index = (i + 1) * _chunk_size - 1
    right_index = (i + 1) * n - 1
    variance_list.append(get_variance(dataset[left_index:right_index]))
    #print variance_list[i]

# find the maximum value of variance
max_variance = max(variance_list)

# compute the Cochran's test statistic
C = max_variance / get_sum(variance_list)
print "The Cochran's test statistic is C = ", C

# get the critical value
alpha = 0.05                                            # level of significance
#upsilon = (len(dataset) / K) - 1
upsilon = n - 1                                         # degrees of freedom
critical_value = get_critical_value(alpha, K, upsilon)
print "The critical value for a level of significance of 0.05 is ", critical_value

if (C < critical_value):
    print "C < critical_value ==> The null hypothesis is held."
else:
    print "C >= critical_value ==> The null hypothesis is rejected."

file.close()
