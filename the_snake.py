from random import choice, randint

import pygame

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет мусора
TRASH_COLOR = (85, 107, 47)

# Цвет камня
STONE_COLOR = (105, 105, 105)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject():
    """
    Класс GameObject — это базовый класс, от которого наследуются другие
    игровые объекты. Он содержит общие атрибуты игровых объектов
    """

    def __init__(self) -> None:
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self) -> None:
        """Абстрактный метод для переопределения в дочерних классах."""
        pass


class Apple(GameObject):
    """
    Apple — класс, унаследованный от GameObject,
    описывающий яблоко и действия с ним
    """

    def __init__(self) -> None:
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self) -> None:
        """Метод устанавливает случайное положение яблока на игровом поле"""
        self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self) -> None:
        """Метод отрисовывает яблоко на игровой поверхности"""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Trash(Apple):
    """
    Trash — класс, унаследованный от Apple,
    описывающий мусор, который змейке есть нельзя.
    При поедании длина змейки уменьшается.
    """

    def __init__(self) -> None:
        super().__init__()
        self.body_color = TRASH_COLOR


class Stone(Apple):
    """
    Stone — класс, унаследованный от Apple,
    описывающий камни, которые змейке есть нельзя.
    При столкновении змейка возвращается к исходному состоянию
    """

    def __init__(self) -> None:
        super().__init__()
        self.body_color = STONE_COLOR


class Snake(GameObject):
    """
    Snake — класс, унаследованный от GameObject, описывающий змейку
    и её поведение. Этот класс управляет её движением, отрисовкой,
    а также обрабатывает действия пользователя.
    """

    def __init__(self) -> None:
        super().__init__()
        self.length = 1
        self.positions = [(20, 240), (40, 240)]  # [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.last = None

    def update_direction(self) -> None:
        """Метод обновляющий направление змейки"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def draw(self) -> None:
        """Метод отрисовывающий змейку"""
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.get_head_position(),
                                (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            self.erase_last(self.last)

    def erase_last(self, last) -> None:
        """Метод закрашивающий "следы" змейки"""
        last_rect = pygame.Rect(last, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self) -> tuple:
        """Метод, возвращающий положение головы змейки"""
        return self.positions[0]

    def reset(self) -> None:
        """
        Метод, сбрасывающий змейку в начальное состояние
        после столкновения с собой.
        """
        self.length = 1
        self.last = None
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        screen.fill(BOARD_BACKGROUND_COLOR)
        # self.move()

    def move(self) -> None:
        """Метод обновляет позицию змейки."""
        head = self.get_head_position()
        dir = self.direction
        new_head_prev = [head[i] + dir[i] * GRID_SIZE for i in range(2)]
        x, y = new_head_prev[0], new_head_prev[1]
        new_head = (x % SCREEN_WIDTH, y % SCREEN_HEIGHT)
        if new_head in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.last = self.positions.pop()

    def is_collide(self, sprite: Apple) -> bool:
        """Метод проверяет столкновение змейки с другим спрайтом"""
        if self.get_head_position() == sprite.position:
            return True
        return False


def handle_keys(game_object: Snake) -> None:
    """Функция обработки действий пользователя"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            if event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            if event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            if event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main() -> None:
    """
    Функция, запускаемая игру.
    В ней прописывается логика игры и создаются экземпляры классов
    """
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    trash = Trash()
    stone = Stone()
    snake = Snake()
    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        if snake.is_collide(apple):
            snake.length += 1
            apple.randomize_position()
            if (apple.position == trash.position
                    or apple.position == stone.position):
                apple.randomize_position()
        if snake.is_collide(stone):
            snake.reset()
            stone.randomize_position()
            if (stone.position == apple.position
                    or stone.position == trash.position):
                stone.randomize_position()
        if snake.is_collide(trash):
            snake.length -= 1
            snake.erase_last(snake.positions.pop())
            if snake.length == 0:
                snake.reset()
            trash.randomize_position()
            if (trash.position == apple.position
                    or trash.position == stone.position):
                trash.randomize_position()
        snake.draw()
        apple.draw()
        stone.draw()
        trash.draw()
        clock.tick(5)
        pygame.display.update()


if __name__ == '__main__':
    main()
