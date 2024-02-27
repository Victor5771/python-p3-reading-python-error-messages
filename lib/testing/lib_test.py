class TestSyntaxError:
    '''
    a_syntax_error.py
    '''

    def test_syntax_error(self):
        '''
        multiplies two numbers
        '''

        result = 3 * 5
        print(result)
        
        

class TestTypeError:
    '''
    a_type_error.py
    '''

    def test_type_error(self):
        '''
        adds two numbers
        '''
        
        num1 = 10
        num2 = 20
        result = num1 + num2
        print(result)

class TestAssertionError:
    '''
    an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        evaluates two equal values
        '''
        
        value1 = 10
        value2 = 10
        assert value1 == value2, "Values are not equal"
