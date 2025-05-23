from typing import Tuple
from queue import LifoQueue
import pytest

def check_excess_closing_char(c : str) -> None:
    if c == ']':
        raise ValueError("Excess closing bracket")
    elif c == ')':
        raise ValueError("Excess closing parenthesis")
    elif c == '}':
        raise ValueError("Excess closing brace")
    elif c == '>':
        raise ValueError("Excess closing angle")

def check_wrong_closing_char(c : str, c2 : str) -> None:
    if c == '[' and c2 != ']':
        raise ValueError("Wrong closing bracket")
    elif c == '(' and c2 != ')':
        raise ValueError("Wrong closing parenthesis")
    elif c == '{' and c2 != '}':
        raise ValueError("Wrong closing brace")
    elif c == '<' and c2 != '>':
        raise ValueError("Wrong closing angle")

def check_missing_closing_char(c : str) -> None:
    if c == '[':
        raise ValueError("Missing closing bracket")
    elif c == '(':
        raise ValueError("Missing closing parenthesis")
    elif c == '{':
        raise ValueError("Missing closing brace")
    elif c == '<':
        raise ValueError("Missing closing angle")

def check_missing_opening_char(c : str) -> None:
    if c == ']':
        raise ValueError("Missing opening bracket")
    elif c == ')':
        raise ValueError("Missing opening parenthesis")
    elif c == '}':
        raise ValueError("Missing opening brace")
    elif c == '>':
        raise ValueError("Missing opening angle")

def replace_str_in_opening_and_closing_chars(s : str, str_to_insert : str) -> str:
    if not s:
        return ""
    elif not str_to_insert:
        return s

    n : int = 0

    while n < len(s):
        check_missing_opening_char(s[n])

        if s[n] == '[' or s[n] == '(' or s[n] == '{' or s[n] == '<':
            break

        n += 1

    if n == len(s):
        return s

    stack : LifoQueue[str] = LifoQueue()

    while n < len(s):
        if s[n] != '[' and s[n] != '(' and s[n] != '{' and s[n] != '<':
            break

        stack.put_nowait(s[n])
        n += 1

    if n == len(s):
        check_missing_closing_char(stack.get_nowait())

    pos_last_opening_char : int = n - 1

    while n < len(s):
        if s[n] == ']' or s[n] == ')' or s[n] == '}' or s[n] == '>':
            break;

        n += 1

    if n == len(s):
        check_missing_closing_char(stack.get_nowait())

    pos_first_closing_char : int = n

    while not stack.empty() and n < len(s):
        opening_char : str = stack.get_nowait()

        check_wrong_closing_char(opening_char, s[n])
        n += 1

    if not stack.empty():
        check_missing_closing_char(stack.get_nowait())
    elif n < len(s):
        check_excess_closing_char(s[n])

    pos_last_closing_char : int = n - 1

    return "".join([s[0:pos_last_opening_char + 1],
                   str_to_insert,
                    s[pos_first_closing_char:pos_last_closing_char + 1]]) \
                    + replace_str_in_opening_and_closing_chars(
                        s[pos_last_closing_char + 1:],
                        str_to_insert)

@pytest.mark.parametrize("parameter", [
    ("abcd])}>", "Python"), # check ValueError is thrown because missing opening bracket
    ("abcd)[12345", "Python"), # check ValueError is thrown because missing opening parenthesis
    ("abcd}(12345)}abcd    ", "Python"), # check ValueError is thrown because missing opening brace
    ("1234><A><B><<<<5678[({<C>})]", "Python"), # check ValueError is thrown because missing opening angle
    ("1234[(<>)5678", "Python"), # check ValueError is thrown because wrong closing bracket
    ("Allo(((42))ollA", "Python"), # check ValueError is thrown because wrong closing parenthesis
    (            "yOUhou[()]aD  ra(<[{]>)cghf   ", "Python"), # check ValueError is thrown because wrong closing brace
    ("ab< edfg", "Python"), # check ValueError is thrown because wrong closing angle
    ("1234[(<>)", "Python"), # check ValueError is thrown because missing closing bracket
    ("Allo((())", "Python"), # check ValueError is thrown because missing closing parenthesis
    ("yOUhou[()]aD  ra(<[{{{ }}", "Python"), # check ValueError is thrown because missing closing brace
    ("ab<<   >", "Python"), # check ValueError is thrown because missing closing angle
    ("1234[(<>)]]", "Python"), # check ValueError is thrown because excess closing bracket
    ("Allo(((C++)))))))", "Python"), # check ValueError is thrown because excess closing parenthesis
    ("yOUhou[()]]]]]aD  ra(<[{{{ }}", "Python"), # check ValueError is thrown because excess closing brace
    ("ab<<   >>>> [(<4242>)]", "Python")]) # check ValueError is thrown because excess closing angle
def test_replace_str_in_opening_and_closing_chars__bad_parameters(
        parameter : Tuple[str, str]) -> None:
    with pytest.raises(ValueError):
        replace_str_in_opening_and_closing_chars(*parameter)

@pytest.mark.parametrize("parameter, expected", [
    (("", "Python"), ""),
    (("Hello World !", "Python"), "Hello World !"),
    (("<<[()]>>", "Python"), "<<[(Python)]>>"),
    (("1234{<{5678}>}9101112", "Python"), "1234{<{Python}>}9101112"),
    (("1234<<<A>>><<<B>>>5678[({<  C  >})]", "Python"),
     "1234<<<Python>>><<<Python>>>5678[({<Python>})]"),
    (("    abcd   <([{C++}])>   efgh    ", "Python"), "    abcd   <([{Python}])>   efgh    "),
    (("Allo(((   42 dqsdqsdqsqs )))ollA <>()[]{}<> HoUrA", "Python"),
     "Allo(((Python)))ollA <Python>(Python)[Python]{Python}<Python> HoUrA"),
    (("yOUhou[(     )]aD  ra(<[{ a b c d}]>)cghf   ", "C++"),
     "yOUhou[(C++)]aD  ra(<[{C++}]>)cghf   "),
    ((" a b<<()>> b a ", "C++"), " a b<<(C++)>> b a "),
    (("[[]] << >> {{ }}((    1234 ))", "C++"), "[[C++]] <<C++>> {{C++}}((C++))"),
    (("{{{{ }}}} 123456789<<>> 123456789    (( ))123456789 []", "C++"),
     "{{{{C++}}}} 123456789<<C++>> 123456789    ((C++))123456789 [C++]")])
def test_replace_str_in_opening_and_closing_chars__good_parameters(
        parameter : Tuple[str, str], expected : str) -> None:
    assert replace_str_in_opening_and_closing_chars(*parameter) == expected
