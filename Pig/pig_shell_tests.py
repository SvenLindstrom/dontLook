import cmd


class Shell (cmd.Cmd):

    def __init__(self):
        super().__init__()

    def do_start(self, _):
        print("test")

    def do_test2 (self, _):
        class mini_shell(cmd.Cmd):
            def __init__(self):
                super().__init__()
            def do_test(self, _):
                print('i am in')
            def do_q(self, _):
                return True
        mini_shell().cmdloop()
        print('mini cmd over')

    def do_exit(self, _):
        return True
    
    def do_quit(self, arg):
        return self.do_exit(arg) 


if __name__ == '__main__':
    me = Shell()
    me.prompt = 'test '
    me.cmdloop()
    print('test2')

