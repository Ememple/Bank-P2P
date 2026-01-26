
class ProtocolHandler:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def handle(self, line: str):
        line = line.strip()
        if not line:
            return "ERROR, EMPTY_COMMAND"

        parts = line.split()
        command_code = parts[0].upper()
        args = parts[1:]

        try:
            response = self.dispatcher.dispatch(command_code, args)
        except KeyError:
            response = "ERROR, UNKNOWN_COMMAND"
        except Exception as e:
            response = f"ERR {e}"
        return response
