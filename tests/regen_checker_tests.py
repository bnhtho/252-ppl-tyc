#!/usr/bin/env python3
"""Regenerate tests/test_checker.py — run from repo root: python3 tests/regen_checker_tests.py"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "test_checker.py"

CASES: list[tuple[str, str]] = [
    ("Static checking passed", "void main() {}"),
    ("Static checking passed", "void main() { int a = 1; int b = 2; int c = a + b; }"),
    (
        "Static checking passed",
        "int add(int x, int y) {\n    return x + y;\n}\nvoid main() {\n    int sum = add(5, 3);\n}\n",
    ),
    ("Static checking passed", "void main() { int a = 1; float b = 2.0; float c = a + b; }"),
    ("Static checking passed", "void main() { auto a = 1; auto b = 2.0; auto c = a + b; }"),
    (
        "Static checking passed",
        "void main() { float f = readFloat(); printFloat(f); string s = readString(); printString(s); }",
    ),
    ("Static checking passed", "struct P { int x; int y; }; void main() { P p; p.x = 1; p.y = 2; }"),
    ("Static checking passed", "struct P { int x; int y; }; void main() { P p = {1, 2}; }"),
    ("Static checking passed", "void main() { int v = 1; { int v = 2; printInt(v); } }"),
    ("Static checking passed", "void main() { if (1) { printInt(0); } }"),
    ("Static checking passed", "void main() { int i = 0; while (i < 1) { i = i + 1; } }"),
    ("Static checking passed", "void main() { for (int i = 0; i < 2; i = i + 1) { printInt(i); } }"),
    (
        "Static checking passed",
        "void main() { switch (2) { case 1: break; case 2: printInt(2); break; } }",
    ),
    ("Static checking passed", "void main() { while (1) { break; } }"),
    ("Static checking passed", "void main() { for (int i = 0; i < 2; i = i + 1) { continue; } }"),
    ("Static checking passed", "void main() { int a; int b; int c; a = b = c = 1; }"),
    ("Static checking passed", "void main() { int x; int y = (x = 3) + 2; }"),
    ("Static checking passed", "void helper() { return; } void main() { helper(); }"),
    (
        "Static checking passed",
        "struct foo { int x; }; int foo(int a) { return a; } void main() { int z = foo(1); }",
    ),
    ("Static checking passed", "void main() { return; }"),
    ("Static checking passed", "int f() { return 1; } void main() { int x = f(); }"),
    ("Static checking passed", "void main() { auto x; printInt(x); }"),
    ("Static checking passed", "void main() { auto x; auto y = x + 5; printInt(y); }"),
    ("Static checking passed", "struct P { int x; }; void main() { P p; p.x = 1; ++p.x; }"),
    ("Static checking passed", "void main() { int a = 1; int b = 0; int c = a && b; int d = a || b; }"),
    ("Static checking passed", "void main() { int a = 1; int b = 2; int c = a < b; }"),
    ("Static checking passed", "void main() { int a = 7 % 3; }"),
    (
        "Static checking passed",
        'void main() { string a = "x"; string b = "y"; printString(a); printString(b); }',
    ),
    ("Static checking passed", "void main() { int a = !0; }"),
    (
        "Static checking passed",
        "void main() { if (1) { if (0) { printInt(1); } else { printInt(2); } } }",
    ),
    ("Static checking passed", "struct P { int x; }; void main() { P a; P b; a = b; }"),
    ("Static checking passed", "void main() { int a = 1 == 1; }"),
    ("Static checking passed", "void main() { float a = 1.0; float b = 2.0; int c = a != b; }"),
    ("Static checking passed", "void main() { float a = 5.0 / 2.0; }"),
    ("Static checking passed", "void main() { int a = 3 * 4; }"),
    ("Static checking passed", "void main() { for (auto i = 0; i < 1; ++i) { break; } }"),
    ("Static checking passed", "void main() { if (0) { printInt(1); } else { printInt(2); } }"),
    ("Static checking passed", "void main() { switch (1) {} }"),
    ("Static checking passed", "void main() { switch (1) { default: break; } }"),
    ("Static checking passed", "void main() { while (1) { while (1) { break; } break; } }"),
    ("Static checking passed", "void main() { int x = readInt(); }"),
    ("Static checking passed", "void main() { int a = 2; float b = a * 1.5; }"),
    ("Static checking passed", "void main() { int x = 1; { int y = 2; printInt(y); } int z = x + 1; }"),
    ("Redeclared(Variable, x)", "void main() { int x; int x; }"),
    ("Redeclared(Function, f)", "void f() {} void f() {} void main() {}"),
    ("Redeclared(Struct, S)", "struct S { int a; }; struct S { int b; }; void main() {}"),
    ("Redeclared(Parameter, a)", "void f(int a, int a) {} void main() {}"),
    ("Redeclared(Member, x)", "struct S { int x; int x; }; void main() {}"),
    ("Redeclared(Variable, x)", "void f(int x) { int x = 1; } void main() { f(1); }"),
    ("UndeclaredIdentifier(u)", "void main() { int z = u; }"),
    ("UndeclaredIdentifier(y)", "void main() { int x = y; int y = 1; }"),
    ("UndeclaredFunction(missing)", "void main() { missing(); }"),
    ("UndeclaredStruct(T)", "void main() { T t; }"),
    ("UndeclaredStruct(B)", "struct A { B b; }; struct B { int x; }; void main() {}"),
    ("UndeclaredFunction(later)", "void main() { later(); } void later() {}"),
    ("UndeclaredStruct(L)", "void main() { L x; } struct L { int a; };"),
    (
        "TypeCannotBeInferred(BinaryOp(Identifier(a), +, Identifier(b)))",
        "void main() { auto a; auto b; int c = a + b; }",
    ),
    ("TypeCannotBeInferred(Identifier(b))", "void main() { auto a; auto b; a = b; }"),
    ("TypeCannotBeInferred(BlockStmt([VarDecl(auto, a)]))", "void main() { auto a; }"),
    (
        "TypeCannotBeInferred(StructLiteral({IntLiteral(1), IntLiteral(2)}))",
        "void main() { auto x = {1, 2}; }",
    ),
    ("TypeCannotBeInferred(Identifier(a))", "void main() { auto a; auto b; int c = a < b; }"),
    ("TypeCannotBeInferred(Identifier(x))", "f() { auto x; return x; } void main() {}"),
    (
        "TypeMismatchInStatement(IfStmt(if Identifier(f) then BlockStmt([])))",
        "void main() { float f = 1.0; if (f) {} }",
    ),
    (
        "TypeMismatchInStatement(WhileStmt(while Identifier(s) do BlockStmt([])))",
        'void main() { string s = "a"; while (s) {} }',
    ),
    (
        "TypeMismatchInStatement(ForStmt(for None; FloatLiteral(1.0); None do BlockStmt([])))",
        "void main() { for (; 1.0; ) {} }",
    ),
    (
        "TypeMismatchInStatement(SwitchStmt(switch Identifier(f) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))",
        "void main() { float f = 1.0; switch (f) { case 1: break; } }",
    ),
    ("TypeMismatchInExpression(Identifier(s))", "void main() { int x; string s; x = s; }"),
    ("TypeMismatchInStatement(ReturnStmt(return IntLiteral(1)))", "void main() { return 1; }"),
    ("TypeMismatchInStatement(ReturnStmt(return))", "int f() { return; } void main() {}"),
    (
        "TypeMismatchInStatement(ReturnStmt(return StringLiteral('x')))",
        'int f() { return "x"; } void main() {}',
    ),
    (
        "TypeMismatchInStatement(ReturnStmt(return FloatLiteral(2.0)))",
        "f() { return 1; return 2.0; } void main() {}",
    ),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(s)))",
        'void main() { int x = 1; string s = "a"; int z = x + s; }',
    ),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(f), %, IntLiteral(3)))",
        "void main() { float f = 1.0; int z = f % 3; }",
    ),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(x), <, Identifier(s)))",
        'void main() { int x = 1; string s = "a"; int z = x < s; }',
    ),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, IntLiteral(1)))",
        "void main() { float f = 1.0; int z = f && 1; }",
    ),
    ("TypeMismatchInExpression(PrefixOp(!Identifier(f)))", "void main() { float f = 1.0; int z = !f; }"),
    ("TypeMismatchInExpression(PrefixOp(++Identifier(f)))", "void main() { float f = 1.0; ++f; }"),
    ("TypeMismatchInExpression(MemberAccess(Identifier(x).y))", "void main() { int x = 1; int z = x.y; }"),
    (
        "TypeMismatchInExpression(MemberAccess(Identifier(p).bad))",
        "struct P { int x; }; void main() { P p; int z = p.bad; }",
    ),
    ("TypeMismatchInExpression(StringLiteral('a'))", 'void g(int x) {} void main() { g("a"); }'),
    ("TypeMismatchInExpression(FuncCall(g, []))", "void g(int x) {} void main() { g(); }"),
    (
        "TypeMismatchInExpression(FuncCall(g, [IntLiteral(1), IntLiteral(2)]))",
        "void g(int x) {} void main() { g(1, 2); }",
    ),
    ("TypeMismatchInExpression(IntLiteral(5))", "void main() { int y = (5 = 1) + 2; }"),
    (
        "TypeMismatchInExpression(PostfixOp(BinaryOp(Identifier(x), +, IntLiteral(1))++))",
        "void main() { int x = 1; (x + 1)++; }",
    ),
    ("TypeMismatchInExpression(PrefixOp(++IntLiteral(5)))", "void main() { ++5; }"),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(s), /, IntLiteral(1)))",
        'void main() { string s = "a"; int x = s / 1; }',
    ),
    (
        "TypeMismatchInExpression(Identifier(b))",
        "struct P { int x; }; struct Q { int y; }; void main() { P a; Q b; a = b; }",
    ),
    ("TypeMismatchInExpression(FloatLiteral(1.0))", "void main() { int x = 1.0; }"),
    ("TypeMismatchInExpression(StringLiteral('a'))", 'void main() { int x = "a"; }'),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(s), *, IntLiteral(1)))",
        'void main() { string s = "a"; int x = s * 1; }',
    ),
    (
        "TypeMismatchInExpression(BinaryOp(Identifier(s), -, IntLiteral(1)))",
        'void main() { string s = "a"; int x = s - 1; }',
    ),
    ("MustInLoop(BreakStmt())", "void main() { break; }"),
    ("MustInLoop(ContinueStmt())", "void main() { continue; }"),
    ("MustInLoop(ContinueStmt())", "void main() { switch (1) { case 1: continue; } }"),
    ("Static checking passed", 'void main() { printString("hi"); }'),
    ("Static checking passed", "void main() { int a = -1; float b = -1.5; }"),
    ("Static checking passed", "void main() { int a = +1; }"),
    ("Static checking passed", "void main() { {} }"),
    ("Static checking passed", "void main() { while (0) { printInt(1); } }"),
    ("Static checking passed", "struct P { int x; }; void main() { P p; int r = (p.x = 2) + 3; }"),
]

DOCS = [
    "Test a valid minimal program",
    "Test valid int locals and addition",
    "Test valid program with functions",
    "Test valid int and float mixed arithmetic",
    "Test valid auto chain inference float result",
    "Test valid builtins readFloat readString print",
    "Test valid struct and member assignment",
    "Test valid struct literal initialization",
    "Test valid inner block shadows outer local",
    "Test valid if with int condition",
    "Test valid while loop with counter",
    "Test valid for loop with int index",
    "Test valid switch with cases and break",
    "Test valid break inside while",
    "Test valid continue inside for",
    "Test valid chained assignment",
    "Test valid assignment used inside expression",
    "Test valid call to another void function",
    "Test valid struct type and function same name",
    "Test valid void return without value",
    "Test valid int function return and call",
    "Test valid auto inferred from printInt argument",
    "Test valid auto inferred from int literal in addition",
    "Test valid struct member increment",
    "Test valid logical and and or",
    "Test valid relational less-than",
    "Test valid modulus on ints",
    "Test valid two strings printed",
    "Test valid logical not on int",
    "Test valid nested if-else",
    "Test valid struct assignment same type",
    "Test valid equality on ints",
    "Test valid inequality on floats",
    "Test valid float division",
    "Test valid int multiplication",
    "Test valid for with auto and break",
    "Test valid if-else branches",
    "Test valid empty switch",
    "Test valid switch default with break",
    "Test valid nested while with breaks",
    "Test valid readInt assignment",
    "Test valid int to float multiplication",
    "Test valid block with locals and outer use",
    "Test Redeclared variable in same block",
    "Test Redeclared function name",
    "Test Redeclared struct name",
    "Test Redeclared parameter in list",
    "Test Redeclared struct member",
    "Test Redeclared local same as parameter",
    "Test UndeclaredIdentifier in expression",
    "Test UndeclaredIdentifier used before declaration",
    "Test UndeclaredFunction call",
    "Test UndeclaredStruct type for variable",
    "Test UndeclaredStruct in member type before definition",
    "Test UndeclaredFunction called before declaration",
    "Test UndeclaredStruct used before declaration",
    "Test TypeCannotBeInferred two autos in addition",
    "Test TypeCannotBeInferred auto assigned from unresolved auto",
    "Test TypeCannotBeInferred unused auto at end of function",
    "Test TypeCannotBeInferred auto struct literal without context",
    "Test TypeCannotBeInferred relational on two unresolved autos",
    "Test TypeCannotBeInferred return of unresolved auto",
    "Test TypeMismatchInStatement if condition float",
    "Test TypeMismatchInStatement while condition string",
    "Test TypeMismatchInStatement for condition float",
    "Test TypeMismatchInStatement switch expression float",
    "Test TypeMismatch assignment int from string",
    "Test TypeMismatchInStatement void function returning value",
    "Test TypeMismatchInStatement non-void function empty return",
    "Test TypeMismatchInStatement int function returns string",
    "Test TypeMismatchInStatement inferred return inconsistent",
    "Test TypeMismatchInExpression int plus string",
    "Test TypeMismatchInExpression modulus with float operand",
    "Test TypeMismatchInExpression relational int with string",
    "Test TypeMismatchInExpression logical and with float operand",
    "Test TypeMismatchInExpression logical not on float",
    "Test TypeMismatchInExpression increment on float",
    "Test TypeMismatchInExpression member access on int",
    "Test TypeMismatchInExpression unknown struct member",
    "Test TypeMismatchInExpression call string for int param",
    "Test TypeMismatchInExpression call too few arguments",
    "Test TypeMismatchInExpression call too many arguments",
    "Test TypeMismatchInExpression assign to int literal",
    "Test TypeMismatchInExpression postfix increment non-lvalue",
    "Test TypeMismatchInExpression prefix increment on literal",
    "Test TypeMismatchInExpression division string by int",
    "Test TypeMismatchInExpression struct assign different types",
    "Test TypeMismatchInExpression int init with float literal",
    "Test TypeMismatchInExpression int init with string literal",
    "Test TypeMismatchInExpression multiply string by int",
    "Test TypeMismatchInExpression subtract int from string",
    "Test MustInLoop break outside loop",
    "Test MustInLoop continue outside loop",
    "Test MustInLoop continue inside switch",
    "Test valid printString literal",
    "Test valid unary minus int and float",
    "Test valid unary plus",
    "Test valid empty block",
    "Test valid while false body skipped",
    "Test valid member assignment in expression",
]

assert len(CASES) == 100 and len(DOCS) == 100, (len(CASES), len(DOCS))


def emit_source(src: str) -> str:
    body = src.rstrip("\n")
    if "\n" not in body:
        return f"    source = {repr(body)}\n"
    lines = ['    source = """']
    lines.extend(body.split("\n"))
    lines.append('"""')
    return "\n".join(lines) + "\n"


def main() -> None:
    parts: list[str] = [
        '"""\n',
        "Semantic checker tests for TyC (StaticChecker).\n\n",
        "One hundred explicit test functions (test_001 ... test_100).\n",
        '"""\n\n',
        "from tests.utils import Checker\n\n",
    ]
    for i, ((exp, src), doc) in enumerate(zip(CASES, DOCS), 1):
        parts.append(f"def test_{i:03d}():\n")
        parts.append(f'    """{doc}"""\n')
        parts.append(emit_source(src))
        parts.append(f"    expected = {repr(exp)}\n")
        parts.append("    assert Checker(source).check_from_source() == expected\n\n")
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({len(CASES)} tests)")


if __name__ == "__main__":
    main()
