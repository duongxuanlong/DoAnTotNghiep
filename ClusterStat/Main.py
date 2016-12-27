__author__ = 'Long'

from GoogleNews import GoogleNewsParser

def main():
    parser = GoogleNewsParser.NewsParsers()
    parser.parse_data_from_tok()
    # print parser.get_texts()

if __name__ == '__main__':
    main()