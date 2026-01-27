
class ProtocolHandler:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def handle(self, line: str):
        line = line.strip()
        if not line:
            return "ER EMPTY COMMAND"

        parts = line.split()
        command_code = parts[0].upper()
        args = parts[1:]

        try:
            response = self.dispatcher.dispatch(command_code, args)
        except KeyError:
            response = "ER UNKNOWN_COMMAND"
        except Exception as e:
            response = f"ER {e}"
        return response
