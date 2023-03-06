import os
APPDATA=os.getenv('LOCALAPPDATA')

class check:
    def __init__():
        try:
            with open(f'{APPDATA}//f35ee3fc-b929-11ed-afa1-0242ac120002.f97a0b4a-b929-11ed-afa1-0242ac120002.dll', 'r') as f:
                return 'except'
        except:
            # Continue #
            return 'pass'