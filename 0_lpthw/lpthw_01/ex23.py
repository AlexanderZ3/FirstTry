# ord() 函数用于返回字符的ASCII码
# chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制


import sys
script, encoding, error = sys.argv

def main(language_file,encoding,errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return(main(language_file, encoding, errors))

def print_line(line, encoding, error):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes,'<==>', cooked_string)

languages = open("languages.txt",encoding = 'utf-8')
main (languages, emcoding, error)
