from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

# The class MUST call this class decorator at creation time
@magics_class
class ProletariatMagic(Magics):

    @line_magic
    def lmagic(self, line):
        "my line magic"
        print("Full access to the main IPython object:", self.shell)
        print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
        return line


    @cell_magic
    def girder(self, line, cell):

        import sys
        sys.path.append("/home/safuser/apps/girder")
        sys.path.append("/home/safuser/apps/proletariat")

        new_cell = 'import sys\n'
        new_cell += 'sys.path.append("/home/safuser/apps/girder")\n'
        new_cell += 'sys.path.append("/home/safuser/apps/proletariat")\n\n'
        new_cell += cell



        print(new_cell)

        from tasks import * 
        payload = {}
        payload['cell'] = new_cell
        task = excarb.delay(payload=payload)

        print('Celery task ', task.id)
        
        return None, None



    @line_cell_magic
    def lcmagic(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            return line
        else:
            print("Called as cell magic")
            return line, cell


# In order to actually use these magics, you must register them with a
# running IPython.  This code must be placed in a file that is loaded once
# IPython is up and running:
ip = get_ipython()
# You can register the class itself without instantiating it.  IPython will
# call the default constructor on it.
ip.register_magics(ProletariatMagic)