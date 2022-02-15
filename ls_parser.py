# you have string of output from the linux ls command.
# parse the ls string below into the parts list below avoiding extraneous
# info:
#
# Relevant Parts
# permissions
# links_to_file
# owner_name
# owner_group
# file_size
# last_mod_date
# last_mod_time
# last_mod_utc_offset
# file_name

# the "main" function is provided to get you started.

def parse():
    columns=[]
    names=[ "permissions", "links_to_file", "owner_name", "owner_group", "file_size", "last_mod_date", "last_mod_time", "last_mod_utc_offset","file_name"]
    ls_string = '/home/pocuser:\n' \
                'total 8\n' \
                'drwxrwxr-x. 2 pocuser pocuser    4096 2016-05-02 20:24:34.174000921 -0700 lets.test.top.command\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160499\n' \
                'drwxrwxr-x. 6 pocuser pocuser    4096 2016-04-18 09:33:28.100000773 -0700 poc\n' \
                '/home/bob:\n' \
                'total 15\n' \
                'drwxrwxr-x. 2 pocuser pocuser    4096 2016-05-02 20:24:34.174000921 -0700 lets.test.top.command\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160421\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160422\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160423\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160424\n' \
                '-rw-rw-r--. 1 pocuser pocuser  384300 2016-04-20 16:30:02.681000809 -0700 top.output.20160425\n' \
                'drwxrwxr-x. 6 pocuser pocuser    4096 2016-04-18 09:33:28.100000773 -0700 abc'

    lines=ls_string.split('\n')
    #print(lines)
    for i in lines:
        if len(i.split()) == 9:
            for j in range(9):
                print(names[j],":",i.split()[j])
                

    

    #print(columns)
    #print(ls_string)


if __name__ == '__main__':
    parse()