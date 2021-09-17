from manim import *
import numpy

class HMS1(Scene):
  def construct(self):
    self.problem1()
    self.problem2()
    self.problem3()
    self.problem4()
    self.problem5()

  def problem1(self):
    introduction = MathTex(r"1.\ Consider\ the\ function\ f(x) = \frac{x - 3}{x^{2} - 9}").to_edge(UP, buff = .1)
    instruction1 = MathTex(r"1.\ Complete\ the\ table\ and\ guess").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 1.5)
    instruction2 = MathTex(r"a\ value\ for\ \lim_{x \rightarrow 3 }\frac{x - 3}{x^{2} - 9}").next_to(instruction1, DOWN, buff = .25)

    axes = Axes(x_range = [0, 5], y_range = [0, .5, .1], x_length = 5, y_length = 3, tips = False).add_coordinates()
    axes_labels = axes.get_axis_labels(MathTex(r"x"), MathTex(r"f(x)"))
    graph = axes.get_graph(lambda x: (x - 3) / (x**2 - 9), x_range = [0.0001  , 5])

    graph_points = VGroup()
    graph_verticies = [(2, 1/5), (2.9, 1/5.9), (2.99, 1/5.99), (2.999, 1/5.999),
    (3.001, 1/6.001), (3.01, 1/6.01), (3.1, 1/6.1), (4, 1/7)]
    for i in range(8):
      d = Dot(axes.coords_to_point(graph_verticies[i][0], graph_verticies[i][1]), color = BLUE, z_index = 1)
      d.set_fill(opacity = 0)
      graph_points.add(d)

    left_secant_line = axes.get_secant_slope_group(x = 2, graph = graph, dx = .0001, secant_line_length = 4, secant_line_color = TEAL)[2].set_opacity(0)
    right_secant_line = axes.get_secant_slope_group(x = 4, graph = graph, dx = .0001, secant_line_length = 4, secant_line_color = TEAL)[2].set_opacity(0)
    secant_lines = VGroup(left_secant_line, right_secant_line)

    limit_dot = graph_points[3].copy()

    graph_group = VGroup(axes, axes_labels, graph, graph_points, secant_lines, limit_dot)

    table = MobjectTable([[MathTex(r"x"), Tex("2"), Tex("2.9"), Tex("2.99"), Tex("2.999"), Tex("3"), Tex("3.001"), Tex("3.01"), Tex("3.1"), Tex("4")],
    [MathTex(r"f(x) = \frac{x - 3}{x^{2} - 9}"), MathTex(r"\frac{1}{5}"), MathTex(""), Tex(""), Tex(""), Tex("und."), Tex(""), Tex(""), Tex(""), MathTex(r"\frac{1}{7}")]],
    include_outer_lines = True, line_config = {"stroke_width": 1}).scale(.4).to_edge(LEFT, buff = .25).to_edge(DOWN, buff = 3)

    in_values = Matrix([[2, 4], [2.9, 3.1], [2.99, 3.01], [2.999, 3.001]],
    element_alignment_corner = [0, 0, 0], h_buff = 1.5).scale(.75).to_edge(DOWN + LEFT, buff = .25)
    in_arrow = Arrow(LEFT, RIGHT, tip_length = 0.25).next_to(in_values, RIGHT, buff = 0).scale(.5)
    equation = MathTex(r"\frac{x - 3}{x^{2} - 9}").next_to(in_arrow, RIGHT, buff = .25)
    out_arrow = Arrow(LEFT, RIGHT, tip_length = 0.25).next_to(equation, RIGHT, buff = 0).scale(.5)
    out_values = Matrix([["1/5", "1/7"], ["1/5.9", "1/6.1"], ["1/5.99", "1/6.01"], ["1/5.999", "1/6.001"]],
    element_alignment_corner = [0, 0, 0], h_buff = 2).scale(.75).next_to(out_arrow, RIGHT, buff = .25)
    out_values.set_row_colors(WHITE, BLUE, BLUE, BLUE)

    table_answers = VGroup()
    target_index_order = [0, 5, 1, 4, 2, 3]
    for i in range(6): table_answers.add(out_values.get_entries()[i + 2])
    for i in range(6): table_answers[i].target = target_index_order[i]

    table_targets = VGroup()
    answer_values = [5.9, 5.99, 5.999, 6.001, 6.01, 6.1]
    cell_index_order = [3, 4, 5, 7, 8, 9]
    for i in range(6):
      table_targets.add(MathTex(r"\frac{1}{" + str(answer_values[i]) + r"}",
      color = BLUE).scale(.4).move_to(table.get_cell((2, cell_index_order[i]))))

    ploting_lines = VGroup()
    table_indicies = [2, 3, 4, 5, 7, 8, 9, 10]
    
    solution = MathTex(r"\lim_{x \rightarrow 3 }\frac{x - 3}{x^{2} - 9} = \frac{1}{6}", color = BLUE).to_edge(RIGHT, buff = .75)
    solution_box = SurroundingRectangle(solution, color = WHITE, buff = .25)

    def run_script():
      self.wait(2)
      self.play(Write(introduction))
      self.wait(2)
      self.play(FadeIn(axes), Write(axes_labels))
      self.wait(1)
      self.play(Create(graph))
      self.wait(4)
      self.play(ScaleInPlace(graph_group, .75))
      self.play(FadeOut(introduction), graph_group.animate.to_edge(UP + LEFT, buff = .25))
      self.wait(1)
      self.play(FadeIn(table, run_time = 2))
      self.wait(1)
      self.play(Write(instruction1), Write(instruction2))
      self.wait(4)
      self.play(FadeIn(in_values))
      self.wait(2)
      self.play(FadeIn(in_arrow, equation))
      self.wait(2)
      self.play(FadeIn(out_arrow, out_values))
      self.wait(2)
      self.play(LaggedStartMap(TransformFromCopy, table_answers, lambda t: (t, table_targets[t.target]), lag_ratio = .25))
      self.wait(2)
      for i in range(8): ploting_lines.add(Line(table.get_cell((2, table_indicies[i])).get_center(), graph_points[i].get_center(), color = BLUE))
      self.play(LaggedStartMap(Create, ploting_lines, lag_ratio = .05))
      self.play(graph_points.animate.set_fill(opacity = 1))
      self.play(LaggedStartMap(Uncreate, ploting_lines, lag_ratio = .05))
      self.wait(2)
      self.play(left_secant_line.animate.set_opacity(1), right_secant_line.animate.set_opacity(1), run_time = 2)
      self.wait(1)
      self.play(Transform(secant_lines, axes.get_secant_slope_group(x = 2.999, graph = graph, dx = .0001, secant_line_length = 4,
      secant_line_color = TEAL)[2], run_time = 4), FadeOut(graph_points), FadeIn(limit_dot.set_fill(opacity = 1)))
      self.wait(2)
      self.play(Write(solution), Create(solution_box))
      self.wait(4)
      self.play(FadeOut(table, table_targets, graph_group, limit_dot, ploting_lines, instruction1, instruction2,
      in_values, in_arrow, equation, out_arrow, out_values, solution, solution_box))
      self.wait(1)

    run_script()

  def problem2(self):
    mq = MathTex(r"2.\ Consider\ the\ function").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)
    qa = MathTex(r"2a.\ What\ is \lim_{x\rightarrow 1}f(x)?").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)
    qb = MathTex(r"2b.\ What\ is\ f(1)?").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)
    qc = MathTex(r"2c.\ What\ is \lim_{x\rightarrow 2^{-}}f(x)?").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)
    qd = MathTex(r"2d.\ What\ is \lim_{x\rightarrow 2^{+}}f(x)?").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)
    qe = MathTex(r"2e.\ Does \lim_{x\rightarrow 2}f(x)\ exist?").to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2.5)

    axes = Axes(x_range = [-3, 3], y_range = [-3, 3], x_length = 4, y_length = 4, tips = False).to_edge(UP + LEFT, buff = .25)

    graph1 = axes.get_graph(lambda x : x**2 - 2, x_range = [-3, 2])
    graph2 = axes.get_graph(lambda x : x - 3, x_range = [2, 3])

    filled_points = VGroup(Dot(axes.coords_to_point(1, 2)), Dot(axes.coords_to_point(2, 3)))
    open_points = VGroup()
    open_point_coords = [(1, -1), (2, 2), (2, -1)]
    for i in range(3):
      c = Circle(.05, color = WHITE).move_to(axes.coords_to_point(open_point_coords[i][0], open_point_coords[i][1]))
      c.set_fill(color = BLACK, opacity = 1)
      open_points.add(c)

    qa_arrows = VGroup()
    qa_arrow_coords = [(axes.coords_to_point(1.55, -.2), axes.coords_to_point(1.35, -.7)),
                       (axes.coords_to_point(.85, -1.75), axes.coords_to_point(1.1, -1.25)),
                       (axes.coords_to_point(.75, -1), axes.coords_to_point(.3, -1))]
    for i in range(len(qa_arrow_coords)): qa_arrows.add(Arrow(qa_arrow_coords[i][0], qa_arrow_coords[i][1], color = ORANGE))
    qa_answer = MathTex(r"-1", color = ORANGE).next_to(qa, DOWN, buff = 1.5)

    qb_arrow = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1, 2), color = ORANGE)
    qb_answer = MathTex(r"2", color = ORANGE).next_to(qb, DOWN, buff = 1.5)

    qc_arrow = Arrow(axes.coords_to_point(1.2, .1), axes.coords_to_point(1.7, 1.9), color = ORANGE)
    qc_answer = MathTex(r"2", color = ORANGE).next_to(qc, DOWN, buff = 1.5)

    qd_arrow = Arrow(axes.coords_to_point(3.2, -.3), axes.coords_to_point(2.3, -1.1), color = ORANGE)
    qd_answer = MathTex(r"-1", color = ORANGE).next_to(qd, DOWN, buff = 1.5)

    qe_answer = MathTex(r"No,\ because\ \lim_{x\rightarrow 2^{-}}f(x) \neq \lim_{x\rightarrow 2^{+}}f(x)", color = ORANGE).next_to(qe, DOWN, buff = 1.5)

    def run_script():
      self.play(FadeIn(axes))
      self.play(Write(mq))
      self.wait(1)
      self.play(Create(graph1), Create(graph2), Create(filled_points), Create(open_points))
      self.wait(1)
      self.play(FadeOut(mq), Write(qa))
      self.wait(1)
      self.play(Create(qa_arrows[0]), Create(qa_arrows[1]))
      self.wait(1)
      self.play(TransformFromCopy(qa_arrows[0:2], qa_arrows[2]))
      self.wait(1)
      self.play(TransformFromCopy(qa_arrows[2], qa_answer))
      self.wait(2)
      self.play(FadeOut(qa, qa_answer, qa_arrows), Write(qb))
      self.wait(1)
      self.play(Create(qb_arrow))
      self.wait(1)
      self.play(TransformFromCopy(qb_arrow, qb_answer))
      self.wait(2)
      self.play(FadeOut(qb, qb_arrow, qb_answer), Write(qc))
      self.wait(1)
      self.play(Create(qc_arrow))
      self.wait(1)
      self.play(TransformFromCopy(qc_arrow, qc_answer))
      self.wait(2)
      self.play(FadeOut(qc, qc_answer), Write(qd))
      self.wait(1)
      self.play(Create(qd_arrow))
      self.wait(1)
      self.play(TransformFromCopy(qd_arrow, qd_answer))
      self.wait(2)
      self.play(FadeOut(qd, qd_answer), Write(qe))
      self.wait(1)
      self.play(FadeOut(qc_arrow, qd_arrow), Write(qe_answer))
      self.wait(2)
      self.play(FadeOut(qe, qe_answer, axes, graph1, graph2, filled_points, open_points))
      self.wait(1)

    run_script()

  def problem3(self):
    def increment_set(places):
      x.add_updater(lambda x : x.become(Tex(str(round(tracker.get_value(), places)), z_index = 1).move_to(table.get_cell((2, 1)))))
      fx.add_updater(lambda fx : fx.become(Tex(str(round((tracker.get_value() + 5) / (tracker.get_value() - 2), 1)),
      z_index = 1).move_to(table.get_cell((2, 2)))))
      self.play(tracker.animate.set_value(float("1." + "9" * places)), run_time = 3)
      x.clear_updaters()
      fx.clear_updaters()

    question = MathTex(r"3.\ Evaluate\ \lim_{x\rightarrow 2^{-}}\frac{x + 5}{x - 2}").to_edge(UP, buff = .5)

    table = MobjectTable([[MathTex(r"x"), MathTex(r"f(x)")], [MathTex(r"FFFFFF", color = BLACK),
    MathTex(r"FFFFFF", color = BLACK)]], include_outer_lines = True).next_to(question, DOWN, buff = 1)

    x = Tex("1.5", z_index = 1).move_to(table.get_cell((2, 1)))
    fx = Tex("-13.0", z_index = 1).move_to(table.get_cell((2, 2)))

    tracker = ValueTracker(1.5)

    solution = MathTex(r"\lim_{x\rightarrow 2^{-}}\frac{x + 5}{x - 2} = -\infty").next_to(table, DOWN, buff = 1)

    def run_script():
      self.play(Write(question))
      self.wait(1)
      self.play(FadeIn(table))
      self.play(Write(x), Write(fx))
      self.wait(1)
      increment_set(1)
      increment_set(2)
      increment_set(3)
      increment_set(4)
      self.wait(2)
      self.play(Write(solution))
      self.wait(3)
      self.play(FadeOut(question, table, x, fx, solution))
      self.wait(1)

    run_script()

  def problem4(self):
    question = MathTex(r"4.\ Suppose\ that\ \lim_{x\rightarrow 3}f(x) = 7\ and\ \lim_{x\rightarrow 3}g(x) = -4.\ What\
    is\ \lim_{x\rightarrow 3}[5f(x) - 3g(x)]?", font_size = 30).to_edge(UP + LEFT, buff = .5)
    laws = MathTex(r"Relevant\ Limit\ Laws\ ", font_size = 30).next_to(question, DOWN, buff = .5)
    colon = MathTex(r":").next_to(laws, RIGHT, buff = .25)
    law1 = MathTex(r"\lim_{x\rightarrow a}[f(x) - g(x)] = \lim_{x\rightarrow a}f(x) - \lim_{x\rightarrow a}g(x)", font_size = 30).next_to(colon, DOWN, buff = .5)
    law2 = MathTex(r"\lim_{x\rightarrow a}[cf(x)] = c\lim_{x\rightarrow c}f(x)", font_size = 30).next_to(law1, DOWN, buff = .5)
    solution1 = MathTex(r"\lim_{x\rightarrow 3}[5f(x) - 3g(x)] = 5\lim_{x\rightarrow 5}f(x) - 3\lim_{x\rightarrow 3}g(x)",
    font_size = 30, color = BLUE).to_edge(LEFT, buff = 2).to_edge(DOWN, buff = 2.5)
    solution2 = MathTex(r"5\lim_{x\rightarrow 5}f(x) - 3\lim_{x\rightarrow 3}g(x) =\ \ \ ", r"5\lim_{x\rightarrow 5}f(x) + 12",
    font_size = 30, color = BLUE).next_to(solution1, DOWN, buff = .75)
    sol_box = SurroundingRectangle(solution2[1], color = YELLOW, buff = .15)

    def run_script():
      self.play(Write(question))
      self.wait(1)
      self.play(Write(laws), Write(colon))
      self.wait(3)
      self.play(Write(law1), Write(law2))
      self.wait(1)
      self.play(Write(solution1))
      self.wait(2)
      self.play(Write(solution2))
      self.wait(1)
      self.play(Create(sol_box))
      self.wait(3)
      self.play(FadeOut(question, laws, colon, law1, law2, solution1, solution2, sol_box))
      self.wait(1)

    run_script()

  def problem5(self):
    qa = MathTex(r"5a.\ Evaluate\ \lim_{x\rightarrow -3}\frac{x^{2} - 5x - 24}{x + 3}", font_size = 26).to_edge(UP + LEFT, buff = .25)
    qb = MathTex(r"5b.\ Evaluate\ \lim_{h\rightarrow 0}\frac{\sqrt{9 + h} - 3}{h}", font_size = 26).to_edge(LEFT, buff = .25)

    tablea = MobjectTable([[MathTex(r"x"), Tex("-4"), Tex("-3.1"), Tex("-3.01"), Tex("-3.001"), Tex("-3"), Tex("-2.999"), Tex("-2.99"), Tex("-2.9"), Tex("-2")],
    [MathTex(r"\frac{x^{2} - 5x - 24}{x + 3}"), Tex("-10"), Tex("-10.9"), Tex("-10.99"), Tex("-10.999"), Tex("und."),
    Tex("-11.001"), Tex("-11.01"), Tex("-11.1"), Tex("-12")]],
    include_outer_lines = True, line_config = {"stroke_width": 1}).scale(.4).next_to(qa, DOWN, buff = .25).to_edge(LEFT, buff = .25)

    tableb = MobjectTable([[MathTex(r"x"), Tex("-1"), Tex("-0.1"), Tex("-0.01"), Tex("-0.001"), Tex("0"), Tex("0.001"), Tex("0.01"), Tex("0.1"), Tex("1")],
    [MathTex(r"\frac{\sqrt{9 + h} - 3}{h}"), Tex("0.17"), Tex("0.167"), Tex("0.166"), Tex("0.1666"), Tex("und."),
    Tex("0.1666"), Tex("0.167"), Tex("0.166"), Tex("0.16")]],
    include_outer_lines = True, line_config = {"stroke_width": 1}).scale(.4).next_to(qb, DOWN, buff = .25).to_edge(LEFT, buff = .25)

    solutiona = MathTex(r"\lim_{x\rightarrow -3}\frac{x^{2} - 5x - 24}{x + 3} = -11", font_size = 26, color = BLUE).next_to(tablea, RIGHT, buff = .25)
    solutionb = MathTex(r"\lim_{h\rightarrow 0}\frac{\sqrt{9 + h} - 3}{h} = \frac{1}{6}", font_size = 32, color = BLUE).next_to(tableb, RIGHT, buff = .25)

    def run_script():
      self.play(FadeIn(qa, qb))
      self.wait(2)
      self.play(FadeIn(tablea))
      self.wait(1)
      self.play(Write(solutiona))
      self.wait(1)
      self.play(FadeIn(tableb))
      self.wait(1)
      self.play(Write(solutionb))
      self.wait(4)
  
    run_script()
