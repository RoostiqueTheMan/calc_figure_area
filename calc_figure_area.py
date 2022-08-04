from typing import List, Tuple


def calc_figure_area(points: List[Tuple[float]]) -> float:
    if len(points) <= 1:
        raise ValueError(
            'Для расчета площади необходимо больше одной координаты'
        )

    total = 0.0

    for i in range(len(points)):

        if len(points[i]) != 2:
            raise ValueError(
                'Для расчета площади необходимо '
                'два значения в одной координате'
            )

        if i == len(points) - 1:
            break
        a = abs(points[i][1])
        b = abs(points[i+1][1])
        h = points[i+1][0] - points[i][0]
        s = h * (a + b) / 2
        total += s
    return total
