# 合ってそうだけどPyPyでもCPythonでもTLE
# PyPyのほうがまだまし
# セグメント木はPythonだと厳しいのかも…
import sys


class Value:
    def __init__(self, i: int, value: int) -> None:
        self.i = i
        self.value = value

    def __lt__(self, other):
        if not isinstance(other, Value):
            raise
        return self.value < other.value


class Cell:
    def __init__(self, start_index: int, end_index: int) -> None:
        self.min_value = Value(0, 0)
        self.max_value = Value(0, 0)
        self.start_index = start_index
        self.end_index = end_index
        self.lower_left_cell: Cell | None = None
        self.lower_right_cell: Cell | None = None
        self.upper_cell: Cell | None = None

    def __repr__(self) -> str:
        return str((self.start_index, self.end_index))


class SegmentTree:
    def __init__(self, init_list: list[Value]):
        self.length = len(init_list)
        self.cells: list[Cell] = []
        self.size = 1
        pow_num = 0
        while True:
            if 2**pow_num < self.length:
                pow_num += 1
            else:
                cells_length = 2**pow_num
                break
        while self.size < cells_length * 2:
            cells: list[Cell] = []
            for i in range(self.size):
                start_index = (cells_length // self.size) * i
                end_index = (cells_length // self.size) * (i + 1) - 1
                cells.append(Cell(start_index, end_index))
            self.cells.extend(cells)
            self.size *= 2
        self.size //= 2
        for i, cell in enumerate(self.cells):
            if i < self.size - 1:
                cell.lower_left_cell = self.cells[i * 2 + 1]
                cell.lower_right_cell = self.cells[i * 2 + 2]
            if i > 0:
                cell.upper_cell = self.cells[(i - 1) // 2]

        for i in range(self.length):
            self.update(i, init_list[i])

    def __repr__(self):
        return str(self.cells)

    def find_cell(self, index: int):
        return self.cells[index + self.size - 1]

    def value(self, index):
        return self.find_cell(index).min_value

    def update(self, index: int, value: Value):
        if index >= self.length:
            raise
        cell = self.find_cell(index)
        cell.max_value = value
        cell.min_value = value
        while cell.upper_cell is not None:
            cell = cell.upper_cell
            if cell.lower_left_cell is None or cell.lower_right_cell is None:
                raise
            cell.max_value = max(
                cell.lower_left_cell.max_value, cell.lower_right_cell.max_value
            )
            cell.min_value = min(
                cell.lower_left_cell.min_value, cell.lower_right_cell.min_value
            )

    def max_value(self, start_index: int, end_index: int):
        return self.query(start_index, end_index, self.cells[0], "max")

    def min_value(self, start_index: int, end_index: int):
        return self.query(start_index, end_index, self.cells[0], "min")

    def query(self, start_index: int, end_index: int, cell: Cell, func: str) -> Value:
        if start_index < 0 or self.length <= end_index:
            raise

        match func:
            case "max":
                default_value = Value(0, -sys.maxsize)
            case "min":
                default_value = Value(0, sys.maxsize)
            case _:
                raise

        if end_index < cell.start_index or cell.end_index < start_index:
            return default_value

        if cell.start_index == start_index and end_index == cell.end_index:
            match func:
                case "max":
                    return cell.max_value
                case "min":
                    return cell.min_value

        # 左下
        if (
            cell.lower_left_cell is not None
            and start_index <= cell.lower_left_cell.end_index
        ):
            lower_left = self.query(
                start_index,
                min(cell.lower_left_cell.end_index, end_index),
                cell.lower_left_cell,
                func,
            )
        else:
            lower_left = default_value

        # 右下
        if (
            cell.lower_right_cell is not None
            and cell.lower_right_cell.start_index <= end_index
        ):
            lower_right = self.query(
                max(start_index, cell.lower_right_cell.start_index),
                end_index,
                cell.lower_right_cell,
                func,
            )
        else:
            lower_right = default_value

        match func:
            case "max":
                return max(lower_left, lower_right)
            case "min":
                return min(lower_left, lower_right)


N, M = map(int, input().split())
P = list(map(int, input().split()))

values: list[Value] = []
for i in range(N):
    p = P[i]
    value = Value(i, p)
    values.append(value)

tree = SegmentTree(values)

for _ in range(M):
    left, right = map(int, input().split())
    left -= 1
    right -= 1

    max_value = tree.max_value(left, right)
    min_value = tree.min_value(left, right)

    tree.update(min_value.i, Value(min_value.i, max_value.value))
    tree.update(max_value.i, Value(max_value.i, min_value.value))

answers: list[int] = []
for i in range(N):
    answers.append(tree.find_cell(i).min_value.value)
print(*answers)
