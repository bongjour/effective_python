profile_dict_many = {
    "name": "홍길동",
    "age": 25,
    "height": 175,
    "country": "대한민국"
}


def myprofile_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{key} = {value}".format(key=key, value=value))


myprofile_kwargs(**profile_dict_many)
