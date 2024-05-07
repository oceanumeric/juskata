import pytest
from juskata import Num2Words


def test_num2words_initialization():
    # test the initialization of the class
    with pytest.raises(ValueError):
        Num2Words(20)
    with pytest.raises(ValueError):
        Num2Words("CN")


def test_convert_20_to_99():
    # initialize the class
    num2words = Num2Words(lang="BE")
    with pytest.raises(AssertionError):
        num2words._convert_20_to_99(0)
    with pytest.raises(AssertionError):
        num2words._convert_20_to_99(17)
    with pytest.raises(AssertionError):
        num2words._convert_20_to_99(120)
    assert num2words._convert_20_to_99(20) == "vingt"
    assert num2words._convert_20_to_99(21) == "vingt-et-un"
    assert num2words._convert_20_to_99(30) == "trente"
    assert num2words._convert_20_to_99(70) == "septante"
    assert num2words._convert_20_to_99(90) == "nonante"
    assert num2words._convert_20_to_99(99) == "nonante-neuf"


def test_convert_20_to_69():
    num2words = Num2Words(lang="FR")
    with pytest.raises(AssertionError):
        num2words._convert_20_to_69(0)
    with pytest.raises(AssertionError):
        num2words._convert_20_to_69(17)
    assert num2words._convert_20_to_69(20) == "vingt"
    assert num2words._convert_20_to_99(21) == "vingt-et-un"
    assert num2words._convert_20_to_99(30) == "trente"
    assert num2words._convert_20_to_99(57) == "cinquante-sept"


def test_convert_70_to_99():
    num2words = Num2Words(lang="FR")

    with pytest.raises(AssertionError):
        num2words._convert_20_to_69(0)
    with pytest.raises(AssertionError):
        num2words._convert_70_to_99(50)
    with pytest.raises(AssertionError):
        num2words._convert_70_to_99(120)

    assert num2words._convert_70_to_99(70) == "soixante-dix"
    assert num2words._convert_70_to_99(80) == "quatre-vingts"
    assert num2words._convert_70_to_99(90) == "quatre-vingt-dix"
    assert num2words._convert_70_to_99(87) == "quatre-vingt-sept"


def test_convert_tenths():

    num2words_fr = Num2Words(lang="FR")

    assert num2words_fr._convert_tens(56) == "cinquante-six"
    assert num2words_fr._convert_tens(70) == "soixante-dix"
    assert num2words_fr.convert(71) == "soixante-et-onze"
    assert num2words_fr._convert_tens(80) == "quatre-vingts"
    assert num2words_fr._convert_tens(80, set_pluras=False) == "quatre-vingt"
    assert num2words_fr._convert_tens(81) == "quatre-vingt-un"
    assert num2words_fr._convert_tens(91) == "quatre-vingt-onze"
    assert num2words_fr._convert_tens(95) == "quatre-vingt-quinze"


def test_convert_hundreds():

    num2words_fr = Num2Words(lang="FR")

    assert num2words_fr._convert_hundreds(100) == "cent"
    assert num2words_fr._convert_hundreds(200) == "deux-cents"
    assert num2words_fr._convert_hundreds(300) == "trois-cents"
    assert num2words_fr._convert_hundreds(343) == "trois-cent-quarante-trois"
    assert num2words_fr._convert_hundreds(400) == "quatre-cents"
    assert num2words_fr._convert_hundreds(500) == "cinq-cents"
    assert num2words_fr._convert_hundreds(571) == "cinq-cent-soixante-et-onze"
    assert num2words_fr._convert_hundreds(600) == "six-cents"
    assert num2words_fr._convert_hundreds(700) == "sept-cents"
    assert num2words_fr._convert_hundreds(800) == "huit-cents"
    assert num2words_fr._convert_hundreds(900) == "neuf-cents"
    assert num2words_fr._convert_hundreds(999) == "neuf-cent-quatre-vingt-dix-neuf"


def test_convert():

    # mainly test for lang = FR
    num2words_fr = Num2Words(lang="FR")

    test_nums1 = [x for x in range(0, 16)]
    test_strings1 = [
        "zéro",
        "un",
        "deux",
        "trois",
        "quatre",
        "cinq",
        "six",
        "sept",
        "huit",
        "neuf",
        "dix",
        "onze",
        "douze",
        "treize",
        "quatorze",
        "quinze",
        "seize",
    ]

    for num, string in zip(test_nums1, test_strings1):
        assert num2words_fr.convert(num) == string

    assert num2words_fr.convert(200) == "deux-cents"
    assert num2words_fr.convert(1110) == "mille-cent-dix"
    assert num2words_fr.convert(252) == "deux-cent-cinquante-deux"
    assert num2words_fr.convert(200000) == "deux-cent-milles"
    assert num2words_fr.convert(180000) == "cent-quatre-vingt-milles"

    # test 35, 101, 105, 111, 123
    assert num2words_fr.convert(35) == "trente-cinq"
    assert num2words_fr.convert(101) == "cent-un"
    assert num2words_fr.convert(105) == "cent-cinq"
    assert num2words_fr.convert(111) == "cent-onze"
    assert num2words_fr.convert(123) == "cent-vingt-trois"

    # test 199, 200, 201, 555, 999, 1000, 1001, 1111,
    assert num2words_fr.convert(199) == "cent-quatre-vingt-dix-neuf"
    assert num2words_fr.convert(200) == "deux-cents"
    assert num2words_fr.convert(201) == "deux-cent-un"
    assert num2words_fr.convert(555) == "cinq-cent-cinquante-cinq"
    assert num2words_fr.convert(999) == "neuf-cent-quatre-vingt-dix-neuf"
    assert num2words_fr.convert(1000) == "mille"
    assert num2words_fr.convert(1001) == "mille-un"
    assert num2words_fr.convert(1111) == "mille-cent-onze"

    #  test 9999, 10000, 11111, 12345, 123456, 654321, 999999
    assert num2words_fr.convert(9999) == "neuf-mille-neuf-cent-quatre-vingt-dix-neuf"
    # some online sources say "dix-mille" is correct, some say "dix-milles"
    assert num2words_fr.convert(10000) == "dix-milles"
    assert num2words_fr.convert(11111) == "onze-mille-cent-onze"
    assert num2words_fr.convert(12345) == "douze-mille-trois-cent-quarante-cinq"
    assert (
        num2words_fr.convert(123456)
        == "cent-vingt-trois-mille-quatre-cent-cinquante-six"
    )
    assert (
        num2words_fr.convert(654321)
        == "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un"
    )
    assert (
        num2words_fr.convert(999999)
        == "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf"
    )