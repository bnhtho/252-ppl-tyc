from build.TyCVisitor import TyCVisitor
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):

# -------------------------------------------------
# Program
# -------------------------------------------------

    def visitProgram(self, ctx):
        return Program([self.visit(d) for d in ctx.decl()])


# -------------------------------------------------
# Declarations
# -------------------------------------------------

    def visitDecl(self, ctx):
        if ctx.structDecl():
            return self.visit(ctx.structDecl())

        if ctx.funcDecl():
            return self.visit(ctx.funcDecl())


    def visitStructDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        members = [self.visit(m) for m in ctx.structMember()]
        return StructDecl(name, members)


    def visitStructMember(self, ctx):

        mtype = self.visit(ctx.getChild(0))
        name = ctx.getChild(1).getText()

        return MemberDecl(mtype, name)

# -------------------------------------------------
# Function
# -------------------------------------------------
    def visitFuncCall(self, ctx):

        name = ctx.IDENTIFIER().getText()

        args = []
        if ctx.exprList():
            args = [self.visit(e) for e in ctx.exprList().expr()]

        return FuncCall(name, args)
    def visitFuncDecl(self, ctx):

        first = ctx.getChild(0).getText()

        if first in ["int", "float", "string", "void"]:
            rtype = self.visit(ctx.getChild(0))
            name = ctx.getChild(1).getText()
        else:
            rtype = None
            name = first

        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockstmt())

        return FuncDecl(rtype, name, params, body)


    def visitParamList(self, ctx):
        return [self.visit(p) for p in ctx.param()]


    def visitParam(self, ctx):
        ptype = self.visit(ctx.getChild(0))
        name = ctx.getChild(1).getText()
        return Param(ptype, name)


# -------------------------------------------------
# Types
# -------------------------------------------------

    def visitType(self, ctx):

        if ctx.builtinType():
            return self.visit(ctx.builtinType())

        return StructType(ctx.IDENTIFIER().getText())


    def visitBuiltinType(self, ctx):

        t = ctx.getText()

        if t == "int":
            return IntType()

        if t == "float":
            return FloatType()

        if t == "string":
            return StringType()

        if t == "void":
            return VoidType()


# -------------------------------------------------
# Statements
# -------------------------------------------------
    def visitStmt(self, ctx):

        child = ctx.getChild(0)

        name = child.__class__.__name__

        if name == "BlockstmtContext":
            return self.visit(child)

        if name == "VarDeclContext":
            return self.visit(child)

        if name == "ForstmtContext":
            return self.visit(child)

        if name == "IfstmtContext":
            return self.visit(child)

        if name == "ReturnstmtContext":
            return self.visit(child)

        if name == "ExprstmtContext":
            return self.visit(child)

        if name == "BreaksmtContext":
            return BreakStmt()

        if name == "WhilestmtContext":
            return self.visit(child)

        if name == "SwitchstmtContext":
            return self.visit(child)

        if name == "ContinuestmtContext":
            return ContinueStmt()

        return None
    def visitBlockstmt(self, ctx):
        stmts = []
        for s in ctx.stmt():
            st = self.visit(s)
            if st is not None:
                stmts.append(st)
        return BlockStmt(stmts)


    def visitVarDecl(self, ctx):

        name = ctx.IDENTIFIER().getText()

        if ctx.getChild(0).getText() == "auto":
            vtype = None
        else:
            vtype = self.visit(ctx.getChild(0))

        init = self.visit(ctx.expr()) if ctx.expr() else None

        return VarDecl(vtype, name, init)


    def visitReturnstmt(self, ctx):

        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)


    def visitExprstmt(self, ctx):
        return ExprStmt(self.visit(ctx.expr()))


    def visitBreakstmt(self, ctx):
        return BreakStmt()


    def visitForstmt(self, ctx):
        init = self.visit(ctx.forInit()) if ctx.forInit() else None
        exprs = ctx.expr()
        cond = self.visit(exprs[0]) if len(exprs) >= 1 else None
        update = self.visit(exprs[1]) if len(exprs) >= 2 else None
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, update, stmt)

    def visitForInit(self, ctx):
        if ctx.varDeclFor():
            return self.visit(ctx.varDeclFor())
        return ExprStmt(self.visit(ctx.expr()))

    def visitVarDeclFor(self, ctx):
        if ctx.AUTO():
            vtype = None
        else:
            vtype = self.visit(ctx.builtinType())
        name = ctx.IDENTIFIER().getText()
        init = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(vtype, name, init)

    def visitIfstmt(self, ctx):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = self.visit(ctx.stmt(1)) if ctx.ELSE() else None
        return IfStmt(cond, then_stmt, else_stmt)

    def visitWhilestmt(self, ctx):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    def visitSwitchstmt(self, ctx):
        expr = self.visit(ctx.expr())
        cases = [self.visit(c) for c in ctx.caseBlock()]
        default = self.visit(ctx.defaultBlock()) if ctx.defaultBlock() else None
        return SwitchStmt(expr, cases, default)

    def visitCaseBlock(self, ctx):
        sign = 1
        if ctx.SUB():
            sign = -1
        val = sign * int(ctx.INTLIT().getText())
        stmts = []
        for s in ctx.stmt():
            st = self.visit(s)
            if st is not None:
                stmts.append(st)
        return CaseStmt(IntLiteral(val), stmts)

    def visitDefaultBlock(self, ctx):
        stmts = []
        for s in ctx.stmt():
            st = self.visit(s)
            if st is not None:
                stmts.append(st)
        return DefaultStmt(stmts)
# -------------------------------------------------
# Expressions
# -------------------------------------------------

    def visitExpr(self, ctx):
        return self.visit(ctx.assignExpr())


    def visitAssignExpr(self, ctx):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalOrExpr())

        lhs = self.visit(ctx.logicalOrExpr())
        rhs = self.visit(ctx.assignExpr())

        return AssignExpr(lhs, rhs)


    def visitLogicalOrExpr(self, ctx):

        exprs = ctx.logicalAndExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            right = self.visit(exprs[i])
            left = BinaryOp(left, "||", right)

        return left


    def visitLogicalAndExpr(self, ctx):

        exprs = ctx.equalityExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            right = self.visit(exprs[i])
            left = BinaryOp(left, "&&", right)

        return left


    def visitEqualityExpr(self, ctx):

        exprs = ctx.relationalExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(exprs[i])
            left = BinaryOp(left, op, right)

        return left


    def visitRelationalExpr(self, ctx):

        exprs = ctx.additiveExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(exprs[i])
            left = BinaryOp(left, op, right)

        return left


    def visitAdditiveExpr(self, ctx):

        exprs = ctx.multiplicativeExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(exprs[i])
            left = BinaryOp(left, op, right)

        return left


    def visitMultiplicativeExpr(self, ctx):

        exprs = ctx.unaryExpr()
        left = self.visit(exprs[0])

        for i in range(1, len(exprs)):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(exprs[i])
            left = BinaryOp(left, op, right)

        return left

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            operand = self.visit(ctx.unaryExpr())
            return PrefixOp(op, operand)
        return self.visit(ctx.postfixExpr())

    def visitPostfixExpr(self, ctx):
        expr = self.visit(ctx.primaryExpr())
        for pp in ctx.postfixPart():
            if pp.postfixOp():
                opctx = pp.postfixOp()
                if opctx.ACCESS():
                    expr = MemberAccess(expr, opctx.IDENTIFIER().getText())
                else:
                    op = "++" if opctx.INCREMENT() else "--"
                    expr = PostfixOp(op, expr)
            else:
                args = []
                if pp.argList():
                    args = [self.visit(e) for e in pp.argList().expr()]
                if isinstance(expr, Identifier):
                    expr = FuncCall(expr.name, args)
                else:
                    raise ValueError("Invalid call target in AST generation")
        return expr

# -------------------------------------------------
# Primary
# -------------------------------------------------

    def visitPrimaryExpr(self, ctx):

        if ctx.IDENTIFIER():
            return Identifier(ctx.IDENTIFIER().getText())

        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))

        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))

        if ctx.STRINGLIT():
            text = ctx.STRINGLIT().getText()

            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]

            return StringLiteral(text)

        if ctx.expr():
            return self.visit(ctx.expr())

        if ctx.structLiteral():
            return self.visit(ctx.structLiteral())

    def visitStructLiteral(self, ctx):
        vals = [self.visit(e) for e in ctx.expr()]
        return StructLiteral(vals)

    def visitExprList(self, ctx):
        return [self.visit(e) for e in ctx.expr()]
