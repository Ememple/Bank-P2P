import datetime
import os


class ActionLogger:
    def __init__(self):
        self.filepath = "../res/actions.log"

        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def log(self, action: str, args: list[str]):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args_str = " ".join(str(x) for x in args)
        log_message = f"[{timestamp}] {action.upper()} {args_str}"

        try:
            with open(self.filepath, "a", encoding="utf-8") as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(f"Failed to write to log file: {e}")