class Complex:
    '''
    Purpose: (What does an object of this class represent?) A complex number with a real and imaginary
    component 
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    self.real - a numeric value that is the real component of a complex number
    self.imag - a numveric value that is the coefficient of the imaginary component of a complex
    number
    Methods: (What methods does this class have, and what does each do in a few words?)
    __init__ - the constructor that initializes self.real and self.imag instance variables
    get_real - a getter method that returns the self.real
    get_imag - a getter method that returns self.imag instance variable
    set_real - A setter method that reassigns self.real instance variable to a new value
    set_imag - A setter method that reassigns self.imag instance variable to a new value
    __add__ overload method that adds imaginary and real components of two complex numbers (self and other)
    together
    __mul__ multiplies complex numbers self and other together the way complex number multiplication is
    __eq__ special overload method compares Complex objects other and self and returns True if they're
    equivalent
    '''

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return (f'{str(self.real)} + {(str(self.imag))}i')

    def get_real(self):
        return self.real
    def get_imag(self):
        return self.imag
    def set_real(self, new_real):
        self.real = new_real
    def set_imag(self, new_imag):
        self.imag = new_imag
    

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
        # i don't know if i need the spaces or not around the plus sign thats a string
    
    def __mul__(self, other): 
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    # def __eq__(self, other):



class Decision: 
    '''
    Purpose: (What does an object of this class represent?) - an object of this class is a decision
    or question to be made with options and results in the form of strings or more decision objects.
    starts with one decision point, presents options for that decision, and goes into more options if you choose another 
    decision object. 
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    self.prompt - a string representing the prompt for decision that is printed before options are displayed 
    self.options - a list of strings, each representing a possible option the user can select
    self.results - a list including both strings and more decision objects. list is same length as self.options
    Can lead to another decision or a final result as a string. 
    Methods: (What methods does this class have, and what does each do in a few words?)
    __init__ - initializes self.options and self.results and assigns them to empty lists. also creates a prompt instance
    variable
    add_option - method takes in an option and a result. Option is only a string, but result is a string or another decision
    object. add_option method appends the option and result to the end of the respective self.option and self.results lists
    returns nothing
    run - has no parameters besides self. run executes a decision allowing the user to choose from options for that 
    decision. Verifies that self.options isn't an empty list and if its not prints out the prompt for the Decision
    object and the self.options. It takes in a number input for the users choice and returns a string if the user chose 
    an ending string, or calls the run method again on a new Decision object if the user chooses a Decision object. 
    Run goes until it returns a string.



    '''

    def __init__(self, prompt):
        self.prompt = prompt
        self.options = []
        self.results = []
    
    def add_option(self, option, result):
        self.options.append(option)
        self.results.append(result)
    def __str__(self):
        return self.results
    
    def run(self):
        if self.options == []:
           return 'No options available'
        
        print(f'\n{self.prompt}\n')
        for i in range(len(self.options)):
            print(f'{i}. {self.options[i]}')
        print(range(len(self.options)))
        choice = (input((f'Enter an number between 0 and {len(self.options)-1}:')))
        
        while (choice.isdigit() == False) or (int(choice) > len(self.options)-1) or (int(choice) < 0):  
              print('Invalid choice, try again')
              choice = (input(f'Enter an number between 0 and {len(self.options)-1}:'))
        
        ele  = self.results[int(choice)]
        # print(ele)
        # print(type(ele))
        if type(ele) == str:
        #    print(type(str(self.results[int(choice)])))
           print(str(self.results[int(choice)]))
           return str(self.results[int(choice)])
      
        else:
            # print(str(ele))
            return ele.run()
           
            
        

class Flowchart: 
    '''
    Purpose: (What does an object of this class represent?)
    Takes in a name of a flowchart. A Flowchart object represents a decision tree or sequence taken through a csv file
    using the Decision class using a set of choices and options. Flowchart object represents a series of decisions,
    options, and results taken in in the form of a file.
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    self.decisions - a list of Decision objects read in from the CSV file in object form, and not as strings
    Methods: (What methods does this class have, and what does each do in a few words?)
    __init__ - a constructor method that takes in self variable and a name of a csv file we're making a flowchart for. 
    init initializes an empty list self.decisions which will hold all of the decisions in the file. The constructor
    loops through each line of the file adding all decision objects to self.decisions, and all corresponding
    "endings" and "paths" to self.options and self.results using the add_options method for each particular decision. 
    start(self) - a method taking in only self which is used to call the .run() method from the Decision class
    on the first element in self.decisions. start returns the output of .run() method. 

    '''
   
    def __init__(self, filename):
        
        
        self.decisions = []
        
        
        Decision.__init__(self, 0)
        
        self.options = []
        self.results = []
        fp = open(filename)
        for line in fp:
            split1 = line.split(',')
            # print(split1[1])
            if split1[0] == "Decision":
               self.decisions.append(Decision(split1[2]))
            
            if (split1[0] == 'Ending'):
               self.decisions[int(split1[1])].add_option((split1[2]), (split1[3]).strip())
        
            if split1[0] == 'Path':
               self.decisions[int(split1[1])].add_option(split1[2], self.decisions[int(split1[3])])
               #option and result
        fp.close()
        self.prompt = self.decisions[0]
        
        
    def start(self):
        
        
        time = (self.decisions[0]).run()
        return time
        # return self.decisions[0].run()


         

if __name__ == '__main__':
    courses = Flowchart('next_course.csv')
    dragon = Flowchart('story1.csv')
    # courses.start()


