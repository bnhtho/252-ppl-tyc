import pytest
from tests.utils import Parser



def test_prog_01():
    """Empty program"""
    assert Parser("").parse() == "success"

def test_prog_02():
    """Minimal program with main"""
    assert Parser("void main() {}").parse() == "success"

def test_prog_03():
    """Function with explicit return type"""
    assert Parser("int add(int a, int b) { return a + b; }").parse() == "success"

def test_prog_04():
    """Function with inferred return type"""
    assert Parser("add(int a, int b) { return a + b; }").parse() == "success"

def test_prog_05():
    """Function with no parameters"""
    assert Parser("void run() {}").parse() == "success"

def test_prog_06():
    """Multiple functions sequence"""
    source = """
        void func1() {}
        int func2() { return 1; }
        void main() {}
    """
    assert Parser(source).parse() == "success"

def test_prog_07():
    """Function with many parameters"""
    assert Parser("void f(int a, float b, string c, MyStruct d) {}").parse() == "success"

def test_prog_08():
    """Function parameters mixed types"""
    assert Parser("void f(int x, float y) {}").parse() == "success"

def test_prog_09():
    """Void return type explicit"""
    assert Parser("void f() { return; }").parse() == "success"

def test_prog_10():
    """Recursive function structure"""
    assert Parser("int fib(int n) { return fib(n-1); }").parse() == "success"




def test_struct_11():
    """Simple struct declaration"""
    assert Parser("struct Point { int x; int y; };").parse() == "success"

def test_struct_12():
    """Empty struct"""
    assert Parser("struct Empty {};").parse() == "success"

def test_struct_13():
    """Struct with mixed types"""
    assert Parser("struct Person { string name; int age; float height; };").parse() == "success"

def test_struct_14():
    """Struct member using another struct type"""
    source = """
        struct Point { int x; };
        struct Line { Point p1; Point p2; };
    """
    assert Parser(source).parse() == "success"

def test_struct_15():
    """Program with Structs and Functions"""
    source = """
        struct Data { int val; };
        void main() { Data d; }
    """
    assert Parser(source).parse() == "success"

def test_struct_16():
    """Struct declaration must end with semicolon"""
    assert Parser("struct A { int x; };").parse() == "success"

def test_struct_17():
    """Multiple independent structs"""
    assert Parser("struct A {}; struct B {}; void main(){}").parse() == "success"

def test_struct_18():
    """Struct with many members"""
    assert Parser("struct Large { int a; int b; int c; int d; };").parse() == "success"

def test_struct_19():
    """Struct member names"""
    assert Parser("struct A { int _x; float y123; };").parse() == "success"

def test_struct_20():
    """Struct cannot be nested (Testing valid flat structure)"""
    source = """
        struct A { int x; };
        struct B { int y; };
    """
    assert Parser(source).parse() == "success"




def test_var_21():
    """Auto with initialization"""
    assert Parser("void main() { auto x = 10; }").parse() == "success"

def test_var_22():
    """Auto without initialization"""
    assert Parser("void main() { auto x; }").parse() == "success"

def test_var_23():
    """Explicit type with initialization"""
    assert Parser("void main() { int x = 10; }").parse() == "success"

def test_var_24():
    """Explicit type without initialization"""
    assert Parser("void main() { float y; }").parse() == "success"

def test_var_25():
    """String variable declaration"""
    assert Parser('void main() { string s = "hello"; }').parse() == "success"

def test_var_26():
    """Struct variable declaration"""
    assert Parser("void main() { Point p; }").parse() == "success"

def test_var_27():
    """Struct variable init with brace"""
    assert Parser("void main() { Point p = {1, 2}; }").parse() == "success"

def test_var_28():
    """Multiple variable declarations"""
    assert Parser("void main() { int a; float b; auto c = 1; }").parse() == "success"

def test_var_29():
    """Variable init with complex expression"""
    assert Parser("void main() { int x = (1 + 2) * 3; }").parse() == "success"

def test_var_30():
    """Struct init with nested braces"""
    assert Parser("void main() { Line l = {{1,1}, {2,2}}; }").parse() == "success"




def test_stmt_31():
    """Block statement"""
    assert Parser("void main() { { int x; } }").parse() == "success"

def test_stmt_32():
    """Empty block"""
    assert Parser("void main() { {} }").parse() == "success"

def test_stmt_33():
    """If statement simple"""
    assert Parser("void main() { if (x) return; }").parse() == "success"

def test_stmt_34():
    """If-Else statement"""
    assert Parser("void main() { if (x == 1) y = 2; else y = 3; }").parse() == "success"

def test_stmt_35():
    """If-Else with blocks"""
    assert Parser("void main() { if (a) { x=1; } else { x=2; } }").parse() == "success"

def test_stmt_36():
    """Nested If"""
    assert Parser("void main() { if (a) if (b) c=1; else c=2; }").parse() == "success"

def test_stmt_37():
    """While loop"""
    assert Parser("void main() { while (i < 10) i++; }").parse() == "success"

def test_stmt_38():
    """While loop with block"""
    assert Parser("void main() { while (1) { break; } }").parse() == "success"

def test_stmt_39():
    """For loop standard"""
    assert Parser("void main() { for (int i=0; i<10; i++) x=i; }").parse() == "success"

def test_stmt_40():
    """For loop with auto"""
    assert Parser("void main() { for (auto i=0; i<10; ++i) {} }").parse() == "success"
def test_stmt_41():
    """For loop infinite"""
    assert Parser("void main() { for (;;) break; }").parse() == "success"

def test_stmt_42():
    """For loop missing init"""
    assert Parser("void main() { for (; i<10; i++) x=1; }").parse() == "success"

def test_stmt_43():
    """For loop missing update"""
    assert Parser("void main() { for (int i=0; i<10; ) i++; }").parse() == "success"

def test_stmt_44():
    """Switch statement simple"""
    assert Parser("void main() { switch(x) { case 1: break; } }").parse() == "success"

def test_stmt_45():
    """Switch with default"""
    assert Parser("void main() { switch(x) { case 1: y=1; default: y=0; } }").parse() == "success"

def test_stmt_46():
    """Switch empty"""
    assert Parser("void main() { switch(x) {} }").parse() == "success"

def test_stmt_47():
    """Switch fallthrough"""
    assert Parser("void main() { switch(x) { case 1: case 2: y=1; break; } }").parse() == "success"

def test_stmt_48():
    """Break statement"""
    assert Parser("void main() { while(1) break; }").parse() == "success"

def test_stmt_49():
    """Continue statement"""
    assert Parser("void main() { for(;;) continue; }").parse() == "success"

def test_stmt_50():
    """Return statement with expression"""
    assert Parser("int f() { return x + 1; }").parse() == "success"




def test_expr_51():
    """Addition and Subtraction"""
    assert Parser("void main() { x = a + b - c; }").parse() == "success"

def test_expr_52():
    """Multiplication and Division"""
    assert Parser("void main() { x = a + b * c; }").parse() == "success"

def test_expr_53():
    """Parentheses grouping"""
    assert Parser("void main() { x = (a + b) * c; }").parse() == "success"

def test_expr_54():
    """Modulo operator"""
    assert Parser("void main() { x = a % b; }").parse() == "success"

def test_expr_55():
    """Unary minus and plus"""
    assert Parser("void main() { x = -a + +b; }").parse() == "success"

def test_expr_56():
    """Logical AND OR"""
    assert Parser("void main() { if (a && b || c) return; }").parse() == "success"

def test_expr_57():
    """Logical NOT"""
    assert Parser("void main() { if (!a) return; }").parse() == "success"

def test_expr_58():
    """Equality operators"""
    assert Parser("void main() { if (a == b && c != d) return; }").parse() == "success"

def test_expr_59():
    """Relational operators"""
    assert Parser("void main() { if (a < b && c >= d) return; }").parse() == "success"

def test_expr_60():
    """Chained assignment"""
    assert Parser("void main() { a = b = c = 0; }").parse() == "success"

def test_expr_61():
    """Postfix increment"""
    assert Parser("void main() { x++; }").parse() == "success"

def test_expr_62():
    """Prefix decrement"""
    assert Parser("void main() { --x; }").parse() == "success"

def test_expr_63():
    """Complex math expression"""
    assert Parser("void main() { x = -a * (b + c) / d % e; }").parse() == "success"

def test_expr_64():
    """Expression statement"""
    assert Parser("void main() { x + y; }").parse() == "success"

def test_expr_65():
    """Function call as expression"""
    assert Parser("void main() { x = f(1); }").parse() == "success"

def test_expr_66():
    """Function call multiple args"""
    assert Parser("void main() { f(1, 2, a+b); }").parse() == "success"

def test_expr_67():
    """Struct member access"""
    assert Parser("void main() { x = p.x; }").parse() == "success"

def test_expr_68():
    """Chained member access"""
    assert Parser("void main() { x = rect.p1.x; }").parse() == "success"

def test_expr_69():
    """Member access on function call"""
    assert Parser("void main() { getPoint().x = 10; }").parse() == "success"

def test_expr_70():
    """Assignment to member"""
    assert Parser("void main() { p.x = 10; }").parse() == "success"




def test_complex_71():
    """For loop complex init"""
    assert Parser("void main() { for (i = a*b; i < n+m; i = i + 1) {} }").parse() == "success"

def test_complex_72():
    """Call with struct literal"""
    assert Parser("void main() { f({1, 2}); }").parse() == "success"

def test_complex_73():
    """Switch with constant expr"""
    assert Parser("void main() { switch(x) { case 3: break; } }").parse() == "success"

def test_complex_74():
    """Deeply nested blocks"""
    assert Parser("void main() { {{{}}} }").parse() == "success"

def test_complex_75():
    """Mixed operators precedence"""
    assert Parser("void main() { flag = !p.x++ * 5 < 10 && a || b; }").parse() == "success"

def test_complex_76():
    """For loop decl explicit type"""
    assert Parser("void main() { for (int i=0; i<10; i++) {} }").parse() == "success"

def test_complex_77():
    """Empty return in non-void function"""
    assert Parser("int f() { return; }").parse() == "success"

def test_complex_78():
    """Built-in IO calls"""
    assert Parser('void main() { printString("Hi"); int x = readInt(); }').parse() == "success"

def test_complex_79():
    """Comment handling"""
    source = """
        /* Block */
        void main() {
            // Line
            int x;
        }
    """
    assert Parser(source).parse() == "success"

def test_complex_80():
    """Function call nested"""
    assert Parser("void main() { f(g(h()), 1); }").parse() == "success"

def test_complex_81():
    """Struct assignment"""
    assert Parser("void main() { p1 = p2; }").parse() == "success"

def test_complex_82():
    """Scientific notation"""
    assert Parser("void main() { x = 1.2e-3 + 5.; }").parse() == "success"

def test_complex_83():
    """Complex if condition"""
    assert Parser("void main() { if ((a || b) && (c > d)) {} }").parse() == "success"

def test_complex_84():
    """String literal in variable init"""
    assert Parser('void main() { string s = "escaped: \\n"; }').parse() == "success"

def test_complex_85():
    """Negative number in switch case"""
    assert Parser("void main() { switch(x) { case -1: break; } }").parse() == "success"

def test_complex_86():
    """Default clause must be at the end"""
    source = "void main() { switch(x) { case 1: break; case 2: break; default: break; } }"
    assert Parser(source).parse() == "success"
def test_complex_87():
    """Empty statement - Error if semi is stand alone"""
    assert Parser("void main() { ; }").parse() == "Error on line 1 col 14: ;"
def test_complex_88():
    """Expression statement side effects"""
    assert Parser("void main() { a = 5; b++; f(); }").parse() == "success"

def test_complex_89():
    """Struct decl no members"""
    assert Parser("struct Empty {}; void main() { Empty e; }").parse() == "success"

def test_complex_90():
    """Complex Program Structure"""
    source = """
        struct Node { int val; };
        Node create() { Node n; return n; }
        void main() {
            auto x = create();
            x.val = 10;
        }
    """
    assert Parser(source).parse() == "success"

def test_err_91():
    """Error: Missing semicolon after variable decl"""
    assert Parser("void main() { int x }").parse() == "Error on line 1 col 20: }"

def test_err_92():
    """Error: Missing closing brace for block"""
    assert Parser("void main() { { int x; }").parse() == "Error on line 1 col 24: <EOF>"

def test_err_94():
    """Error: Struct missing semicolon at end"""
    assert Parser("struct A { int x; }").parse() == "Error on line 1 col 19: <EOF>"

def test_err_95():
    """Error: Function missing body (prototype)"""
    assert Parser("void main();").parse() == "Error on line 1 col 11: ;"

def test_err_96():
    """Error: If missing parentheses"""
    assert Parser("void main() { if x > 0 {} }").parse() == "Error on line 1 col 17: x"

def test_err_97():
    """Error: Unbalanced parentheses"""
    assert Parser("void main() { x = (1 + 2; }").parse() == "Error on line 1 col 24: ;"

def test_err_98():
    """Error: Global variable declaration - error"""
    result = Parser("int global_x; void main() {}").parse()
    assert result == "Error on line 1 col 12: ;"

def test_err_100():
    """Error: Missing colon in switch case"""
    assert Parser("void main() { switch(x) { case 1 break; } }").parse() == "Error on line 1 col 33: break"

def test_case_101():
    """Khởi tạo struct lồng nhau (Nested Struct Init)"""
    source = "void main() { Point p = {1, {2, 3}}; }"
    assert Parser(source).parse() == "success"

def test_case_102():
    """Hàm trả về kiểu dữ liệu Identifier (Struct)"""
    source = "Rect create() { Rect r; return r; } void main() {}"
    assert Parser(source).parse() == "success"
