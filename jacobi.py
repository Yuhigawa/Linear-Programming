from manimlib.imports import *

class Jacobi(Scene):

    def construct(self):
        # self.scene1()
        # self.wait(2)
        # self.clear()
        self.scene2()
        # self.wait(2)
        # self.clear()
        


    def scene1(self):
        texto1 = TextMobject("Seja:")

        matrix1 = TexMobject("A = \\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ a_{n1} & a_{n2} & \\cdots & a_{nn} \\\ \\end{bmatrix},")
        matrix2 = TexMobject("X = \\begin{bmatrix} x_{1} \\\ x_{2} \\\ \\vdots \\\ x_{n} \\end{bmatrix} \\mbox{ e  }")
        matrix3 = TexMobject("b = \\begin{bmatrix} b_{1} \\\ b_{2} \\\ \\vdots \\\ b_{n} \\end{bmatrix}")

        texto1.to_edge(UP + LEFT)
        matrix2.move_to(matrix1, RIGHT)
        matrix3.move_to(matrix2, RIGHT)

        self.play(FadeIn(texto1))
        self.play(Write(matrix1))
        self.wait(1)
        self.play(matrix1.to_edge, LEFT, .5)
        self.play(Write(matrix2), Write(matrix3))


    def scene2(self):
        texto1 = TextMobject("A pode ser decomposto como: ")
        texto2 = TexMobject("A = D + L + U", tex_to_color_map={"D": YELLOW, "U": GREEN, "L": BLUE})
        
        texto1.to_edge(UP + LEFT)

        self.play(Write(texto1))
        self.wait(1)
        self.play(Write(texto2))
        self.play(FadeOut(texto2))
        self.play(Write(texto2.next_to(texto1, RIGHT)))
        self.wait(1)        

# ---------------------------------------------------------------------

        matrix_A = TexMobject("A = \\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ a_{n1} & a_{n2} & \\cdots & a_{nn} \\\ \\end{bmatrix}")
        text_A = TexMobject("A = ")
        
        # self.add(matrix_A)
        self.play(Write(matrix_A))
        self.wait(1)
        self.play(matrix_A.to_edge, LEFT, 0.5)
        self.wait(1)
        
        text_A.to_edge(LEFT, 0.5)

        self.play(Transform(matrix_A, text_A))
        self.wait(1)

# ---------------------------------------------------------------------

        matrix_D = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix}")

        text_D = TexMobject("D  +", tex_to_color_map={"D": YELLOW, "+": WHITE})
        text_D.next_to(text_A, RIGHT)

        # self.add(matrix_D)
        self.play(Write(matrix_D))
        self.wait(1)
        self.play(matrix_D.next_to, text_A, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_D, text_D))
        self.wait(1)

# ---------------------------------------------------------------------

        matrix_L = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix}")

        text_L = TexMobject("L  +", tex_to_color_map={"L": BLUE, "+": WHITE})
        text_L.next_to(text_D, RIGHT)

        # self.add(matrix_L)
        self.play(Write(matrix_L))
        self.wait(1)
        self.play(matrix_L.next_to, text_D, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_L, text_L))
        self.wait(1)

# ---------------------------------------------------------------------

        matrix_U = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix}")

        text_U = TexMobject("U ", tex_to_color_map={"U": GREEN, "+": WHITE})
        text_U.next_to(text_L, RIGHT)

        # self.add(matrix_U)
        self.play(Write(matrix_U))
        self.wait(1)
        self.play(matrix_U.next_to, text_L, RIGHT)
        self.wait(1)

        self.play(Transform(matrix_U, text_U))
        self.wait(1)

# ---------------------------------------------------------------------
        
        # self.add(texto1)

        # FadeOut(matrix_U)
        FadeOut(text_U)
        self.remove(matrix_U, text_U)
        self.wait(1/2)

        # FadeOut(matrix_L)
        FadeOut(text_L)
        self.remove(matrix_L, text_L)
        self.wait(1/2)

        FadeOut(matrix_D)
        FadeOut(text_D)
        self.remove(matrix_D, text_D)
        self.wait(1/2)

        # self.remove(matrix_A)

        # self.clear()
        # self.wait(0.5)

# ---------------------------------------------------------------------

        # matrix_A = TexMobject("\\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ a_{n1} & a_{n2} & \\cdots & a_{nn} \\\ \\end{bmatrix}")
        matrix_D = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix} + ")
        matrix_L = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix} + ")
        matrix_U = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix}")

        text_D = TexMobject("D", tex_to_color_map={"D": YELLOW})
        text_L = TexMobject("L", tex_to_color_map={"L": BLUE})
        text_U = TexMobject("U", tex_to_color_map={"U": GREEN})
        
        matrix_D.scale(0.8)
        matrix_L.scale(0.8)
        matrix_U.scale(0.8)

        matrix_D.next_to(matrix_A, RIGHT)
        matrix_L.next_to(matrix_D, RIGHT)
        matrix_U.next_to(matrix_L, RIGHT)

        matrix_D.set_color(YELLOW)
        matrix_L.set_color(BLUE)
        matrix_U.set_color(GREEN)


        # self.play(matrix_A.move_to, LEFT)
        self.play(text_D.next_to, matrix_A, RIGHT)
        # self.remove(text_D, matrix_D)
        self.play(Transform(text_D, matrix_D))

        # self.play(text_L.next_to, text_D, RIGHT)
        self.play(Transform(text_L, matrix_L))
        
        # self.play(text_U.next_to, text_L, RIGHT)
        self.play(Transform(text_U, matrix_U))
        
        
        # self.play(matrix_D.next_to, matrix_A)
        # self.play(matrix_U.next_to, matrix_D)
        # self.play(matrix_L.next_to, matrix_U)

        self.wait(1)
                
        # matrix_D = TexMobject("\\begin{bmatrix} d_{11} & 0 & \\cdots & 0 \\\ 0 & d_{22} & \\cdots & 0 \\\ \\vdots & \\vdots & \\ddots & \\vdots \\\ 0 & 0 & \\cdots & d_{nn} \\\ \\end{bmatrix}")
    