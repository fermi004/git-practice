"""一个小型命令行待办清单，用于 Git 练习。"""


def collect_tasks() -> list[str]:
    """读取用户输入，空行结束。"""
    tasks: list[str] = []
    print("输入待办事项；直接按 Enter 结束。")

    while True:
        try:
            task = input(f"任务 {len(tasks) + 1}: ").strip()
        except EOFError:
            return tasks
        if not task:
            return tasks
        tasks.append(task)


def show_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("还没有待办事项。")
        return

    print("\n今日待办：")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


if __name__ == "__main__":
    show_tasks(collect_tasks())
