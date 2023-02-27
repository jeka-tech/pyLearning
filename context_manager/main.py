from contextlib import contextmanager
class Resourse:
    def __init__(self):
        self.oppened = True

    def open(self, *args):
        print(f'Resorse was opened with arguments {args}.')
        self.oppened = True

    def close(self):
        print('Resorse was closed.')
        self.oppened = False

    def __del__(self):
        if self.oppened:
            print('Memory leak detected. Resourse was not closed.')

    def action(self):
        print('Do something with resource.')

@contextmanager
def open_resource(*args):
    example = None
    try:
        example = Resourse()
        example.open(*args)
        yield example
    except Exception:
        raise
    finally:
        if example:
            example.close()

class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.example = None
    def __enter__(self):
        self.example = Resourse()
        self.example.open(*self.args)
        return self.example
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.example:
            self.example.close()
        return True #Эта строка глотает исключения. Это не рекомендуется.

if __name__ == "__main__":
    with ResourceWorker(1, 2, 4) as result:
        result.action()
        raise ValueError('Stop')
