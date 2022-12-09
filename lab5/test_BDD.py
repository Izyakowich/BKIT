from main import get_roots
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("equation.feature")

@given(parsers.parse("The A coefficient {A:d}"), target_fixture="coefA")
def t_root_input_1(A):
    return A

@given(parsers.parse('The B coefficient {B:d}'), target_fixture="coefB")
def t_root_input_2(B):
    return B

@given(parsers.parse('The C coefficient {C:d}'), target_fixture="coefC")
def t_root_input_3(C):
    return C

@when(parsers.parse('Solve the equation'), target_fixture="equ")
def t_root_solve(coefA, coefB, coefC):
    return get_roots(coefA, coefB, coefC)

@then(parsers.parse("I get {zero:d} roots"))
def t_then(equ, zero):
    assert len(equ) == zero