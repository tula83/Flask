# consists of   pytest 
import pytest
class  Number:
    def __init__(self,no):
        self.no=no
    def add(self,value):
        self.no+=value

    def mult(self,value):
        self.no*=value

    def get(self):
        return self.no



def func(x):
    return x+1
def test_answer():
    assert func(2)==3
    assert func(4)!=2

def test_mult():
    assert 2==2


def test_get():
    first=Number(10)
    first.add(10)
    assert  first.get()==20
    first.mult(10)
    assert first.get()==200
    assert first.get()!=2000

def test_negative():
    second=Number(-10)
    second.add(-10)
    assert second.get()==-20

    second.mult(-20)
    assert second.get()==400


# using fixture
# fixture is the  normal function which runs   before execution of test . They are used to feed some data to tests such as database connection,
# urls to test and some sort of input

@pytest.fixture
def input_value():
    input=39
    return input

def test_even_odd(input_value):

    assert input_value%3==0
    assert input_value%2!=0


@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num=100
    assert num < 1000
# it will fail after < 100

@pytest.mark.skipif
@pytest.mark.great
def test_great():
    assert 100 >2



@pytest.mark.square
def test_square():
    assert 7**2==49


@pytest.mark.others
def test_cube():
    assert 2**2 * 2==8
    assert 0**2 * 0==0
    assert (-1)**2 * (-1)==-1

#pytest -m others  --disable-warnings -v --durations=2
# --durations=2 gives 2 slowest  test  case */


# parametrize
@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,33)])
def test_multiplication(num,output):
    assert 11*num==output
#pytest -k parameterize
