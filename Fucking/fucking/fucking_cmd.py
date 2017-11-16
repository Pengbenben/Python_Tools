import getopt
import socket
import sys

help_info = {
    "fucking word": "Get the pronunciation and the definition of the `word`",
    "fucking -f|--force word": "Force to fetch data from the Internet",
    "fucking -u|--update word": "Update the local cache of the `word`(Has the same effect of the -f)",
    "fucking -p|--ping": "Ping the target to check the connection",
    "fucking -h|--help": "Print this help information"
}
force = 0
update = 0


def get_cmd():
    return {
        "force": force,
        "update": update
    }


def usage():
    m = max(map(len, help_info.keys()))
    print("Usage:")
    for k in help_info:
        print("\t", k.ljust(m), "\t", help_info[k])


def ping():
    try:
        soc = socket.socket()
        res = soc.connect(("fanyi.baidu.com", 80))
    except Exception:
        print("Fail!")
    finally:
        soc.close()
    print("Success!")


def parse_cmd():
    global force
    global update
    opts, args = getopt.getopt(sys.argv[1:], "fuph", ["help", "update", "force", "ping"])

    for val in opts:
        val = val[0]
        if val in ["-h", "--help"]:
            usage()
            exit(0)
        elif val in ["-p", "--ping"]:
            ping()
            exit(0)
        elif val in ["-f", "--force"]:
            force = 1
        elif val in ["-u", "--update"]:
            update = 1

    try:
        word = args[0]
    except IndexError:
        print("Seems like you lose your word?")
        exit(-2)

    return word
