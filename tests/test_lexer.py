import pytest
from tests.utils import Tokenizer

# ========== Simple Test Cases (100 types) ==========

# --- 1. Keywords ---

def test_kw_01():
    """Keyword: auto"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

def test_kw_02():
    """Keyword: break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_kw_03():
    """Keyword: case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_kw_04():
    """Keyword: continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_kw_05():
    """Keyword: default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_kw_06():
    """Keyword: else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_kw_07():
    """Keyword: float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_kw_08():
    """Keyword: for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_kw_09():
    """Keyword: if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_kw_10():
    """Keyword: int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_kw_11():
    """Keyword: return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_kw_12():
    """Keyword: string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_kw_13():
    """Keyword: struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_kw_14():
    """Keyword: switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_kw_15():
    """Keyword: void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_kw_16():
    """Keyword: while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

# --- 2. Operators ---

def test_op_17():
    """Operator: +"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_op_18():
    """Operator: -"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_op_19():
    """Operator: *"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_op_20():
    """Operator: /"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_op_21():
    """Operator: %"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_op_22():
    """Operator: =="""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_op_23():
    """Operator: !="""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_op_24():
    """Operator: <"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_op_25():
    """Operator: >"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_op_26():
    """Operator: <="""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_op_27():
    """Operator: >="""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_op_28():
    """Operator: ||"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_op_29():
    """Operator: &&"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_op_30():
    """Operator: !"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_op_31():
    """Operator: ++"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_op_32():
    """Operator: --"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_op_33():
    """Operator: ="""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"

def test_op_34():
    """Operator: ."""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

# --- 3. Separators ---

def test_sep_35():
    """Separator: {"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_sep_36():
    """Separator: }"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_sep_37():
    """Separator: ("""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_sep_38():
    """Separator: )"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_sep_39():
    """Separator: ;"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"

def test_sep_40():
    """Separator: ,"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_sep_41():
    """Separator: :"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

# --- 4. Identifiers ---

def test_id_42():
    """Identifier: single char"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_id_43():
    """Identifier: leading underscore"""
    tokenizer = Tokenizer("_var")
    assert tokenizer.get_tokens_as_string() == "_var,<EOF>"

def test_id_44():
    """Identifier: letters and numbers"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_id_45():
    """Identifier: uppercase with underscore"""
    tokenizer = Tokenizer("MY_VAR")
    assert tokenizer.get_tokens_as_string() == "MY_VAR,<EOF>"

def test_id_46():
    """Identifier: multiple underscores"""
    tokenizer = Tokenizer("a_b_c")
    assert tokenizer.get_tokens_as_string() == "a_b_c,<EOF>"

def test_id_47():
    """Identifier: underscore followed by numbers"""
    tokenizer = Tokenizer("_123")
    assert tokenizer.get_tokens_as_string() == "_123,<EOF>"

def test_id_48():
    """Identifier: CamelCase"""
    tokenizer = Tokenizer("CamelCase")
    assert tokenizer.get_tokens_as_string() == "CamelCase,<EOF>"

def test_id_49():
    """Identifier: i"""
    tokenizer = Tokenizer("i")
    assert tokenizer.get_tokens_as_string() == "i,<EOF>"

def test_id_50():
    """Identifier: long name"""
    tokenizer = Tokenizer("long_identifier_name")
    assert tokenizer.get_tokens_as_string() == "long_identifier_name,<EOF>"

def test_id_51():
    """Identifier: keyword-like"""
    tokenizer = Tokenizer("auto1")
    assert tokenizer.get_tokens_as_string() == "auto1,<EOF>"

# --- 5. Numbers ---

def test_num_52():
    """Number: zero"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_num_53():
    """Number: integer"""
    tokenizer = Tokenizer("12345")
    assert tokenizer.get_tokens_as_string() == "12345,<EOF>"

def test_num_54():
    """Number: float with pi"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_num_55():
    """Number: float ending with dot"""
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_num_56():
    """Number: float starting with dot"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_num_57():
    """Number: scientific notation e"""
    tokenizer = Tokenizer("1e10")
    assert tokenizer.get_tokens_as_string() == "1e10,<EOF>"

def test_num_58():
    """Number: scientific notation E negative"""
    tokenizer = Tokenizer("2.5E-3")
    assert tokenizer.get_tokens_as_string() == "2.5E-3,<EOF>"

def test_num_59():
    """Number: float 0.0"""
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_num_60():
    """Number: scientific notation positive"""
    tokenizer = Tokenizer("1.2e+4")
    assert tokenizer.get_tokens_as_string() == "1.2e+4,<EOF>"

def test_num_61():
    """Number: leading zeros"""
    tokenizer = Tokenizer("007")
    assert tokenizer.get_tokens_as_string() == "007,<EOF>"

# --- 6. Strings ---

def test_str_62():
    """String: empty"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_str_63():
    """String: hello"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_str_64():
    """String: space"""
    tokenizer = Tokenizer('" "')
    assert tokenizer.get_tokens_as_string() == " ,<EOF>"

def test_str_65():
    """String: escape chars"""
    tokenizer = Tokenizer('"\\n\\t\\r"')
    assert tokenizer.get_tokens_as_string() == "\\n\\t\\r,<EOF>"

def test_str_66():
    """String: escaped quote"""
    tokenizer = Tokenizer('"quote:\\""')
    assert tokenizer.get_tokens_as_string() == "quote:\\\",<EOF>"

def test_str_67():
    """String: escaped backslash"""
    tokenizer = Tokenizer('"back:\\\\"')
    assert tokenizer.get_tokens_as_string() == "back:\\\\,<EOF>"

def test_str_68():
    """String: digits"""
    tokenizer = Tokenizer('"123"')
    assert tokenizer.get_tokens_as_string() == "123,<EOF>"

def test_str_69():
    """String: math expression"""
    tokenizer = Tokenizer('"a+b=c"')
    assert tokenizer.get_tokens_as_string() == "a+b=c,<EOF>"

def test_str_70():
    """String: comment inside"""
    tokenizer = Tokenizer('"/*comment*/"')
    assert tokenizer.get_tokens_as_string() == "/*comment*/,<EOF>"

def test_str_71():
    """String: more escapes"""
    tokenizer = Tokenizer('"escaped: \\b\\f"')
    assert tokenizer.get_tokens_as_string() == "escaped: \\b\\f,<EOF>"

# --- 7. Comments ---

def test_cm_72():
    """Comment: single line"""
    tokenizer = Tokenizer("// line")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_cm_73():
    """Comment: block"""
    tokenizer = Tokenizer("/* block */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_cm_74():
    """Comment: inline after code"""
    tokenizer = Tokenizer("int x; // c")
    assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"

def test_cm_75():
    """Comment: multiline"""
    tokenizer = Tokenizer("/* multiline \n comment */ x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_cm_76():
    """Comment: empty block"""
    tokenizer = Tokenizer("/***/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_cm_77():
    """Comment: division then comment"""
    tokenizer = Tokenizer("x / 2 // div")
    assert tokenizer.get_tokens_as_string() == "x,/,2,<EOF>"

def test_cm_78():
    """Comment: block inside line"""
    tokenizer = Tokenizer("// /* block */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_cm_79():
    """Comment: line inside block"""
    tokenizer = Tokenizer("/* // line */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_cm_80():
    """Comment: complex block"""
    tokenizer = Tokenizer("/* * */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"
# --- 8. Errors ---

def test_cm_81():
    """Comment: unclosed block"""
    tokenizer = Tokenizer("/* unclosed")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_082():
    """Double comments consecutive"""
    source = '#a\n#b'
    expected = 'Error Token #'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_083():
    """Double hash then single hash"""
    source = '##a\n#b'
    expected = 'Error Token #'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_err_84():
    """Error: unclosed string"""
    tokenizer = Tokenizer('"abc')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"

def test_err_85():
    """Error: unclosed string with newline"""
    tokenizer = Tokenizer('"line1\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: line1\n"

def test_err_86():
    """Error: illegal escape x"""
    tokenizer = Tokenizer('"\\x12"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\x"

def test_err_87():
    """Error: illegal escape space"""
    tokenizer = Tokenizer('"\\ "')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\ "

def test_088():
    """Double comments consecutive (Using # results in Error)"""
    # Vì Tokenizer không hiểu # là comment, nó báo lỗi tại ký tự đầu tiên
    source = '#a\n#b'
    expected = 'Error Token #'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_089():
    """Double hash then single hash (Using # results in Error)"""
    source = '##a\n#b'
    expected = 'Error Token #'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_err_90():
    """Error: illegal character $"""
    tokenizer = Tokenizer("$")
    assert tokenizer.get_tokens_as_string() == "Error Token $"

def test_err_91():
    """Error: unclosed string with escape and newline"""
    tokenizer = Tokenizer('"unclosed\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: unclosed\\n"

# --- 9. Mixed Expressions ---

def test_mix_92():
    """Mix: main function"""
    tokenizer = Tokenizer("void main(){printString(\"Hi\");}")
    assert tokenizer.get_tokens_as_string() == "void,main,(,),{,printString,(,Hi,),;,},<EOF>"

def test_mix_93():
    """Mix: increments and logic"""
    tokenizer = Tokenizer("a++||b--")
    assert tokenizer.get_tokens_as_string() == "a,++,||,b,--,<EOF>"

def test_mix_94():
    """Mix: struct definition"""
    tokenizer = Tokenizer("struct P {float x,y;};")
    assert tokenizer.get_tokens_as_string() == "struct,P,{,float,x,,,y,;,},;,<EOF>"

def test_mix_95():
    """Mix: if statement"""
    tokenizer = Tokenizer("if(a!=b)return;")
    assert tokenizer.get_tokens_as_string() == "if,(,a,!=,b,),return,;,<EOF>"

def test_mix_96():
    """Mix: assignment with string"""
    tokenizer = Tokenizer("auto s = \"str\";")
    assert tokenizer.get_tokens_as_string() == "auto,s,=,str,;,<EOF>"

def test_mix_97():
    """Mix: negative scientific notation"""
    tokenizer = Tokenizer("x=-1.0e-2;")
    assert tokenizer.get_tokens_as_string() == "x,=,-,1.0e-2,;,<EOF>"

def test_mix_98():
    """Mix: while loop"""
    tokenizer = Tokenizer("while(1){break;}")
    assert tokenizer.get_tokens_as_string() == "while,(,1,),{,break,;,},<EOF>"

def test_mix_99():
    """Mix: member access and float"""
    tokenizer = Tokenizer("p.x = .5;")
    assert tokenizer.get_tokens_as_string() == "p,.,x,=,.5,;,<EOF>"

def test_mix_100():
    """Mix: switch case statement"""
    tokenizer = Tokenizer("switch(c){case 1:default:;}")
    assert tokenizer.get_tokens_as_string() == "switch,(,c,),{,case,1,:,default,:,;,},<EOF>"
