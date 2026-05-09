"""
AST Generation test cases for TyC compiler
Total: 100 test cases
"""

import pytest
from tests.utils import ASTGenerator


# ================= PROGRAM =================

def test_program_1():
    source = "void main(){}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_program_2():
    source = "int main(){}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_program_3():
    source = "float main(){}"
    expected = "Program([FuncDecl(FloatType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_program_4():
    source = "string main(){}"
    expected = "Program([FuncDecl(StringType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_program_5():
    source = "void a(){} void b(){}"
    expected = "Program([FuncDecl(VoidType(), a, [], BlockStmt([])), FuncDecl(VoidType(), b, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= LITERAL =================

def test_literal_1():
    source = "int main(){return 1;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(1))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_literal_2():
    source = "int main(){return 0;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(0))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_literal_3():
    source = "float main(){return 1.5;}"
    expected = "Program([FuncDecl(FloatType(), main, [], BlockStmt([ReturnStmt(return FloatLiteral(1.5))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_literal_4():
    source = 'string main(){return "hello";}'
    expected = "Program([FuncDecl(StringType(), main, [], BlockStmt([ReturnStmt(return StringLiteral('hello'))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_literal_5():
    source = 'string main(){return "";}'
    expected = "Program([FuncDecl(StringType(), main, [], BlockStmt([ReturnStmt(return StringLiteral(''))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= IDENTIFIER =================

def test_identifier_1():
    source = "int main(){return a;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return Identifier(a))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_identifier_2():
    source = "int main(){return abc;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return Identifier(abc))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_identifier_3():
    source = "int main(){return value;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return Identifier(value))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_identifier_4():
    source = "int main(){return result;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return Identifier(result))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_identifier_5():
    source = "int main(){return x;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return Identifier(x))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= VAR DECL =================

def test_vardecl_1():
    source = "void main(){int a;}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_vardecl_2():
    source = "void main(){float b;}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(FloatType(), b)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_vardecl_3():
    source = "void main(){string s;}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StringType(), s)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_vardecl_4():
    source = "void main(){auto x=5;}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x = IntLiteral(5))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_vardecl_5():
    source = "void main(){int a=1;}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a = IntLiteral(1))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= FUNCTION DECL =================

def test_funcdecl_1():
    source = "void foo(){}"
    expected = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_funcdecl_2():
    source = "int add(int a,int b){}"
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_funcdecl_3():
    source = "float square(float x){}"
    expected = "Program([FuncDecl(FloatType(), square, [Param(FloatType(), x)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_funcdecl_4():
    source = "string getName(){}"
    expected = "Program([FuncDecl(StringType(), getName, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_funcdecl_5():
    source = "add(int a,int b){}"
    expected = "Program([FuncDecl(None, add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= STRUCT =================

def test_struct_1():
    source = "struct A{int x;};"
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_struct_2():
    source = "struct A{int x; int y;};"
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_struct_3():
    source = "struct A{string s;};"
    expected = "Program([StructDecl(A, [MemberDecl(StringType(), s)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_struct_4():
    source = "struct Point{float x; float y;};"
    expected = "Program([StructDecl(Point, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_struct_5():
    source = "struct Node{int value;};"
    expected = "Program([StructDecl(Node, [MemberDecl(IntType(), value)])])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= BINARY =================

def test_binary_1():
    source = "int main(){return a+b;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_binary_2():
    source = "int main(){return a-b;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), -, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_binary_3():
    source = "int main(){return a*b;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), *, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_binary_4():
    source = "int main(){return a/b;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), /, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_binary_5():
    source = "int main(){return a+b*c;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= UNARY =================

def test_unary_1():
    source = "int main(){return ++a;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return UnaryOp('++', Identifier(a)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_unary_2():
    source = "int main(){return --a;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return UnaryOp('--', Identifier(a)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_unary_3():
    source = "int main(){return !a;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return UnaryOp('!', Identifier(a)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= ASSIGN =================

def test_assign_1():
    source = "int main(){a=5;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a), IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_assign_2():
    source = "int main(){a=b;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a), Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= IF =================

def test_if_1():
    source = "int main(){if(a) return 1;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([IfStmt(Identifier(a), ReturnStmt(IntLiteral(1)), None)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_if_2():
    source = "int main(){if(a) return 1; else return 2;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([IfStmt(Identifier(a), ReturnStmt(IntLiteral(1)), ReturnStmt(IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= WHILE =================

def test_while_1():
    source = "int main(){while(a) break;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([WhileStmt(Identifier(a), BreakStmt())]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_while_2():
    source = "int main(){while(a>0) a=a-1;}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([WhileStmt(BinaryOp(Identifier(a), >, IntLiteral(0)), ExprStmt(AssignExpr(Identifier(a), BinaryOp(Identifier(a), -, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= FUNCTION CALL =================

def test_call_1():
    source = "void main(){foo();}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_call_2():
    source = "void main(){foo(1,2);}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ================= NESTED =================

def test_nested_1():
    source = "int main(){return (a+b)*(c+d);}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), +, Identifier(d))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_nested_2():
    source = "int main(){if(a){while(b) break;}}"
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([IfStmt(Identifier(a), BlockStmt([WhileStmt(Identifier(b), BreakStmt())]), None)]))])"
    assert str(ASTGenerator(source).generate()) == expected
