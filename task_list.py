def create_task_list():
    """
    Creates task list using closure. Its create one list of tasks with two properties (description, is_complete) and some functions for manipulate it.

    :return: Dictionary with closure functions
    """

    tasks = []

    def add_task(description: str):
        """
        Add new uncompleted task
        :param description: the task text
        """
        if len(description.strip()) < 0:
            raise Exception("Task must contains one char at least.")

        tasks.append({"description": description, "is_complete": False})

    def set_complete(description: str):
        for t in tasks:
            if t["description"] == description:
                t["is_complete"] = True
                break

    def get_uncompleted() -> list:
        """
        Select uncompleted tasks amd return it
        :return: list of descriptions in str
        """
        uncompleted = []
        for t in tasks:
            if not t["is_complete"]:
                uncompleted.append(t["description"])
        return uncompleted

    def get_completed() -> list:
        """
        Select completed tasks amd return it
        :return: list of descriptions in str
        """
        completed = []
        for t in tasks:
            if t["is_complete"]:
                completed.append(t["description"])
        return completed

    def chytry_vypis() -> list:
        """
        Select completed tasks amd return it
        :return: list of descriptions in str
        """
        list = []
        for t in tasks:
            if t["is_complete"]:
                list.append("[ ]" + t["description"])
            else:
                list.append("[X]" + t["description"])
        return list

    return {"add_task": add_task, "get_uncompleted": get_uncompleted, "get_completed": get_completed, "set_complete": set_complete, "chytry_vypis": chytry_vypis}


try:
    peter_todo = create_task_list()
    peter_todo["add_task"]("Vynest smeti")
    peter_todo["add_task"]("Uklidit si pokojicek")

    print(peter_todo["get_uncompleted"]())
    peter_todo["set_complete"]("Uklidit si pokojicek")
    print(peter_todo["get_uncompleted"]())
    print(peter_todo["get_completed"]())
    print(peter_todo["chytry_vypis"]())
    peter_todo["set_complete"]("Vynest smeti")
    print(peter_todo["chytry_vypis"]())
except Exception as e:
    print(e)

