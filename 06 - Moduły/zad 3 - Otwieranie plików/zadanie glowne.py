import safe_open_save as sos

def main():
    content = sos.open_file()
    content = content + 'lalalalalala2'
    sos.safe_save_file('pan_tadeusz.txt', content)
main()
