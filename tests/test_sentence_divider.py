from langdetect import DetectorFactory

from open_llm_vtuber.utils.sentence_divider import (
    comma_splitter,
    contains_comma,
    contains_end_punctuation,
    detect_language,
    is_complete_sentence,
    segment_text_by_regex,
)

# langdetect e probabilistico; fixar a seed mantem o teste deterministico.
DetectorFactory.seed = 0


def test_is_complete_sentence():
    assert is_complete_sentence("Olá, tudo bem?")
    assert is_complete_sentence("Hello world.")
    assert not is_complete_sentence("sem pontuacao")


def test_contains_comma_and_splitter():
    assert contains_comma("primeira, segunda")
    assert not contains_comma("primeira segunda")
    head, tail = comma_splitter("primeira, segunda")
    assert head == "primeira,"
    assert tail.strip() == "segunda"


def test_contains_end_punctuation():
    assert contains_end_punctuation("fim!")
    assert not contains_end_punctuation("sem fim")


def test_segment_text_by_regex_keeps_remainder():
    sentences, remainder = segment_text_by_regex("Uma frase. Outra frase. resto")
    assert sentences == ["Uma frase.", "Outra frase."]
    assert remainder.strip() == "resto"


def test_detect_language_known_pairs():
    english = "This is a longer sentence written in English to make detection stable."
    assert detect_language(english) == "en"
    assert detect_language("こんにちは世界、お元気ですか。") == "ja"
    # "pt" nao esta em SUPPORTED_LANGUAGES (pysbd), entao o detector devolve None.
    portuguese = "Olá, como você está hoje? Este é um texto maior em português."
    assert detect_language(portuguese) is None
