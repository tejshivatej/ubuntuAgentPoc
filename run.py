"""

It connects to remote windows device and execute commands 
remotely from local host

"""



import winrm

class RemoteAgent:

    def __init__(self, hostname, username, password) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect_to_remote_host(self):

        """
        
        It establishes connection with remote device

        """

        
        session = winrm.Session(self.hostname, auth = (self.username, self.password))
        return session

   
    def execute_commands(self,session):

        """
        
        It executes commands in remote device and prints response 
        on local device

        """

        print("ipconfig\n")
        output = session.run_cmd('ipconfig', ['/all'])
        print(output.std_out)
        print("\n")
        print("hostname\n")
        output = session.run_cmd('hostname')
        print(output.std_out)

    

if __name__ == "__main__":

    connection = RemoteAgent('192.168.1.105','Administrator','India@123')
    session = connection.connect_to_remote_host()
    connection.execute_commands(session)
    