import Pudmed

if __name__ == '__main__':
    searchword = Pudmed.user_input()
    id_list = Pudmed.info_pubmed(searchword)
    Pudmed.number_of_hits(id_list)


