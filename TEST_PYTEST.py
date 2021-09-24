import pytest

DATA1 = [-10,-1,0,1,10]               # Список
DATA2 = {i ** 2 for i in range(10)}   # Множество

#LIST TESTS
@pytest.mark.parametrize("data,num,res",[(DATA1,0,0),  # Ожидание чётности от первого числа в списке
                                         (DATA1,4,0),  # Ожидание чётности от пятого числа в списке
                                         (DATA1,3,1)]) # Ожидание нечётности от четвёртого числа в списке
def test_DATA1_chet(data,num,res):
    assert data[num] %2 == res                         # Проверка чётности числа

#SET TESTS
@pytest.mark.parametrize("exep,num",[(AssertionError,15),   # Ожидание ошибки условия
                                     (TypeError,DATA1)])    # Ожидание ошибки типа данных
                                     
def test_DATA2_error(exep,num):
    with pytest.raises(exep):                           
         assert num in DATA2                                # Проверка на наличие элемента в множестве

def test_DATA2_good():
    assert 2**2 in DATA2